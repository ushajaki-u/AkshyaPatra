# Phase 2 — Customer Intelligence

![Akshaya Patra Customer Intelligence](Akshaya%20Patra%20Synthetic%20Customer%20Intelligence-2.png)

**Synthetic Data Generation | Rule-Based Evaluation | Hybrid Intelligence**


## 1. Overview

Phase 2 introduces Customer Intelligence into Akshaya Patra.

While Phase 1 focuses on Food Intelligence through the classification and analysis of cookie products, Phase 2 introduces the customer dimension.

The objective is to understand individual customer allergen requirements, household composition and purchasing behaviour, and use this information to develop personalized food recommendations.

The work is organized around three interconnected areas:

1. Synthetic Customer Data Generation.
2. Rule-Based Customer–Allergen Evaluation.
3. Hybrid Intelligence using Machine Learning, NLP and AI techniques.

The initial implementation will focus exclusively on cookies, using the existing Phase 1 product catalogue.

## 2. Why Synthetic Data?

Publicly available datasets, including those explored through Hugging Face and Instacart, were investigated as potential sources of customer and purchasing information.

However, they did not provide the specific combination of information required for Akshaya Patra:

- Individual customer allergen profiles.
- Avoidance requirements across the nine major US food allergens.
- Household composition, including mixed and non-mixed households.
- Customer-specific shopping history.
- Cookie purchasing information that can be evaluated against the existing Phase 1 product catalogue.

Since suitable real-world customer data is not currently available, the decision is to create a controlled synthetic customer population.

Synthetic data will allow us to define customer characteristics, allergen combinations, household profiles and shopping behaviour through explicitly documented business rules.

## 3. Workstream 1 — Synthetic Customer Data Generation

### 3.1 Customer Population

The initial population will consist of **200 synthetic customers**.

The distribution is deliberately designed to represent different allergen combinations and customer profiles.

| Customer category | Generation rule | Count |
|---|---|---:|
| Single-allergen customers | 10 customers per allergen × 9 allergens | 90 |
| Multiple-allergen customers | 10 customers for each combination size, from 2 to 9 allergens | 80 |
| No declared allergies | Fixed population | 20 |
| Additional random profiles | Additional varied customer profiles | 10 |
| **Total** | | **200** |

This is a controlled experimental population, not a statistically representative sample of the US population.

### 3.2 Household Composition

Household information will be incorporated into the customer profiles.

Two household types will be represented:

- **Mixed households:** Household members have different allergen requirements.
- **Non-mixed households:** Household members have similar or shared allergen requirements.

Each customer record will include a household ID and household size.

### 3.3 Customer Allergen Profile

Each customer will have an individual avoidance score for each of the nine major US food allergens.

The nine allergens are:

1. Milk
2. Eggs
3. Fish
4. Crustacean Shellfish
5. Tree Nuts
6. Peanuts
7. Wheat
8. Soybeans
9. Sesame

Each allergen will have an independent avoidance score ranging from 0 to 5.

| Score | Interpretation |
|---|---|
| 0 | No declared avoidance |
| 1 | Low avoidance |
| 2 | Mild avoidance |
| 3 | Moderate avoidance |
| 4 | High avoidance |
| 5 | Absolute avoidance |

The score represents the customer's declared avoidance requirement, not medical allergy severity. Confirmed allergies, when represented, must be distinguished from preference-based avoidance and treated as safety constraints.

### 3.4 Annual Shopping History

Each customer will have an annual shopping history covering January through December.

Initial generation assumptions:

| Attribute | Scope |
|---|---:|
| Shopping period | 12 months |
| Shopping frequency | 1 trip per week |
| Shopping trips per customer | 52 |
| Total customers | 200 |
| Total shopping trips | 10,400 |

Each shopping trip may contain multiple cookie products and quantities.

Shopping dates will be assigned to calendar weeks, with the annual total maintained at 52 trips per customer.

## 4. JSON Data Structure

The proposed approach is **one JSON file per customer**.

Each file contains the complete customer profile and one year of shopping history.

### File Organization

```text
Phase2_Customer_Intelligence/
│
├── README.md
│
└── synthetic_data/
    │
    ├── customer_001.json
    ├── customer_002.json
    ├── customer_003.json
    ├── customer_004.json
    ├── ...
    └── customer_200.json
```

**200 customers = 200 JSON files.**

### Example: customer_001.json

The following is the proposed structure. Product IDs are illustrative placeholders and will be replaced with actual IDs from the Phase 1 cookie catalogue.

```json
{
  "customer_id": "CUST001",

  "household": {
    "household_id": "HH001",
    "number_of_people": 3,
    "household_type": "mixed"
  },

  "allergen_profile": {
    "milk": {
      "avoidance_score": 5
    },
    "eggs": {
      "avoidance_score": 0
    },
    "fish": {
      "avoidance_score": 0
    },
    "crustacean_shellfish": {
      "avoidance_score": 0
    },
    "tree_nuts": {
      "avoidance_score": 3
    },
    "peanuts": {
      "avoidance_score": 5
    },
    "wheat": {
      "avoidance_score": 0
    },
    "soybeans": {
      "avoidance_score": 2
    },
    "sesame": {
      "avoidance_score": 0
    }
  },

  "shopping_history": {
    "year": 2026,
    "months": {

      "January": {
        "weeks": {

          "week_1": {
            "shopping_trip": {
              "shopping_date": "2026-01-04",
              "products": [
                {
                  "product_id": "PRODUCT_ID_001",
                  "quantity": 2
                },
                {
                  "product_id": "PRODUCT_ID_002",
                  "quantity": 1
                }
              ]
            }
          },

          "week_2": {
            "shopping_trip": {
              "shopping_date": "2026-01-11",
              "products": [
                {
                  "product_id": "PRODUCT_ID_003",
                  "quantity": 1
                }
              ]
            }
          },

          "week_3": {},
          "week_4": {}
        }
      },

      "February": {
        "weeks": {}
      },
      "March": {
        "weeks": {}
      },
      "April": {
        "weeks": {}
      },
      "May": {
        "weeks": {}
      },
      "June": {
        "weeks": {}
      },
      "July": {
        "weeks": {}
      },
      "August": {
        "weeks": {}
      },
      "September": {
        "weeks": {}
      },
      "October": {
        "weeks": {}
      },
      "November": {
        "weeks": {}
      },
      "December": {
        "weeks": {}
      }
    }
  }
}
```

The abbreviated months and weeks above are for illustration. Generated files will contain the complete annual shopping history, with the agreed weekly shopping records.

## 5. Product Data Source

The existing Phase 1 cookie catalogue, containing approximately 13,000 products, will remain the source of truth for product information.

Synthetic shopping transactions will reference actual product IDs from this catalogue.

The following principles will apply:

- No synthetic cookie products.
- No invented product IDs.
- Product ingredients and allergen information will originate from the existing catalogue.
- Missing allergen information will not be interpreted as confirmed allergen absence.
- Initial experimentation will concentrate exclusively on cookies.

## 6. Workstream 2 — Rule-Based Customer–Allergen Evaluation

The second workstream will establish a deterministic, rule-based evaluation mechanism.

The objective is to evaluate each customer's requirements against each of the nine major allergens.

The evaluation will consider:

- Individual customer avoidance scores.
- Allergen-specific requirements.
- Product ingredient information.
- Allergen declarations and precautionary statements.
- Product compatibility with customer requirements.

A transparent grading mechanism will be developed to evaluate each customer–allergen combination.

The initial rule-based implementation will establish the baseline for customer–allergen evaluation.

The grading methodology, thresholds and interpretation will be documented as part of implementation.

**Safety principle:** Confirmed allergen incompatibilities must remain hard exclusions. A favourable score for another attribute cannot override a food-safety restriction.

## 7. Workstream 3 — Hybrid Intelligence: ML / NLP / AI Exploration

The third workstream will explore how Machine Learning, Natural Language Processing and AI techniques can complement the deterministic rule-based approach.

The objective is to investigate a hybrid evaluation mechanism that can improve customer–allergen assessment and support more intelligent personalization.

Potential areas of exploration include:

- Machine Learning-based customer evaluation.
- NLP for interpreting ingredient and allergen-related text.
- AI-assisted analysis of customer requirements.
- Combining rule-based evaluation with ML-derived scores.
- Generating customer-specific allergen grades on a scale of 1–5.
- Supporting personalized product recommendations.

The exact algorithms, models and hybrid architecture have not yet been finalized.

The rule-based implementation will provide the initial baseline against which future ML and AI approaches can be explored.

ML, NLP and AI will complement the safety rules; they will not override deterministic allergen exclusions.

## 8. Overall Phase 2 Objective

The three workstreams will come together to establish a Customer Intelligence layer for Akshaya Patra.

| Workstream | Primary outcome |
|---|---|
| Synthetic Data Generation | 200 customer profiles and annual shopping histories |
| Rule-Based Evaluation | Transparent customer–allergen evaluation and grading |
| Hybrid Intelligence | Exploration of ML, NLP and AI for enhanced evaluation and personalization |

The eventual objective is to combine Customer Intelligence with the existing Phase 1 Food Intelligence catalogue to support personalized cookie recommendations.

## 9. Proposed Technology

| Technology | Intended application |
|---|---|
| Python | Synthetic data generation and rule-based processing |
| Faker | Synthetic customer information |
| JSON | Individual customer profiles and shopping history |
| Pandas | Data manipulation and analysis |
| SQLite | Future exploration of relational storage |
| ML / NLP libraries | Future hybrid evaluation experiments |
| SDV | Future exploration of statistical synthetic data generation |

The initial implementation will use Python and explicitly defined business rules. Additional technologies will be introduced as the workstreams evolve.

---

**Phase 2 Status:** Design and planning in progress. Synthetic data generation, rule-based evaluation and hybrid intelligence implementation are planned workstreams.
