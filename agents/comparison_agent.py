from agents.base_agent import BaseAgent


class ComparisonAgent(BaseAgent):
    """
    Agent responsible for generating a comparison
    between the main product and a fictional competitor.
    """

    def run(self, task: dict):
        if task.get("type") != "GENERATE_COMPARISON":
            return None

        product = task.get("product", {})

        competitor = {
            "product_name": "RadiantPlus Vitamin C Serum",
            "concentration": "5%",
            "price": "₹899"
        }

        return {
            "status": "comparison_generated",
            "main_product": {
                "product_name": product.get("product_name", ""),
                "concentration": product.get("concentration", ""),
                "price": product.get("price", "")
            },
            "competitor_product": competitor,
            "summary": "GlowBoost offers higher Vitamin C concentration at a lower price."
        }
