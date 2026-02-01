def transform_meal(meal:dict):
    ingredients = []

    for i in range(1,21):
        ingredient=meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")

        if ingredient and ingredient.strip():
            ingredients.append({
                "name":ingredient,
                "measure": measure,
                "image":f"https://www.themealdb.com/images/ingredients/{ingredient.replace(" ","_")}.png"
            })
        
    return {
        "id":meal["idMeal"],
        "name":meal["strMeal"],
        "category":meal["strCategory"],
        "area": meal["strArea"],
        "instruction":meal["strInstructions"],
        "images":{
            "small": meal["strMealThumb"]+"/small",
            "medium": meal["strMealThumb"]+"/medium",
            "large": meal["strMealThumb"]+"/large"
        },
        "youtube": meal["strYoutube"],
        "ingredients": ingredients

    }