"""
Akshaya Patra — Safe Cookie Finder (Phase 3.2 MVP)
Rule-based allergen filter over the real Phase-1 Food Intelligence output.

Two tabs:
  1. Find safe cookies  — pick the allergens you avoid, get a list of safe cookies.
  2. Check a cookie      — pick ONE specific cookie, see its allergens AND the exact
                           ingredient that triggered each one (explainability).

Data source: Phase 1 -> CookieIntelligence.csv (USDA Branded Foods, cookie category).
Reads the CSV from ./data next to this file, so the path works locally AND on Streamlit Cloud.
"""
import json
import re
from pathlib import Path

import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# 1. PAGE CONFIG & STYLING
# ---------------------------------------------------------
st.set_page_config(page_title="Akshaya Patra - Safe Cookie Finder", page_icon="🍪", layout="wide")

st.markdown("""
    <style>
    .main-header { font-size: 2.3rem; color: #064e3b; font-weight: 800; margin-bottom: 0; }
    .sub-header  { font-size: 1.05rem; color: #b45309; font-weight: 600; margin-bottom: 18px; }
    .verify-banner {
        background-color: #e8f5e9; border: 1px solid #a5d6a7; padding: 12px;
        border-radius: 8px; margin-bottom: 15px; color: #1b5e20; font-weight: 500;
    }
    .disclaimer-box {
        background-color: #fff3e0; border-left: 5px solid #ff9800; padding: 15px;
        border-radius: 6px; margin-top: 25px; font-size: 0.86rem; color: #424242;
    }
    .safe-badge {
        background:#10b981; color:white; font-weight:700; font-size:0.8rem;
        padding:4px 12px; border-radius:10px; display:inline-block;
    }
    .warn-badge {
        background:#f43f5e; color:white; font-weight:700; font-size:0.8rem;
        padding:4px 12px; border-radius:10px; display:inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. ALLERGEN SCOPE
# ---------------------------------------------------------
# SAFETY-CRITICAL: the pipeline's raw labels differ from the display labels.
ALLERGEN_LABEL_MAP = {
    "Milk": "Milk",
    "Eggs": "Eggs",
    "Wheat": "Wheat",
    "Sesame": "Sesame",
    "Peanuts": "Peanuts",
    "Tree nuts": "Tree Nuts",   # case fix
    "Soy": "Soybeans",          # word fix
}
IN_SCOPE_ALLERGENS = list(ALLERGEN_LABEL_MAP.values())

DATA_PATH = Path(__file__).parent / "data" / "CookieIntelligence.csv"

# ---------------------------------------------------------
# 2b. EXPLAINABILITY ENGINE  (reuses the EXACT Phase-1 keyword dictionary + logic)
# Source of truth: Phase1_Food_Intelligence/RuleBased/src/02_levelcleanupcookies.py
# Copied here verbatim so the trigger we SHOW always matches the Y/N tag in the data.
# ---------------------------------------------------------
ALLERGEN_DICT = {
    "Milk": ["milk", "butter", "cream", "whey", "lactose", "casein", "caseinate",
             "yogurt", "cheese", "ghee", "buttermilk", "curd"],
    "Wheat": ["wheat", "flour", "semolina", "spelt", "kamut", "triticale"],
    "Eggs": ["egg", "albumen", "ovalbumin", "yolk"],
    "Sesame": ["sesame", "tahini", "benne", "gingelly", "til"],
    "Tree nuts": ["cashew", "pistachio", "pecan", "almond", "walnut", "hazelnut",
                  "macadamia", "chestnut", "brazil nut", "hickory"],
    "Peanuts": ["peanut", "arachis"],
    "Soy": ["soy", "soya", "soybean", "lecithin", "tofu", "edamame"],
}


def explain_allergens(ingredients_text):
    """Re-scan one cookie's ingredients to find WHICH word triggered each allergen.

    Mirrors Phase-1 scan_ingredients() exactly (same keywords, same non-dairy exclusion),
    so the Y/N status is identical to the stored tags; additionally captures the matched
    ingredient(s) for display. Cocoa-butter / coconut-milk are excluded from Milk triggers
    so we never mislead the user about why a flag fired.
    """
    result = {a: {"status": "N", "triggers": []} for a in ALLERGEN_DICT}
    if not ingredients_text:
        return result
    t = str(ingredients_text).lower()

    for allergen, keywords in ALLERGEN_DICT.items():
        trig = []
        for kw in keywords:
            for m in re.finditer(r"\b" + re.escape(kw) + r"s?\b", t):
                if allergen == "Milk":
                    pre = t[max(0, m.start() - 8):m.start()]
                    if kw == "butter" and "cocoa" in pre:
                        continue
                    if kw == "milk" and "coconut" in pre:
                        continue
                trig.append(m.group(0))
        if trig:
            result[allergen] = {"status": "Y", "triggers": sorted(set(trig))}

    # Phase-1 non-dairy exclusion (keeps Milk Y/N identical to the stored tag)
    if result["Milk"]["status"] == "Y":
        all_milk = re.findall(r"\b(milk|butter)s?\b", t)
        false_pos = t.count("cocoa butter") + t.count("coconut milk")
        if len(all_milk) <= false_pos:
            remaining = [k for k in ALLERGEN_DICT["Milk"] if k not in ("milk", "butter")]
            still_dairy = any(re.search(r"\b" + re.escape(k) + r"s?\b", t) for k in remaining)
            if not still_dairy:
                result["Milk"] = {"status": "N", "triggers": []}
    return result


# ---------------------------------------------------------
# 3. DATA LOADER
# ---------------------------------------------------------
def parse_allergens(tags: dict) -> list[str]:
    present = []
    for raw_label, flag in tags.items():
        if str(flag).strip().upper() == "Y":
            present.append(ALLERGEN_LABEL_MAP.get(raw_label, raw_label))
    return present


@st.cache_data(show_spinner="Loading cookie intelligence…")
def load_cookies(path: Path = DATA_PATH) -> list[dict]:
    df = pd.read_csv(path)
    cookies = []
    for _, row in df.iterrows():
        desc = str(row["description"]).strip()
        if "," in desc:
            brand, name = desc.split(",", 1)
            brand, name = brand.strip(), name.strip()
        else:
            brand, name = "", desc
        try:
            tags = json.loads(row["allergenTags"]) if isinstance(row["allergenTags"], str) else {}
        except (json.JSONDecodeError, TypeError):
            tags = {}
        cookies.append({
            "fdcId": row.get("fdcId", ""),
            "name": name,
            "brand": brand,
            "tags": tags,                      # raw Y/N per allergen (source of truth)
            "allergens": parse_allergens(tags),
            "ingredients": str(row["ingredients"]),
        })
    return cookies


COOKIES_DATA = load_cookies()

# ---------------------------------------------------------
# 4. HEADER
# ---------------------------------------------------------
st.markdown('<div class="main-header">🍃 Akshaya Patra</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Transforming Food Anxiety into Culinary Abundance</div>', unsafe_allow_html=True)
st.markdown(f"**Phase 3 — Streamlit MVP**  ·  Rule-based allergen discovery over "
            f"**{len(COOKIES_DATA):,} real cookie products** (USDA Branded Foods).")
st.divider()

tab_find, tab_check = st.tabs(["🔍 Find safe cookies", "🍪 Check a cookie"])

# =========================================================
# TAB 1 — FIND SAFE COOKIES  (original flow, unchanged)
# =========================================================
with tab_find:
    col_user, _ = st.columns([2, 1])
    with col_user:
        st.subheader("1. Profile & Allergen Preferences")
        user_name = st.text_input("Customer Name (Optional)", placeholder="e.g., Alex")
        selected_allergens = st.multiselect(
            label="Select allergens you wish to avoid:",
            options=IN_SCOPE_ALLERGENS, default=[],
            help="These 7 allergens are the ones currently detectable in the Phase-1 data "
                 "(Fish and Crustacean Shellfish are not yet evaluated).",
        )

    st.divider()
    greeting = f"for **{user_name}**" if user_name else ""
    st.subheader(f"2. Safe Cookie Recommendations {greeting}")

    if selected_allergens:
        st.info(f"🚫 Filtering out products containing: **{', '.join(selected_allergens)}**")
    else:
        st.warning("⚠️ No allergens selected. Showing general recommendations.")

    safe_cookies = [c for c in COOKIES_DATA
                    if not any(a in selected_allergens for a in c["allergens"])]

    total_count, safe_count = len(COOKIES_DATA), len(safe_cookies)
    m1, m2 = st.columns(2)
    m1.metric("🍪 Cookies in database", f"{total_count:,}")
    m2.metric("✅ Safe for this profile", f"{safe_count:,}")

    if safe_count == 0:
        st.error("No cookies match all your safety criteria. Try removing an allergen filter.")
    else:
        max_show = min(50, safe_count)
        n_show = st.slider("How many recommendations to show:", 5, max_show, 5, 5) if max_show > 5 else max_show
        top_cookies = safe_cookies[:n_show]
        st.markdown(f"Showing **{len(top_cookies)}** of **{safe_count:,}** safe option(s):")
        st.markdown("""<div class="verify-banner">🔎 <b>Important Safety Check:</b> Always verify the
            physical product packaging and ingredient list before consumption. Formulations can
            change without notice.</div>""", unsafe_allow_html=True)
        for i, cookie in enumerate(top_cookies, 1):
            title = cookie["name"] if not cookie["brand"] else f"{cookie['name']}  ·  {cookie['brand']}"
            with st.expander(f"#{i} — {title}", expanded=(n_show <= 5)):
                if cookie["allergens"]:
                    st.markdown(f'<span class="warn-badge">Contains: {", ".join(cookie["allergens"])}</span>',
                                unsafe_allow_html=True)
                else:
                    st.markdown('<span class="safe-badge">No Top-7 allergens detected</span>',
                                unsafe_allow_html=True)
                st.markdown("**Full Ingredients:**")
                st.write(f"_{cookie['ingredients']}_")
                st.caption(f"USDA FoodData Central ID: {cookie['fdcId']}")

# =========================================================
# TAB 2 — CHECK A COOKIE  (new: lookup + Level-2 explainability)
# =========================================================
with tab_check:
    st.subheader("Is a specific cookie safe for you?")
    st.caption("Type to search. Only the 13,308 cookies in our database are selectable — "
               "if a cookie isn't here, we don't have its data (we won't guess).")

    labels = [f"{c['name']} · {c['brand']}".strip(" ·") for c in COOKIES_DATA]
    idx = st.selectbox(
        "Search a cookie by name or brand (e.g., Oreo):",
        options=range(len(COOKIES_DATA)),
        format_func=lambda i: labels[i],
        index=None,
        placeholder="Start typing… e.g. Oreo",
    )

    if idx is not None:
        cookie = COOKIES_DATA[idx]
        st.markdown(f"#### {cookie['name']}" + (f"  ·  {cookie['brand']}" if cookie["brand"] else ""))
        st.caption(f"USDA FoodData Central ID: {cookie['fdcId']}")

        explain = explain_allergens(cookie["ingredients"])
        rows_html = ""
        for raw in ALLERGEN_DICT:                       # fixed order, all 7 shown
            label = ALLERGEN_LABEL_MAP.get(raw, raw)
            status = str(cookie["tags"].get(raw, "N")).upper()   # stored tag = source of truth
            if status == "Y":
                trig = ", ".join(explain[raw]["triggers"]) or "listed in the ingredients"
                rows_html += (f'<div style="margin:7px 0;">'
                              f'<span class="warn-badge">⛔ CONTAINS {label}</span>'
                              f'&nbsp;&nbsp;<span style="color:#b91c1c;">from: <b>{trig}</b></span></div>')
            else:
                rows_html += (f'<div style="margin:7px 0;">'
                              f'<span class="safe-badge">✓ {label}</span>'
                              f'&nbsp;&nbsp;<span style="color:#6b7280;">not detected</span></div>')
        st.markdown("##### Allergen profile")
        st.markdown(rows_html, unsafe_allow_html=True)

        st.markdown("""<div class="verify-banner">🔎 <b>Verify before you eat:</b> this is based on the
            USDA ingredient text, which can be incomplete or out of date. <b>Always read the physical
            package label</b> — and when in doubt, don't.</div>""", unsafe_allow_html=True)

        with st.expander("See the full ingredient list"):
            st.write(f"_{cookie['ingredients']}_")

# ---------------------------------------------------------
# DISCLAIMER (shown under both tabs)
# ---------------------------------------------------------
st.markdown("""
<div class="disclaimer-box">
    <b>⚖️ Legal & Medical Disclaimer:</b><br>
    Akshaya Patra is an educational MVP prototype for information discovery only. It does NOT
    provide medical, dietary, or legal advice, and a data match is never a guarantee of safety.
    Data is derived from public USDA datasets and may be incomplete. Always read the physical
    package label and consult a qualified allergist for personal health guidance.
</div>
""", unsafe_allow_html=True)
