import random
from logic_blocks import generate_answer
from templates import get_faq_template

class FAQAgent:
    """Agent responsible for assembling FAQ page: selects questions and generates answers."""
    def run(self, questions, data):
        # Select at least 5 questions (e.g., random selection for variety, min 5)
        all_questions = [q for cat_qs in questions.values() for q in cat_qs]
        selected = random.sample(all_questions, min(8, len(all_questions)))  # More than min 5
        faqs = [{"question": q, "answer": generate_answer(q, data)} for q in selected]
        return get_faq_template(data['product_name'], faqs)