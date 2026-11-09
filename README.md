# Akshaya Patra

> *Netflix understands movies. Spotify understands music. **Akshaya Patra understands food.***

**[Try the live demo »](https://akshyapatra-rulebased.streamlit.app/)**

## Vision

Akshaya Patra is an evolving Food Intelligence platform designed to help people discover foods that align with their dietary restrictions, preferences, and needs.

The long-term goal is to make food discovery more informed and more practical by connecting an understanding of food products with an understanding of the people choosing them.

## The Problem

![Consumer food-allergy journey](./FAREConsumerJourney.png)

People managing food allergies and other dietary restrictions often have to inspect product information themselves and make decisions with incomplete or difficult-to-interpret information. Grocery platforms can show what is available and what people have purchased, but they do not necessarily understand whether a product is suitable for a particular person.

![Akshaya Patra illustration](./Akshya_Patra_Chibi.png)

## Conceptual System Architecture

The architecture brings together two complementary intelligence capabilities. **Food Intelligence** describes the products; **Customer Intelligence** describes the individual or household. Both contribute to the Recommendation Engine, which evaluates product suitability and supports personalized food discovery.

AK_ConceptualArchDiagram.png
![Akshaya Patra Conceptual System Architecture](AK_ConceptualArchDiagram.png)

```mermaid
graph TD
    subgraph AP ["AKSHAYA PATRA"]
        direction TD
        SubTitle["Conceptual System Architecture"] --- Blank[ ]
        style Blank fill:none,stroke:none;
        style SubTitle fill:none,stroke:none,font-weight:bold,font-size:14px;

        subgraph Inputs [" "]
            direction LR
            FI["<b>FOOD INTELLIGENCE</b><br/><br/>Product information<br/>Ingredients<br/>Allergen information"]
            CI["<b>CUSTOMER INTELLIGENCE</b><br/><br/>Customer profiles<br/>Restrictions and preferences<br/>Shopping history"]
        end

        RE["<b>RECOMMENDATION ENGINE</b><br/><br/>Combines food and customer intelligence to evaluate product suitability and generate recommendations."]
        
        FD["<b>PERSONALIZED FOOD DISCOVERY</b><br/><br/>Relevant and suitable food recommendations"]

        FI --> RE
        CI --> RE
        RE --> FD
    end

    %% Minimalist Border & Box Styling
    style AP fill:#fafafa,stroke:#e0e0e0,stroke-width:1px,rx:10px,color:#111111;
    style Inputs fill:none,stroke:none;
    style FI fill:#ffffff,stroke:#cccccc,stroke-width:1px,rx:6px;
    style CI fill:#ffffff,stroke:#cccccc,stroke-width:1px,rx:6px;
    style RE fill:#ffffff,stroke:#cccccc,stroke-width:1px,rx:6px;
    style FD fill:#ffffff,stroke:#cccccc,stroke-width:1px,rx:6px;


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


## Longer-Term Opportunities

The broader vision may extend beyond food allergies to other dietary needs and restrictions, including celiac disease, diabetes-related dietary needs, hypertension-related dietary needs, and vegan or vegetarian preferences. These are future areas of exploration, not current MVP capabilities.



## Key Value Proposition

> **Discover more. Choose safely. Eat with confidence.**
