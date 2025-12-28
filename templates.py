# Template definitions: structured dicts with fields, rules, and formatting.
# Dependencies on logic blocks are handled in agents.

def get_faq_template(product_name, faqs):
    """FAQ Page Template."""
    return {
        "title": f"FAQ for {product_name}",
        "faqs": faqs  # List of {"question": str, "answer": str}
    }

def get_product_page_template(data):
    """Product Description Page Template."""
    description = (
        f"{data['product_name']} features {data['concentration']} and is suitable for {data['skin_type']} skin types. "
        f"Key ingredients: {data['key_ingredients']}. Benefits: {data['benefits']}."
    )
    return {
        "name": data['product_name'],
        "description": description,
        "concentration": data['concentration'],
        "skin_type": data['skin_type'],
        "key_ingredients": data['key_ingredients'],
        "benefits": data['benefits'],
        "how_to_use": data['how_to_use'],
        "side_effects": data['side_effects'],
        "price": data['price']
    }

def get_comparison_page_template(a, b, comparisons):
    """Comparison Page Template."""
    return {
        "product_a": a['product_name'],
        "product_b": b['product_name'],
        "product_a_details": a,
        "product_b_details": b,
        "comparisons": comparisons  # Dict of field: comparison_string
    }