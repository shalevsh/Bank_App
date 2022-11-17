class Recipe:

    def __init__(self, recipe_dictionary):
            self.title = recipe_dictionary.get("title")
            self.thumbnail = recipe_dictionary.get("thumbnail")
            self.ingredients = recipe_dictionary.get("ingredients")
            self.href = recipe_dictionary.get("href")