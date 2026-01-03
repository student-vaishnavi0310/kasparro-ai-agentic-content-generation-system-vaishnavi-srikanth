from agents.base_agent import BaseAgent


class ProductPageAgent(BaseAgent):
    """
    Agent responsible for generating structured
    product page content.
    """

    def run(self, task: dict):
        if task.get("type") != "GENERATE_PRODUCT_PAGE":
            return None

        product = task.get("product", {})

        return {
            "status": "product_page_generated",
            "product_name": product.get("product_name", ""),
            "concentration": product.get("concentration", ""),
            "skin_type": product.get("skin_type", ""),
            "key_ingredients": product.get("key_ingredients", ""),
            "benefits": product.get("benefits", ""),
            "how_to_use": product.get("how_to_use", ""),
            "side_effects": product.get("side_effects", ""),
            "price": product.get("price", "")
        }
