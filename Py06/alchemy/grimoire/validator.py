
def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "air", "earth"]
    ing = ingredients.split()
    if ing and all(i in valid_ingredients for i in ing):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
