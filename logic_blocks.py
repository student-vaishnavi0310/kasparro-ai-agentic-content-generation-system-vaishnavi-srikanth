# Reusable content logic blocks: functions that apply rules to transform data into copy

def generate_benefits_block(data):
    """Transforms benefits data into readable copy."""
    return f"The benefits include {data['benefits']}."

def extract_usage_block(data):
    """Extracts and formats usage instructions."""
    return data['how_to_use']

def generate_side_effects_block(data):
    """Transforms side effects data into readable copy."""
    return f"Possible side effects: {data['side_effects']}."

def compare_ingredients(a, b):
    """Compares ingredients between two products."""
    a_ing = set(a['key_ingredients'].split(', '))
    b_ing = set(b['key_ingredients'].split(', '))
    common = ', '.join(a_ing & b_ing) if a_ing & b_ing else "None"
    unique_a = ', '.join(a_ing - b_ing) if a_ing - b_ing else "None"
    unique_b = ', '.join(b_ing - a_ing) if b_ing - a_ing else "None"
    return f"Common ingredients: {common}. Unique to {a['product_name']}: {unique_a}. Unique to {b['product_name']}: {unique_b}."

def compare_prices(a, b):
    """Compares prices between two products."""
    return f"{a['product_name']} is priced at {a['price']}, while {b['product_name']} is priced at {b['price']}."

def compare_concentrations(a, b):
    """Compares concentrations between two products."""
    return f"{a['product_name']} has {a['concentration']}, while {b['product_name']} has {b['concentration']}."

def generate_answer(question, data):
    """Rule-based dispatcher to generate answers from data based on question content."""
    q_lower = question.lower()
    if "concentration" in q_lower:
        return data['concentration']
    elif "skin type" in q_lower or ("suitable for" in q_lower and "skin" in q_lower):
        return data['skin_type']
    elif "key ingredients" in q_lower:
        return data['key_ingredients']
    elif "benefits" in q_lower:
        return data['benefits']
    elif "how to use" in q_lower:
        return data['how_to_use']
    elif "side effects" in q_lower:
        return data['side_effects']
    elif "price" in q_lower:
        return data['price']
    elif "contain vitamin c" in q_lower:
        return "Yes, it contains Vitamin C."
    elif "contain hyaluronic acid" in q_lower:
        return "Yes, it contains Hyaluronic Acid."
    elif "brightening skin" in q_lower:
        return "Yes, one of the benefits is brightening."
    elif "fade dark spots" in q_lower:
        return "Yes, it fades dark spots."
    elif "oily skin" in q_lower:
        return "Yes, it is suitable for oily skin."
    elif "combination skin" in q_lower:
        return "Yes, it is suitable for combination skin."
    elif "sensitive skin" in q_lower:
        return f"It may cause {data['side_effects'].lower()}."
    elif "when should i apply" in q_lower:
        return "In the morning before sunscreen."
    elif "how many drops" in q_lower:
        return "2–3 drops."
    else:
        return "No specific information available from the product data."