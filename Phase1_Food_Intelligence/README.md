# Akshaya Patra — Phase 1 (Rule-Based) Data Provenance

_Last updated: 2026-11-06. Documents where the cookie data comes from, how it is
transformed, and the known gaps — so we don't forget the decisions behind the numbers._

---

## 1. Source dataset

| | |
|---|---|
| **File** | `rawdata/FoodData_Central_branded_food_json_2026-04-30.json` |
| **Source** | USDA FoodData Central — Branded Foods |
| **Download date** | 2026-04-30 (in the filename) |
| **Size on disk** | ~3.1 GB |
| **Total records** | **455,458** branded-food products |
| **Distinct `brandedFoodCategory` values** | 352 |

> 455,458 is the **entire** branded-foods database (all foods, all categories), **not**
> the cookie count. The cookie count comes from filtering this down (step 01 below).

---

## 2. The cookie count — and the coverage gap (IMPORTANT)

Step 01 keeps only records whose category is **exactly** `"Cookies & Biscuits"` → **13,308**.

But cookies/biscuits also live in **other** categories that the exact match skips. A full
scan of the raw file (2026-11-06) found:

| Cookie/biscuit category | Records |
|---|---|
| **Cookies & Biscuits**  *(what we currently keep)* | **13,308** |
| Cake, Cookie & Cupcake Mixes | 3,367 |
| Biscuits/Cookies | 1,870 |
| Frozen Breakfast Sandwiches, Biscuits & Meals | 973 |
| Biscuits/Cookies (Shelf Stable) | 334 |
| Breakfast Sandwiches, Biscuits & Meals | 298 |
| Biscuits Cracker / Chocolate / Plain / Kids / Cakes-Slices-Biscuits | ~29 |
| **Total in ANY cookie/biscuit-named category** | **20,179** |
| (Records whose *description* contains "cookie") | 15,187 |

**Known gap:** we currently capture **13,308 of ~20,179** cookie-ish records. The clearest
omissions are **`Biscuits/Cookies` (1,870)** and `Biscuits/Cookies (Shelf Stable)` (334) —
unambiguous cookies. "Cake, Cookie & Cupcake Mixes" (3,367) are mixes, not finished
cookies, so excluding them is defensible.

**DECISION (2026-11-06): keep the single exact category (13,308) for the MVP.** A smaller,
cleaner dataset is better for an MVP — widening coverage is easy to add later and hard to
justify now. This is a **deliberate scope choice, not a bug or an oversight.** To broaden
later, change `TARGET` in `01_levelcleanupcookies.py` from a single string to a set of
categories (e.g. add `Biscuits/Cookies`).

---

## 3. Pipeline — step by step

Row count changes **only at step 01**; every later step preserves all 13,308 rows.

| Script | Purpose | Input → Output | Rows |
|---|---|---|---|
| `01_levelcleanupcookies.py` | **Extract.** Stream the 3.1 GB raw JSON (ijson); keep records where `brandedFoodCategory == "Cookies & Biscuits"` (exact). Writes a run report. | raw JSON → `output/cookiesjuly2026.json` (+ `_report.txt`) | 455,458 → **13,308** |
| `02_levelcleanupcookies.py` | **Tag allergens.** Rule-based keyword scan of each ingredient string (dictionary per allergen, word-boundary + plural-aware regex). Includes a *non-dairy exclusion* that flips Milk→N when the only hits are "cocoa butter" / "coconut milk". | `cookiesjuly2026.json` → `output/CookieAllergenTagged.json` | 13,308 |
| `03_levelcleanupcookies.py` | **Load to DB.** Insert tagged records into SQLite (`cookies` table; `fdcId` primary key; `allergenTags` stored as JSON text). | `CookieAllergenTagged.json` → `output/CookieIntelligence.db` | 13,308 |
| `04_query_cookies.py` | **Validate (read-only).** Interactive CLI: pick an allergen + Y/N; uses SQLite `json_extract` to count/preview matches. The command-line ancestor of the Streamlit filter. | reads `CookieIntelligence.db` | — |
| `05_ai_evaluator.py` | AI-based evaluation (see roadmap Phase 1.4/1.5 — not documented here yet). | — | — |
| `06_testcookiedb_foodsjson.py` | Test script. | — | — |
| `07_FoodIntelligenceOOP.py` | Object-oriented refactor of the pipeline. | — | — |
| `08_dbtocsv.py` | **Export.** Dump the DB table to CSV — the file the Streamlit app loads. | `CookieIntelligence.db` → `output/CookieIntelligence.csv` | **13,308** |

---

## 4. Allergen tagging — scope & method

**7 allergens tracked** (the ones present in cookie data): **Milk, Wheat, Eggs, Sesame,
Tree nuts, Peanuts, Soy.** Fish and Crustacean Shellfish are **out of scope** (not
meaningfully present in cookies).

Method = **rule-based keyword matching** per allergen (e.g. Milk ← milk, butter, whey,
casein, lactose…; Soy ← soy, lecithin, tofu, edamame…), word-boundary regex, plural-aware.
Special case: non-dairy exclusion for cocoa-butter / coconut-milk false positives.

**Known limitations (rule-based):** can produce false positives (e.g. an ingredient that
merely *contains* a keyword) and false negatives (an allergen named in a way not in the
dictionary). Formal precision/recall/F1 evaluation is roadmap Phase 1.4 — still outstanding.

---

## 5. App integration note (Phase 3)

The Streamlit app (`Phase3_Abundance/app/streamlit_app.py`) reads `CookieIntelligence.csv`
and **normalizes two labels** so the UI filter matches the data — **safety-critical**:

- data `"Soy"` → UI **"Soybeans"**
- data `"Tree nuts"` → UI **"Tree Nuts"**

If this mapping is wrong, a cookie containing an allergen could be shown as SAFE.

---

## 6. Current status (2026-11-06)

- Raw data acquired; cookie-focused rule-based pipeline implemented; CSV = 13,308 rows.
- **Decided (2026-11-06):** keep single category (13,308) for MVP — smaller dataset is better.
- **Outstanding:** formal allergen-tagging evaluation (Phase 1.4); ML enhancement (Phase 1.5).
