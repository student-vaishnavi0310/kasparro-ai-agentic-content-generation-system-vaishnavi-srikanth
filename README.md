# Kasparro - Applied AI Engineer Challenge  
### 🚀 Multi-Agent Content Generation System 🚀


## Overview
A modular agentic automation system that takes a small product
dataset and automatically generates structured, machine-readable JSON content pages:

- `product_page.json` – Detailed product description
- `faq.json`         – FAQ page with ≥8 categorized Q&As
- `comparison_page.json` – Side-by-side comparison with a fictional Product B

## System Design Highlights

- **6 specialized agents** with single responsibilities and clear input/output
- **Orchestration** via a clean DAG-style pipeline in `main.py`
- **Reusable logic blocks** for content transformation (e.g., comparisons, answer generation)
- **Custom template engine** for consistent, machine-readable JSON output
- **Extensible structure** — easy to add new agents or templates


## Automation Flow (Orchestration Graph)

```mermaid
flowchart TD
    Raw["`Raw Product Data
(data.py)`"] --> Parser[ParserAgent]
    Parser --> Cleaned["`Cleaned Product Data`"]

    Cleaned --> QG[QuestionGeneratorAgent]
    QG --> Questions["`Categorized Questions`"]
    Questions --> FAQ[FAQAgent]
    FAQ --> FAQJson["`faq.json`"]

    Cleaned --> ProdPage[ProductPageAgent]
    ProdPage --> ProdJson["`product_page.json`"]

    Cleaned --> Fict[FictionalProductAgent]
    Fict --> ProductB["`Product B`"]
    ProductB --> Comp["`ComparisonAgent
(Product A + B)`"]
    Comp --> CompJson["`comparison_page.json`"]

    %% Color styling for better readability
    style Raw fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#000
    style Cleaned fill:#bbdefb,stroke:#1976d2,stroke-width:2px,color:#000

    style Parser fill:#424242,stroke:#fff,stroke-width:2px,color:#fff
    style QG fill:#424242,stroke:#fff,stroke-width:2px,color:#fff
    style FAQ fill:#424242,stroke:#fff,stroke-width:2px,color:#fff
    style ProdPage fill:#424242,stroke:#fff,stroke-width:2px,color:#fff
    style Fict fill:#424242,stroke:#fff,stroke-width:2px,color:#fff
    style Comp fill:#424242,stroke:#fff,stroke-width:2px,color:#fff

    style Questions fill:#f1f8e9,stroke:#689f38,stroke-width:2px,color:#000
    style ProductB fill:#f1f8e9,stroke:#689f38,stroke-width:2px,color:#000

    style FAQJson fill:#c8e6c9,stroke:#388e3c,stroke-width:3px,color:#000
    style ProdJson fill:#c8e6c9,stroke:#388e3c,stroke-width:3px,color:#000
    style CompJson fill:#c8e6c9,stroke:#388e3c,stroke-width:3px,color:#000
```
## How to Run:

```bash
python main.py
