# Akshaya Patra

> *Netflix understands movies. Spotify understands music. **Akshaya Patra understands food.***

**[Try the live demo »](https://akshyapatra-rulebased.streamlit.app/)**

## Vision

Akshaya Patra is an evolving Food Intelligence platform designed to help people discover foods that align with their dietary restrictions, preferences, and needs.

The long-term goal is to make food discovery more informed and more practical by connecting an understanding of food products with an understanding of the people choosing them.

## The Problem

<p align="center">
  <img src="./FAREConsumerJourney.png" alt="Consumer food-allergy journey" />
</p>

People managing food allergies and other dietary restrictions often have to inspect product information themselves and make decisions with incomplete or difficult-to-interpret information. Grocery platforms can show what is available and what people have purchased, but they do not necessarily understand whether a product is suitable for a particular person.

![Akshaya Patra illustration](./Akshya_Patra_Chibi.png)

## Conceptual System Architecture

The architecture brings together two complementary intelligence capabilities. **Food Intelligence** describes the products; **Customer Intelligence** describes the individual or household. Both contribute to the Recommendation Engine, which evaluates product suitability and supports personalized food discovery.

AK_ConceptualArchDiagram.png
![Akshaya Patra Conceptual System Architecture](AK_ConceptualArchDiagram.png)
*This is a conceptual view of the intended system. It describes the capabilities and their relationships, not the current implementation or specific data providers.*

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
