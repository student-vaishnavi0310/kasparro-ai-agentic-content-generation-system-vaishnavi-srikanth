import random
from agents.base_agent import BaseAgent


class FAQAgent(BaseAgent):
    """
    Agent responsible for assembling the FAQ page
    by selecting questions and generating answers.
    """

    def run(self, task: dict):
        # Agent only responds to its assigned task
        if task.get("type") != "GENERATE_FAQ":
            return None

        questions = task.get("questions", {})
        data = task.get("product", {})

        all_questions = [
            q for category_questions in questions.values()
            for q in category_questions
        ]

        selected_questions = random.sample(
            all_questions,
            min(8, len(all_questions))
        )

        faqs = []
        for q in selected_questions:
            faqs.append({
                "question": q,
                "answer": "Please refer to the product details for accurate information."
            })

        return {
            "status": "faq_generated",
            "product_name": data.get("product_name", ""),
            "faqs": faqs
        }
