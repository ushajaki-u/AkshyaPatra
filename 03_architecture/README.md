# 03 — Architecture

> This README is automatically generated from the architecture documents.

# Akshaya Patra — Intelligence Model -Conceptual Arch
```text
User Intelligence ──┐
Food Intelligence ──┼──→ Recommendation
Sales Intelligence ─┘
```


---

# Akshaya Patra — Intelligence Architecture

```text
┌──────────────────────────┐   ┌──────────────────────────┐   ┌──────────────────────────┐
│    USER INTELLIGENCE     │   │    FOOD INTELLIGENCE     │   │   SALES INTELLIGENCE     │
├──────────────────────────┤   ├──────────────────────────┤   ├──────────────────────────┤
│ Customer Profile         │   │ Data Ingestion           │   │ Sales Data               │
│          ↓               │   │          ↓               │   │          ↓               │
│ Sensitivity              │   │ Cleaning / Filtering     │   │ Weekly Aggregation       │
│ Classification           │   │          ↓               │   │          ↓               │
│          ↓               │   │ Ingredient Processing    │   │ Demand Signal            │
│ Sensitivity Score        │   │          ↓               │   │                          │
│                          │   │ Allergen Classification  │   │                          │
│                          │   │          ↓               │   │                          │
│                          │   │ Product Labels           │   │                          │
└────────────┬─────────────┘   └────────────┬─────────────┘   └────────────┬─────────────┘
             │                              │                              │
             └───────────────┬──────────────┴──────────────┬───────────────┘
                             │                             │
                             ▼                             ▼
                  ┌────────────────────────────────────────────────┐
                  │              RECOMMENDATION ENGINE              │
                  ├────────────────────────────────────────────────┤
                  │ Eligibility Filter                             │
                  │                ↓                               │
                  │ Ranking                                        │
                  │                ↓                               │
                  │ Explanation                                    │
                  └────────────────────────────────────────────────┘
```

---

![HLD](HLD-diagram.png)

# Akshaya Patra — POC Implementation

```text
                         DATA SOURCES
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
        Product Data    Customer Data     Sales Data
          ~400K          Synthetic        Synthetic
              │               │               │
              ▼               ▼               ▼
        Python / Pandas   Python          Python
        Processing       Generator       Generator
              │               │               │
              ▼               ▼               ▼
        ~30K Cookies   Customer Profiles  Weekly Sales
              │               │               │
              ▼               │               │
       Food Intelligence      │               │
       Rules / ML / Hybrid    │               │
              │               │               │
              ▼               │               │
        Product Labels        │               │
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                         SQLite DB
                              │
                              ▼
                   Recommendation Engine
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              Eligibility            Ranking
                Filter                 │
                    │                  │
                    └────────┬─────────┘
                             ▼
                       Recommendation
                             │
                             ▼
                           Output
```
