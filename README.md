# Akshaya Patra

> *Netflix understands movies. Spotify understands music. **Akshaya Patra understands food.***

**[Try the live demo »](https://akshyapatra-rulebased.streamlit.app/)**

## Vision

Akshaya Patra is an evolving Food Intelligence platform designed to help people discover foods that align with their dietary restrictions, preferences, and needs.

The long-term goal is to make food discovery more informed and more practical by connecting an understanding of food products with an understanding of the people choosing them.

## The Problem

![Consumer food-allergy journey](./FAREConsumerJourney.png)

People managing food allergies and other dietary restrictions often have to inspect product information themselves and make decisions with incomplete or difficult-to-interpret information. Grocery platforms can show what is available and what people have purchased, but they do not necessarily understand whether a product is suitable for a particular person.

## Conceptual System Architecture

The architecture brings together two complementary intelligence capabilities. **Food Intelligence** describes the products; **Customer Intelligence** describes the individual or household. Both contribute to the Recommendation Engine, which evaluates product suitability and supports personalized food discovery.

```mermaid
flowchart TB
    FI["Food Intelligence"]
    CI["Customer Intelligence"]
    RE["Recommendation Engine"]
    PFD["Personalized Food Discovery"]

    FI --> RE
    CI --> RE
    RE --> PFD

    classDef capability fill:#f5f5f5,stroke:#777,color:#222,stroke-width:1px;
    classDef engine fill:#eaeaea,stroke:#555,color:#222,stroke-width:1.2px;
    class FI,CI capability;
    class RE,PFD engine;
```

*This is a conceptual view of the intended system. It describes the capabilities and their relationships, not the current implementation or specific data providers.*

| Capability | Responsibility |
|---|---|
| **Food Intelligence** | Understands food products using information such as ingredients, allergens, and nutritional attributes |
| **Customer Intelligence** | Represents customer and household profiles, dietary restrictions, preferences, and shopping behavior |
| **Recommendation Engine** | Combines food and customer intelligence to assess product suitability and generate recommendations |
| **Personalized Food Discovery** | Presents relevant food options that align with an individual's or household's needs |

A confirmed allergen incompatibility is treated as a hard exclusion. A recommendation approach must not override that safety constraint.

## Current Project Focus

The project is being developed incrementally, with each phase building toward the conceptual architecture.

### Phase 1 — Food Intelligence

The initial implementation focuses on a cookie product catalogue and deterministic, rule-based allergen matching. Product ingredient and allergen information is used to identify options against selected dietary restrictions.

### Phase 2 — Customer Intelligence

This phase explores how customer and household profiles can represent dietary restrictions, preferences, and shopping behavior. A controlled synthetic customer population is being used for experimentation; it is not intended to represent a statistically representative sample of the US population.

### Phase 3 — Recommendation and Discovery

The longer-term direction is to bring Food Intelligence and Customer Intelligence together through a Recommendation Engine and deliver personalized food discovery.

## Intelligence Roadmap

Customer Intelligence is being explored in stages:

1. **Rule-Based Intelligence** — establish transparent, deterministic matching and decision logic.
2. **Hybrid Intelligence** — explore how machine learning or language-based techniques could complement rule-based methods.
3. **AI Agent-Based Intelligence** — explore agent-based capabilities as a future direction.

These are exploration milestones, not claims that all three approaches are currently implemented. Safety-critical allergen exclusions remain deterministic constraints.

## Longer-Term Opportunities

The broader vision may extend beyond food allergies to other dietary needs and restrictions, including celiac disease, diabetes-related dietary needs, hypertension-related dietary needs, and vegan or vegetarian preferences. These are future areas of exploration, not current MVP capabilities.

![Akshaya Patra illustration](./Akshya_Patra_Chibi.png)

## Key Value Proposition

> **Discover more. Choose safely. Eat with confidence.**
