from templates import get_product_page_template

class ProductPageAgent:
    """Agent responsible for assembling product description page."""
    def run(self, data):
        return get_product_page_template(data)