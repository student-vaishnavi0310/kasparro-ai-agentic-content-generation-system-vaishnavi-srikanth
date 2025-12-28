# Problem Statement

Design and implement a modular agentic automation system that takes a small product dataset and automatically generates structured, machine-readable content pages (FAQ, Product Description, and Comparison pages) in JSON format.

The system must parse the provided product data, generate at least 15 categorized user questions, use reusable content logic blocks, apply custom templates, and produce the final pages through a multi-agent pipeline.

# Solution Overview

A Python-based multi-agent system processes the single provided product dataset through specialized agents with clear responsibilities.  
The orchestration is handled in `main.py` as a simple directed acyclic graph (DAG)-style pipeline:  
- Parsing → branches into FAQ generation, product page generation, and comparison page generation (with a fictional product).

All transformations are rule-based and derived strictly from the input data (no external facts or LLMs used).

# Scopes & Assumptions

- Only the provided product data is used.
- Generates exactly three JSON output files: `faq.json`, `product_page.json`, `comparison_page.json`.
- 18 categorized questions are generated (exceeding the minimum of 15).
- FAQ page contains at least 8 Q&As (exceeding the minimum of 5).
- Fictional Product B is statically defined but fully structured.
- No external libraries or internet access required — pure Python standard library + basic imports.

# System Design

## Agent Boundaries

Each agent is a class with a single `run()` method, clear input/output, and no shared global state:

- **ParserAgent**: Converts raw dict → clean internal model
- **QuestionGeneratorAgent**: Generates categorized questions from product data
- **FAQAgent**: Selects questions and generates answers → produces FAQ JSON
- **ProductPageAgent**: Builds product description page JSON
- **FictionalProductAgent**: Generates structured fictional Product B
- **ComparisonAgent**: Compares two products → produces comparison JSON

## Automation Flow / Orchestration Graph

Executed sequentially in `main.py` with branching:
