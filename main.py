import json
from data import raw_product_data
from agents.parser_agent import ParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.faq_agent import FAQAgent
from agents.product_page_agent import ProductPageAgent
from agents.fictional_product_agent import FictionalProductAgent
from agents.comparison_agent import ComparisonAgent

# Orchestration: Simple sequential pipeline (DAG-like: parser branches to others)
parser = ParserAgent()
cleaned_data = parser.run(raw_product_data)

question_gen = QuestionGeneratorAgent()
questions = question_gen.run(cleaned_data)

faq_agent = FAQAgent()
faq_content = faq_agent.run(questions, cleaned_data)
with open('faq.json', 'w') as f:
    json.dump(faq_content, f, indent=4)

product_page_agent = ProductPageAgent()
product_content = product_page_agent.run(cleaned_data)
with open('product_page.json', 'w') as f:
    json.dump(product_content, f, indent=4)

fictional_agent = FictionalProductAgent()
product_b = fictional_agent.run(None)

comparison_agent = ComparisonAgent()
comparison_content = comparison_agent.run(cleaned_data, product_b)
with open('comparison_page.json', 'w') as f:
    json.dump(comparison_content, f, indent=4)

print("Generated: faq.json, product_page.json, comparison_page.json")