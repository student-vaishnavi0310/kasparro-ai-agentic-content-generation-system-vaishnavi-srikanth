from logic_blocks import compare_ingredients, compare_prices, compare_concentrations
from templates import get_comparison_page_template

class ComparisonAgent:
    """Agent responsible for assembling comparison page."""
    def run(self, data_a, data_b):
        comparisons = {
            "ingredients": compare_ingredients(data_a, data_b),
            "prices": compare_prices(data_a, data_b),
            "concentrations": compare_concentrations(data_a, data_b)
        }
        return get_comparison_page_template(data_a, data_b, comparisons)