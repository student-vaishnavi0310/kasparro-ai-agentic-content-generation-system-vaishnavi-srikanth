class FictionalProductAgent:
    """Agent responsible for generating a fictional Product B (structured, no external research)."""
    def run(self, _):  # Ignores input, as it's fictional
        return {
            "product_name": "RadiantSkin Vitamin C Serum",
            "concentration": "15% Vitamin C",
            "skin_type": "Dry, Normal",
            "key_ingredients": "Vitamin C, Aloe Vera",
            "benefits": "Hydrating, Reduces wrinkles",
            "how_to_use": "Apply 3-4 drops at night",
            "side_effects": "None reported",
            "price": "₹799"
        }