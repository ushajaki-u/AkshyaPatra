# 05 Qa Evals

Master placeholder documentation for Akshya Patra.
```mermaid
graph TD
    %% 1. Scenario Generator
    A["1. Scenario Generator (Python itertools)<br><i>Generates 127 allergen combinations</i>"] 
    -->|"Injects Allergen Profile"| B

    %% 2. Target Web App
    B["2. Target Web Application (Streamlit UI Surface)<br><i>Playwright drives live UI at: akshyapatra-rulebased.streamlit.app</i>"] 
    -->|"Scrapes Rendered Cookie Cards"| C

    %% 3. Random UI Sampler
    C["3. Random UI Sampler (Python random.sample)<br><i>Limits scraped results to 5 random cookies per run</i>"] 
    -->|"Sends Scraped Ingredient Text"| D

    %% 4. AI Audit Core
    D["4. Semantic AI Audit Core (Local Ollama LLM)<br><i>Independent auditor checks for hidden allergens</i>"] 
    -->|"Writes Pass/Fail Audit Logs"| E

    %% 5. Telemetry Registry
    E["5. Test Telemetry Registry<br><i>Saves final System Accuracy % to local JSON log</i>"]
