# Akshaya Patra — Food Intelligence for Safer Food Discovery

> **Netflix understands movies. Spotify understands music. Akshaya Patra understands food.**

**Discover More. Choose Safely. Eat with Confidence.**

[**Explore the live POC**](https://akshyapatra-rulebased.streamlit.app/)

Akshaya Patra is a food intelligence product concept designed to help people with food allergies and dietary restrictions discover products that better align with their individual requirements.

The project explores how product-level food information and customer-level intelligence can work together to make food discovery more informed and personalized.

**Current implementation:** A deployed, rule-based cookie discovery MVP using 13,308 USDA FoodData Central product records and seven allergen categories.

---

## The Problem

People managing food allergies and dietary restrictions often have to inspect product labels, interpret ingredient lists, and make decisions using incomplete or difficult-to-understand information.

The challenge is not simply finding products. It is understanding the relationship between what a product contains and what an individual or household needs to avoid.

<p align="center">
  <img src="./FAREConsumerJourney.png" alt="FARE consumer food-allergy journey" />
</p>

Akshaya Patra explores how food and customer intelligence can help address this problem.

![Akshaya Patra illustration](./Akshya_Patra_Chibi.png)

## My Product Approach

I am developing Akshaya Patra incrementally, starting with a focused, explainable MVP and building toward a broader personalized food discovery experience.

The product is organized around two complementary intelligence capabilities:

- **Food Intelligence:** Understand product ingredients, allergen information, and food attributes.
- **Customer Intelligence:** Represent individual and household requirements, preferences, and purchasing behaviour.

These capabilities are intended to inform a Recommendation Engine that supports personalized food discovery.

## Conceptual Product Architecture

![Akshya Patra Conceptual System Architecture](AK_ConceptualArchDiagram.png)

*This represents the intended product architecture, not the current implementation. It illustrates how Food Intelligence and Customer Intelligence are expected to contribute to the Recommendation Engine.*

## Development Journey

### Phase 1 — Food Intelligence

**Status: Initial rule-based implementation completed**

- Explored USDA FoodData Central Branded Foods data.
- Developed a cookie-focused product catalogue containing 13,308 records.
- Built a deterministic, keyword-based allergen identification process.
- Documented data provenance, scope decisions, and known classification limitations.

[Explore Phase 1 — Food Intelligence](Phase1_Food_Intelligence/README.md)

### Phase 2 — Customer Intelligence

**Status: Design and planning**

Exploring how customer and household profiles can represent allergen requirements, avoidance preferences, and purchasing behaviour.

The initial approach is to develop a controlled synthetic customer dataset that references actual products from Phase 1. Rule-based evaluation is the starting point, with ML/NLP and agent-based approaches considered as future exploration.

[Explore Phase 2 — Customer Intelligence](Phase2_Customer_Intelligence/README.md)

### Phase 3 — Rule-Based Cookie Discovery

**Status: Deployed MVP**

Built a Streamlit application that allows users to select allergens they wish to avoid and explore matching cookie products from the Phase 1 catalogue.

The application demonstrates how product-level intelligence can support a practical discovery experience.

[Explore Phase 3 — Cookie Discovery MVP](Phase3_Abundance/README.md)

## Product Decisions and Principles

Several decisions guide the development:

- **Start focused:** Begin with cookies rather than attempting to cover every food category.
- **Use real product data:** Product records and identifiers come from USDA FoodData Central.
- **Establish explainable rules first:** Build a deterministic baseline before exploring more advanced intelligence.
- **Separate product and customer intelligence:** Understand the product and the person independently before combining them.
- **Treat incomplete information carefully:** Missing or incomplete allergen information must not be interpreted as proof that a product is suitable.
- **Distinguish implementation from vision:** Clearly identify what works today and what remains future exploration.

## Technology

Python · Pandas · Streamlit · SQLite · JSON · USDA FoodData Central

Additional ML/NLP and agent technologies will be evaluated as the project evolves.

## Current Limitations and Next Steps

The deployed MVP is a rule-based cookie discovery prototype. It does not yet integrate the planned synthetic customer population, household shopping histories, personalized recommendation scoring, or AI agent capabilities.

Further work includes:

- Validating and improving allergen classification.
- Developing the synthetic customer data foundation.
- Exploring customer-level evaluation and recommendation approaches.
- Integrating Food Intelligence and Customer Intelligence.
- Improving the discovery experience and product explanations.

The long-term goal is to evolve from product-level filtering toward more informed, personalized food discovery.
