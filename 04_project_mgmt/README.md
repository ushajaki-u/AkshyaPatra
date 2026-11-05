# Akshaya Patra --- Product Roadmap

![Akshaya Patra Product
Roadmap](images/akshaya-patra-product-roadmap.png)

**Transforming food anxiety into culinary abundance.**

## 1. Product Vision

Akshaya Patra is an AI-powered Food Intelligence and Discovery platform
designed to help people understand food products and discover options
aligned with their dietary requirements and preferences.

The long-term vision is to serve consumers first and, eventually, enable
partnerships with grocery retailers and food brands.

The product is built around three connected intelligence capabilities:

1.  **Food Intelligence** --- Understands food products, ingredients,
    allergens, and nutritional attributes.
2.  **Customer Intelligence** --- Represents dietary requirements and
    preferences using synthetic customer data for development and
    testing.
3.  **Recommendation Intelligence** --- Connects food and customer
    intelligence to support relevant food discovery.

## 2. Product Strategy

The initial market-entry strategy is consumer-facing:

-   Build a focused, demonstrable product.
-   Make the product accessible to people for feedback and testing.
-   Learn from feedback and improve the experience.
-   Use the working product and evidence from testing as a foundation
    for future retailer and food-brand conversations.

Potential future partners include grocery retailers such as Whole Foods,
Costco, Sam's Club, Target, and Kroger. These are long-term
opportunities, not current partnerships or commitments.

## 3. Product Roadmap

The roadmap is organized into a product-discovery foundation followed by
three capability phases. These are outcome-oriented stages, not calendar
commitments.

### Foundation --- Product Discovery and Strategy

**Objective:** Establish the product direction before expanding
implementation.

-   Define the problem and target users.
-   Understand food-discovery challenges associated with dietary
    restrictions.
-   Research the competitive landscape and identify differentiation
    hypotheses.
-   Define the product vision, value proposition, and strategic pillars.
-   Identify assumptions that require validation.

### Phase 1 --- Food Intelligence

**Objective:** Build the foundation for understanding food products
through structured product, ingredient, allergen, and nutritional
information.

The first proof of concept is **Cookie Allergen Discovery**. It is a
focused MVP within Food Intelligence, not the entirety of Akshaya Patra.

#### 1.1 --- Data Foundation: USDA Branded Foods

-   Acquire and inspect USDA Branded Foods data.
-   Understand available fields, ingredient information, and data
    limitations.
-   Identify the relevant food categories.
-   Establish data provenance and document known gaps.

#### 1.2 --- Category Focus: Cookies

-   Filter the Branded Foods dataset to the cookie category.
-   Create a structured dataset for the initial proof of concept.
-   Identify the seven allergens currently in scope: milk, eggs, tree
    nuts, peanuts, wheat, soy, and sesame.
-   Create consistent allergen attributes for downstream processing.

#### 1.3 --- Rule-Based Food Intelligence

-   Define allergen-identification rules.
-   Implement the initial rule-based classification approach.
-   Identify matches, non-matches, ambiguous cases, and missing
    information.
-   Make the classification logic explainable and traceable.

#### 1.4 --- Rule-Based Evaluation

-   Establish a test dataset and expected outcomes.
-   Evaluate classification results.
-   Measure precision, recall, and F1 where appropriate.
-   Review false positives, false negatives, and ambiguous ingredient
    cases.
-   Document limitations and improvement opportunities.

#### 1.5 --- Machine Learning Enhancement

-   Explore an ML-based approach to complement or improve the rule-based
    baseline.
-   Define data and labeling requirements.
-   Train or evaluate an appropriate model only when the dataset and
    labels support it.
-   Compare ML results with the rule-based baseline.
-   Assess whether the additional complexity provides measurable value.

#### 1.6 --- Food Intelligence Readiness

-   Consolidate the selected food-classification approach.
-   Document data quality, explainability, and known limitations.
-   Prepare the Food Intelligence capability for integration with
    Customer Intelligence.

**Phase 1 outcome:** A demonstrable Food Intelligence capability,
initially evaluated against the cookie allergen discovery use case.

### Phase 2 --- Customer Intelligence

**Objective:** Develop the ability to represent customer dietary
requirements and preferences without depending on access to real users'
personal or health data.

**Data strategy: Synthetic data only.**

Akshaya Patra will use collaboratively designed synthetic customer
profiles and scenarios for this phase. The project will not depend on
collecting real customer health records or personal dietary profiles.

-   Define representative customer personas and dietary scenarios.
-   Design synthetic customer profiles covering different restrictions,
    needs, and preferences.
-   Generate synthetic datasets for development and testing.
-   Define how customer attributes should be represented.
-   Test whether the system can interpret profile requirements
    consistently.
-   Document assumptions, limitations, and synthetic-data coverage.

**Phase 2 outcome:** A testable Customer Intelligence capability built
and evaluated using synthetic data.

Synthetic-data results will be treated as development and testing
evidence, not proof of real-world customer behavior or clinical
validity.

### Phase 3 --- Abundance: Integrated Consumer MVP

**Objective:** Bring Food Intelligence and Customer Intelligence
together in a user-friendly application that people can explore and
test.

This is where the individual capabilities become a demonstrable product
experience.

#### 3.1 --- Intelligence Integration

-   Integrate Food Intelligence from Phase 1.
-   Integrate synthetic Customer Intelligence profiles from Phase 2.
-   Connect product attributes with customer-profile requirements.
-   Implement the initial matching and recommendation logic.
-   Provide understandable explanations for results.

#### 3.2 --- Streamlit Application

-   Build a user-friendly Streamlit interface.
-   Enable people to explore food products.
-   Allow testing with predefined synthetic customer profiles.
-   Present relevant product and allergen information clearly.
-   Explain why a product matches or does not match a selected profile.
-   Clearly communicate missing, ambiguous, or unverified information.

#### 3.3 --- MVP Testing and Feedback

-   Make the application accessible to selected testers.
-   Invite feedback from relevant communities.
-   Collect structured product feedback, such as usability issues,
    clarity, missing information, and feature requests.
-   Provide a mechanism to review and organize feedback.
-   Prioritize improvements based on findings.
-   Iterate on the application and document product decisions.

Testing will focus on the usefulness, clarity, and usability of the
product experience. It will not treat application results as guarantees
that a food product is safe for an individual.

**Phase 3 outcome:** A shareable, consumer-facing Akshaya Patra MVP that
demonstrates the integration of Food Intelligence and Customer
Intelligence and supports structured feedback and iteration.

## 4. Cross-Cutting Product Principles

-   **Trust and transparency:** Explain how results are produced and
    identify uncertainty.
-   **Data quality:** Track data sources, completeness, freshness, and
    limitations.
-   **Safety first:** Never equate an ingredient-data match with a
    guarantee of food safety.
-   **Explainability:** Make classification and recommendation reasoning
    understandable.
-   **Privacy-aware design:** Use synthetic customer data for Customer
    Intelligence development and testing.
-   **Evaluation:** Define measurable criteria before claiming that a
    capability works.
-   **Iterative development:** Use technical evaluation and product
    feedback to guide improvements.

## 5. Roadmap Success Measures

  -----------------------------------------------------------------------
  Area                                What success looks like
  ----------------------------------- -----------------------------------
  Food Intelligence                   Reliable, explainable
                                      food-attribute and allergen
                                      classification on the defined test
                                      data

  Customer Intelligence               Representative synthetic profiles
                                      and consistent interpretation of
                                      their requirements

  Integration                         Correct and understandable matching
                                      between food attributes and
                                      synthetic customer profiles

  Application                         A usable, shareable Streamlit MVP

  Feedback                            Structured feedback that leads to
                                      documented product improvements

  Future readiness                    A credible product demonstration
                                      and evidence base for exploring
                                      retailer and food-brand
                                      partnerships
  -----------------------------------------------------------------------

## 6. Current Status and Scope

This roadmap describes the intended product direction. It does not imply
that every capability has been implemented or validated.

-   **Product Discovery:** Initial vision, problem framing, and
    strategic direction established; further validation remains ongoing.
-   **Phase 1:** USDA Branded Foods dataset acquired; cookie-focused
    rule-based implementation partially completed; formal evaluation
    remains outstanding.
-   **Phase 2:** Synthetic-data strategy established; profile design and
    generation are future work.
-   **Phase 3:** Integrated Streamlit MVP, external testing, and
    feedback workflow are future work.

## 7. Long-Term Vision

The cookie allergen discovery MVP is the starting point, not the
destination.

Akshaya Patra aims to grow from understanding individual food products
into connecting food intelligence with individual dietary needs,
enabling more informed food discovery for consumers.

Once the consumer-facing product has a credible demonstration and
evidence from testing, the next strategic opportunity is to explore how
this intelligence could support grocery retailers and food brands.

**Akshaya Patra: The right food, for the right person --- powered by
intelligence at every layer.**
