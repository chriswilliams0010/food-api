
# # Get the dictionary of categories and dishes from the request body
# data = request.get_json()
# categories = data['categories']

# for category, dishes in categories.items():
#     for dish_name, url in dishes.items():
#         # Check if a recipe with the same dish name already exists in the database
#         recipe = Recipe.query.filter_by(dish_name=dish_name).first()

#         # If the recipe doesn't exist, create a new one
#         if recipe is None:
#             recipe = Recipe(dish_name=dish_name, category=category)
#             db.session.add(recipe)
#             db.session.commit()

#         # Create a new url for the recipe
#         url = Url(recipe_id=recipe.id, url=url)
#         db.session.add(url)
#         db.session.commit()
