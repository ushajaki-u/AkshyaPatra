# 🗺️ System Design: Automated Quality Assurance Framework

**Project Name:** Akshaya Patra Integration Testing Suite  
**Objective:** A black-box testing framework to mathematically verify the accuracy of the cookie filtering pipeline by driving the UI and using a local LLM as an independent auditor.

---

## 1. System Architecture Diagram

```
 ┌────────────────────────────────────────────────────────┐
 │ 1. Scenario Generator (Python)                         │
 │    - Mathematically compiles 127 allergen profiles      │
 └───────────────────────────┬────────────────────────────┘
                             │ (Allergen List Injection)
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │ 2. UI Automation Web Driver (Playwright)               │
 │    - Launches browser -> Goes to local Streamlit URL   │
 │    - Inputs allergens into the multiselect widgets      │
 └───────────────────────────┬────────────────────────────┘
                             │ (Scrapes Webpage HTML Surface)
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │ 3. Stochastic UI Sampler (Random Filter)               │
 │    - Limits output to 5 random cookies per scenario    │
 └───────────────────────────┬────────────────────────────┘
                             │ (Extracts Clean Text Lines)
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │ 4. Semantic AI Audit Core (Local Ollama Engine)        │
 │    - Evaluates scraped text lines for hidden allergens  │
 └───────────────────────────┬────────────────────────────┘
                             │ (Saves Verification Telemetry)
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │ 5. Test Telemetry Registry                             │
 │    - Outputs final 'System Accuracy %' to local JSON   │
 └────────────────────────────────────────────────────────┘
```

---

## 2. Core Functional Steps (The 4-Stage Lifecycle)

### Stage 1: Exhaustive Scenario Generation
* **What it does:** Automatically calculates all possible testing inputs based on combinatorial subset mathematics.
* **The Math:** For the 7 active allergens in the app, the engine builds 2⁷ - 1 = 127 unique test profiles. 
* **Benefit:** Eliminates human testing bias and guarantees complete edge-case coverage.

### Stage 2: Front-End UI Emulation
* **What it does:** Drives an automated, headless browser instance directly to the active Streamlit app URL (`http://localhost:8501`).
* **Execution:** For each of the 127 profiles, it refreshes the view container, types the allergen constraints into the multi-select dropdown field, and triggers the update loop.

### Stage 3: Random Sub-Sampling (Stochastic Filtering)
* **What it does:** Bypasses browser memory limits and hardware rendering overhead when a query yields thousands of rows (e.g., thousands of cookies containing no milk).
* **Execution:** Instead of parsing the entire page footprint, the driver isolates the rendered cookie view cards and extracts a randomized sample pool capped at exactly 5 products.

### Stage 4: Independent AI Semantic Audit
* **What it does:** Uses a completely un-vetted, local language model (Ollama) as a digital health inspector to find logical bugs or data classification leaks in your main code.
* **Execution:** The driver takes the ingredient string scraped straight off the screen and passes it to Ollama. The model uses its pre-trained biochemistry knowledge to flag hidden derivatives (like "whey" or "casein" for a milk restriction) and writes a permanent validation report back to a local logging file.

---

## 3. Key Design Benefits
* **Implementation Agnostic:** The test suite treats your application as a complete black box. It works identically whether your backend is written with basic text rules, an NLP vector database, or complex multi-agent setups.
* **100% Secure & Local:** Running your frontend via local loops and your reasoning engine through Ollama on `localhost:11434` means the entire pipeline executes safely on your laptop without any data exposure or cloud usage bills.

---
*This is for informational purposes only. For medical advice or diagnosis, consult a professional. AI responses may include mistakes.*
