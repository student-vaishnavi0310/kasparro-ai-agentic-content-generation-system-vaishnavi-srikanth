class QuestionGeneratorAgent:
    """Agent responsible for automatically generating at least 15 categorized user questions."""
    def run(self, data):
        product = data['product_name']
        questions = {
            "Informational": [
                f"What is the concentration of {product}?",
                f"What skin types is {product} suitable for?",
                f"What are the key ingredients in {product}?",
                f"What are the benefits of {product}?",
                f"Does {product} contain Vitamin C?",
                f"Does {product} contain Hyaluronic Acid?",
                f"Is {product} good for brightening skin?",
                f"Can {product} fade dark spots?",
                f"Is {product} suitable for oily skin?",
                f"Is {product} suitable for combination skin?"
            ],
            "Safety": [
                f"What are the side effects of {product}?",
                f"Is {product} suitable for sensitive skin?"
            ],
            "Usage": [
                f"How to use {product}?",
                f"When should I apply {product}?",
                f"How many drops of {product} should I use?"
            ],
            "Purchase": [
                f"What is the price of {product}?"
            ],
            "Comparison": [
                f"How does {product} compare to other serums in terms of concentration?",
                f"Is {product} better for oily skin than products for dry skin?"
            ]
        }
        return questions  # 18 questions total