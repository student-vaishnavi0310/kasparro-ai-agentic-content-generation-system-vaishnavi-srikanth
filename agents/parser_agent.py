class ParserAgent:
    """Agent responsible for parsing and cleaning raw product data into an internal model."""
    def run(self, raw_data):
        return {
            "product_name": raw_data.get("Product Name", ""),
            "concentration": raw_data.get("Concentration", ""),
            "skin_type": raw_data.get("Skin Type", ""),
            "key_ingredients": raw_data.get("Key Ingredients", ""),
            "benefits": raw_data.get("Benefits", ""),
            "how_to_use": raw_data.get("How to Use", ""),
            "side_effects": raw_data.get("Side Effects", ""),
            "price": raw_data.get("Price", "")
        }