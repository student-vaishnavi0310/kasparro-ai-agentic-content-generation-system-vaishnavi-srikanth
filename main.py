import json

from data import raw_product_data
from orchestrator import Orchestrator

from agents.parser_agent import ParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.faq_agent import FAQAgent
from agents.product_page_agent import ProductPageAgent
from agents.fictional_product_agent import FictionalProductAgent
from agents.comparison_agent import ComparisonAgent


def main():
    # Initialize orchestrator
    orchestrator = Orchestrator()

    # Initialize agents (independent + autonomous)
    parser_agent = ParserAgent("ParserAgent")
    question_agent = QuestionGeneratorAgent("QuestionGeneratorAgent")
    faq_agent = FAQAgent("FAQAgent")
    product_page_agent = ProductPageAgent("ProductPageAgent")
    fictional_agent = FictionalProductAgent("FictionalProductAgent")
    comparison_agent = ComparisonAgent("ComparisonAgent")

    # ---- STEP 1: Parse raw product data ----
    cleaned_data = orchestrator.dispatch(
        parser_agent,
        {
            "type": "PARSE_PRODUCT",
            "data": raw_product_data
        }
    )

    # ---- STEP 2: Generate user questions ----
    questions = orchestrator.dispatch(
        question_agent,
        {
            "type": "GENERATE_QUESTIONS",
            "product": cleaned_data
        }
    )

    # ---- STEP 3: Generate FAQ content ----
    faq_content = orchestrator.dispatch(
        faq_agent,
        {
            "type": "GENERATE_FAQ",
            "questions": questions,
            "product": cleaned_data
        }
    )

    # ---- STEP 4: Generate product page ----
    product_content = orchestrator.dispatch(
        product_page_agent,
        {
            "type": "GENERATE_PRODUCT_PAGE",
            "product": cleaned_data
        }
    )

    # ---- STEP 5: Generate fictional product ----
    fictional_product = orchestrator.dispatch(
        fictional_agent,
        {
            "type": "GENERATE_FICTIONAL_PRODUCT"
        }
    )

    # ---- STEP 6: Generate comparison page ----
    comparison_content = orchestrator.dispatch(
        comparison_agent,
        {
            "type": "GENERATE_COMPARISON",
            "product_a": cleaned_data,
            "product_b": fictional_product
        }
    )

    # ---- Save outputs ----
    with open("faq.json", "w") as f:
        json.dump(faq_content, f, indent=4)

    with open("product_page.json", "w") as f:
        json.dump(product_content, f, indent=4)

    with open("comparison_page.json", "w") as f:
        json.dump(comparison_content, f, indent=4)

    print("Generated: faq.json, product_page.json, comparison_page.json")


if __name__ == "__main__":
    main()
