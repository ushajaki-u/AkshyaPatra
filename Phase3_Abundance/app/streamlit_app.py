"""
Akshaya Patra — Safe Cookie Finder (Phase 3.2 MVP)
Rule-based allergen filter over the real Phase-1 Food Intelligence output.

Data source: Phase 1 -> CookieIntelligence.csv (USDA Branded Foods, cookie category).
This app is deploy-ready: it reads the CSV from ./data next to this file, so the
same path works on your laptop AND on Streamlit Cloud (Linux).
"""
import json
from pathlib import Path

import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# 1. PAGE CONFIG & STYLING  (brand look ported from the HTML mockup)
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
# 2. ALLERGEN SCOPE  (per roadmap Phase 1.2 — 7 allergens actually in the data)
# ---------------------------------------------------------
# SAFETY-CRITICAL: your pipeline labels differ from the display labels.
# If this map is wrong, an unsafe cookie could be shown as SAFE. Keep it exact.
ALLERGEN_LABEL_MAP = {
    "Milk": "Milk",
    "Eggs": "Eggs",
    "Wheat": "Wheat",
    "Sesame": "Sesame",
    "Peanuts": "Peanuts",
    "Tree nuts": "Tree Nuts",   # case fix
    "Soy": "Soybeans",          # word fix  <-- the one that matters most
}
# The 7 display labels the user can filter on (only what we can actually detect).
IN_SCOPE_ALLERGENS = list(ALLERGEN_LABEL_MAP.values())

DATA_PATH = Path(__file__).parent / "data" / "CookieIntelligence.csv"

# ---------------------------------------------------------
# 3. DATA LOADER  (the "plug-in" — real data replaces the mock list)
# ---------------------------------------------------------
def parse_allergens(tag_json: str) -> list[str]:
    """Turn the allergenTags dict-string into a list of present allergens (display labels).

    Fail-LOUD on safety: if the data ever contains an allergen key we don't know,
    we keep it (raw) rather than silently dropping it — hiding an allergen is the
    one thing an allergen app must never do.
    """
    try:
        tags = json.loads(tag_json) if isinstance(tag_json, str) else {}
    except (json.JSONDecodeError, TypeError):
        return []
    present = []
    for raw_label, flag in tags.items():
        if str(flag).strip().upper() == "Y":
            present.append(ALLERGEN_LABEL_MAP.get(raw_label, raw_label))  # unknown -> keep raw
    return present


@st.cache_data(show_spinner="Loading cookie intelligence…")
def load_cookies(path: Path = DATA_PATH) -> list[dict]:
    df = pd.read_csv(path)
    cookies = []
    for _, row in df.iterrows():
        desc = str(row["description"]).strip()
        # description bundles brand + product; split on the first comma as a reasonable guess
        if "," in desc:
            brand, name = desc.split(",", 1)
            brand, name = brand.strip(), name.strip()
        else:
            brand, name = "", desc
        cookies.append({
            "fdcId": row.get("fdcId", ""),
            "name": name,
            "brand": brand,
            "allergens": parse_allergens(row["allergenTags"]),
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

# ---------------------------------------------------------
# 5. USER INPUT
# ---------------------------------------------------------
col_user, _ = st.columns([2, 1])
with col_user:
    st.subheader("1. Profile & Allergen Preferences")
    user_name = st.text_input("Customer Name (Optional)", placeholder="e.g., Alex")
    selected_allergens = st.multiselect(
        label="Select allergens you wish to avoid:",
        options=IN_SCOPE_ALLERGENS,
        default=[],
        help="These 7 allergens are the ones currently detectable in the Phase-1 data "
             "(Fish and Crustacean Shellfish are not yet evaluated).",
    )

st.divider()

# ---------------------------------------------------------
# 6. RULE-BASED FILTERING ENGINE
# ---------------------------------------------------------
greeting = f"for **{user_name}**" if user_name else ""
st.subheader(f"2. Safe Cookie Recommendations {greeting}")

if selected_allergens:
    st.info(f"🚫 Filtering out products containing: **{', '.join(selected_allergens)}**")
else:
    st.warning("⚠️ No allergens selected. Showing general recommendations.")

# A cookie is safe if it contains NONE of the selected allergens.
safe_cookies = [
    c for c in COOKIES_DATA
    if not any(a in selected_allergens for a in c["allergens"])
]

# ---------------------------------------------------------
# 7. RESULTS  (counts + "show more" control)
# ---------------------------------------------------------
total_count = len(COOKIES_DATA)
safe_count = len(safe_cookies)

m1, m2 = st.columns(2)
m1.metric("🍪 Cookies in database", f"{total_count:,}")
m2.metric("✅ Safe for this profile", f"{safe_count:,}")

if safe_count == 0:
    st.error("No cookies match all your safety criteria. Try removing an allergen filter.")
else:
    # User chooses how many to see: default 5, up to 50 (or fewer if that's all we have).
    max_show = min(50, safe_count)
    if max_show > 5:
        n_show = st.slider("How many recommendations to show:",
                           min_value=5, max_value=max_show, value=5, step=5)
    else:
        n_show = max_show

    top_cookies = safe_cookies[:n_show]
    st.markdown(f"Showing **{len(top_cookies)}** of **{safe_count:,}** safe option(s):")
    st.markdown("""
    <div class="verify-banner">
        🔎 <b>Important Safety Check:</b> Always verify the physical product packaging and
        ingredient list before consumption. Formulations can change without notice.
    </div>
    """, unsafe_allow_html=True)

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

# ---------------------------------------------------------
# 8. DISCLAIMER
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
