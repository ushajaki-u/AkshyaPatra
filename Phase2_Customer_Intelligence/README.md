# Phase 2 — Customer Intelligence

![Akshaya Patra Customer Intelligence](Akshaya%20Patra%20Synthetic%20Customer%20Intelligence-2.png)

**Synthetic Customer Data | Rule-Based Evaluation | Hybrid Intelligence | Future AI Exploration**

## 1. Overview

Phase 2 introduces Customer Intelligence into Akshaya Patra.

While Phase 1 focuses on Food Intelligence through the classification and analysis of cookie products, Phase 2 introduces the customer dimension.

The objective is to understand individual customer allergen requirements, household composition, and purchasing behaviour, and use this information to develop personalized food recommendations.

The initial scope focuses exclusively on cookies, using the existing Phase 1 product catalogue.

Phase 2 has two complementary dimensions:

- **Data foundation:** Generate a controlled synthetic customer population with allergen profiles and shopping histories.
- **Intelligence development:** Progressively develop customer evaluation capabilities, beginning with deterministic rules and moving toward hybrid ML/NLP and future AI agent-based approaches.

## 2. Customer Intelligence Roadmap

Customer Intelligence Roadmap Infographic.png

![Customer Intelligence Roadmap Infographic](Customer%20Intelligence%20Roadmap%20Infographic.png) 
The Customer Intelligence roadmap is a sequential learning and product development journey. Each milestone builds on the data, understanding, and outcomes of the previous milestone.

The roadmap represents planned future capabilities, not completed implementations.

### Foundation — Synthetic Customer Dataset

Create a population of 200 synthetic customers, including:

- Individual customer allergen profiles and avoidance scores.
- Household composition and relationships.
- Annual shopping histories.
- References to actual products in the Phase 1 cookie catalogue.

This dataset will serve as the common foundation for all three intelligence milestones.

### Milestone 1 — Rule-Based Intelligence

**Starting point | Deterministic and explainable evaluation**

Begin with explicitly defined business rules to establish a transparent customer intelligence baseline.

Planned areas of work:

- Evaluate customer allergen profiles and declared avoidance requirements.
- Analyze customer shopping history and purchased products.
- Examine product ingredients and recurring ingredient patterns.
- Explore customer–allergen relationships using deterministic rules.
- Establish an explainable evaluation baseline.

This is the first intelligence approach and the starting point for implementation.

### Milestone 2 — Hybrid Intelligence

**Next stage | Combining rules with ML/NLP**

Build on the rule-based baseline and explore how machine learning and natural language processing can add value.

Planned areas of exploration:

- Identify patterns that may not be captured by explicitly defined rules.
- Learn and experiment with suitable ML/NLP techniques and models.
- Investigate combining deterministic results with model-generated insights.
- Experiment with customer–allergen grades and scores.
- Compare model outputs against the rule-based baseline.

The specific algorithms, models, and evaluation methods will be determined during this milestone.

### Milestone 3 — AI Agent-Based Intelligence

**Future exploration | Agentic approaches**

Explore whether AI agents can extend customer intelligence capabilities beyond the earlier approaches.

Potential areas of exploration:

- Agent workflows and tool usage.
- Reasoning across customer requirements and product information.
- Retrieval and interpretation of relevant product and ingredient information.
- Explanations and evaluation of agent-generated results.
- Appropriate agent architectures, guardrails, and safety controls.

The agent architecture and implementation approach are intentionally open at this stage.

**Guiding principle:** Start with what we understand and can explicitly define, then progressively learn, experiment, and evaluate more advanced approaches.

Confirmed allergy incompatibilities will remain hard safety exclusions throughout every milestone.

## 3. Why Synthetic Data?

Publicly available datasets, including those explored through Hugging Face and Instacart, were investigated as potential sources of customer and purchasing information.

However, they did not provide the specific combination of information required for Akshaya Patra:

- Individual customer allergen profiles.
- Avoidance requirements across the nine major US food allergens.
- Household composition, including mixed and non-mixed households.
- Customer-specific shopping history.
- Cookie purchasing information that can be evaluated against the existing Phase 1 product catalogue.

Since suitable real-world customer data is not currently available, the decision is to create a controlled synthetic customer population.

Synthetic data will allow us to define customer characteristics, allergen combinations, household profiles, and shopping behaviour through explicitly documented generation rules.

The same dataset will support experimentation across all three intelligence milestones.

## 4. Workstream 1 — Synthetic Customer Data Generation

### 4.1 Customer Population

The initial population will consist of **200 synthetic customers**.

| Customer category | Generation rule | Count |
|---|---|---:|
| Single-allergen customers | 10 customers per allergen × 9 allergens | 90 |
| Multiple-allergen customers | 10 customers for each combination size, from 2 to 9 allergens | 80 |
| No declared allergies | Fixed population | 20 |
| Additional random profiles | Additional varied customer profiles | 10 |
| **Total** | | **200** |

This is a controlled experimental population, not a statistically representative sample of the US population.

### 4.2 Household Composition

Household information will be incorporated into the customer profiles.

Two household types will be represented:

- **Mixed households:** Household members have different allergen requirements.
- **Non-mixed households:** Household members have similar or shared allergen requirements.

Each customer record will include a household ID and household size.

### 4.3 Customer Allergen Profile

Each customer will have an individual avoidance score for each of the nine major US food allergens:

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

The score represents the customer's declared avoidance requirement, not medical allergy severity. Confirmed allergies must be distinguished from preference-based avoidance and treated as safety constraints.

### 4.4 Annual Shopping History

Each customer will have an annual shopping history covering January through December.

| Attribute | Scope |
|---|---:|
| Shopping period | 12 months |
| Shopping frequency | 1 trip per week |
| Shopping trips per customer | 52 |
| Total customers | 200 |
| Total shopping trips | 10,400 |

Each shopping trip may contain multiple cookie products and quantities.

Shopping dates will be assigned to calendar weeks, with the annual total maintained at 52 trips per customer.

## 5. JSON Data Structure

The proposed approach is **one JSON file per customer**.

Each file contains the complete customer profile and one year of shopping history.

### File Organization

```text
Phase2_Customer_Intelligence/
│
├── README.md
│
└── synthetic_data/
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
    "milk": {"avoidance_score": 5},
    "eggs": {"avoidance_score": 0},
    "fish": {"avoidance_score": 0},
    "crustacean_shellfish": {"avoidance_score": 0},
    "tree_nuts": {"avoidance_score": 3},
    "peanuts": {"avoidance_score": 5},
    "wheat": {"avoidance_score": 0},
    "soybeans": {"avoidance_score": 2},
    "sesame": {"avoidance_score": 0}
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
          }
        }
      }
    }
  }
}
```

The example is abbreviated for readability. Generated files will contain the complete annual shopping history and all agreed weekly shopping records.

## 6. Product Data Source

The existing Phase 1 cookie catalogue, containing approximately 13,000 products, will remain the source of truth for product information.

Synthetic shopping transactions will reference actual product IDs from this catalogue.

The following principles will apply:

- No synthetic cookie products.
- No invented product IDs.
- Product ingredients and allergen information will originate from the existing catalogue.
- Missing allergen information will not be interpreted as confirmed allergen absence.
- Initial experimentation will concentrate exclusively on cookies.

## 7. Workstream 2 — Rule-Based Customer–Allergen Evaluation

This workstream corresponds to **Milestone 1 of the Customer Intelligence Roadmap**.

The objective is to establish a deterministic, explainable evaluation mechanism that assesses customer requirements against the nine major food allergens.

The evaluation will consider:

- Individual customer avoidance scores.
- Allergen-specific requirements.
- Product ingredient information.
- Allergen declarations and precautionary statements.
- Product compatibility with customer requirements.
- Relevant patterns in customer shopping history.

A transparent grading mechanism will be developed to evaluate customer–allergen relationships.

The grading methodology, thresholds, and interpretation will be documented during implementation.

Shopping history may reveal purchasing patterns, but the absence of a product from a customer's history does not by itself establish an allergy or avoidance requirement. Explicit customer requirements and observed behaviour must be distinguished.

**Safety principle:** Confirmed allergen incompatibilities must remain hard exclusions. A favourable score for another attribute cannot override a food-safety restriction.

## 8. Workstream 3 — Hybrid Intelligence: ML / NLP Exploration

This workstream corresponds to **Milestone 2 of the Customer Intelligence Roadmap**.

The objective is to explore how Machine Learning and Natural Language Processing can complement the deterministic rule-based approach.

Potential areas of exploration include:

- Machine Learning-based customer evaluation.
- NLP for interpreting ingredient and allergen-related text.
- Identifying patterns that may not be captured by explicit rules.
- Combining rule-based evaluation with model-generated insights.
- Experimenting with customer–allergen grades and scores.
- Supporting personalized product recommendations.

The exact algorithms, models, and hybrid architecture have not yet been finalized.

The rule-based implementation will provide the initial baseline against which future ML/NLP approaches can be explored.

ML/NLP outputs will complement the safety rules; they will not override deterministic allergen exclusions.

## 9. Future Exploration — AI Agent-Based Intelligence

This is **Milestone 3 of the Customer Intelligence Roadmap**.

AI agent-based approaches are a future learning and exploration area, not a currently defined implementation workstream.

The objective will be to investigate whether agentic workflows can support more advanced customer intelligence by interacting with customer requirements, product information, and evaluation capabilities.

Potential areas of learning include:

- Agent workflows and tool integration.
- Reasoning and retrieval across customer and product information.
- Agent evaluation and output validation.
- Guardrails and food-safety controls.
- Appropriate agent frameworks and architectures.

The specific approach will be determined after gaining experience with the rule-based and hybrid milestones.

## 10. Overall Phase 2 Objective

Phase 2 will establish a Customer Intelligence layer that complements the Food Intelligence capabilities developed in Phase 1.

| Area | Intended outcome |
|---|---|
| Synthetic Data Generation | 200 customer profiles and annual shopping histories |
| Rule-Based Intelligence | Transparent customer–allergen evaluation |
| Hybrid Intelligence | Exploration of ML/NLP-enhanced evaluation |
| AI Agent-Based Intelligence | Future exploration of agentic capabilities |

The eventual objective is to combine Customer Intelligence with the Phase 1 Food Intelligence catalogue to support personalized cookie recommendations.

## 11. Proposed Technology

| Technology | Intended application |
|---|---|
| Python | Synthetic data generation and rule-based processing |
| Faker | Synthetic customer information |
| JSON | Individual customer profiles and shopping history |
| Pandas | Data manipulation and analysis |
| SQLite | Future exploration of relational storage |
| ML / NLP libraries | Future hybrid evaluation experiments |
| SDV | Future exploration of statistical synthetic data generation |
| Agent frameworks and tools | Future exploration during Milestone 3 |

Additional technologies will be evaluated and introduced as the roadmap progresses.

## 12. Project Status

**Phase 2: Design and planning in progress.**

The synthetic data foundation and rule-based evaluation are the initial areas of focus. Hybrid intelligence and AI agent-based approaches are planned future milestones.

The roadmap is intentionally progressive: each milestone will build on the knowledge, implementation experience, and evaluation results from the previous stage.
