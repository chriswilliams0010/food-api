# from app import db

# class Recipe(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     dish_name = db.Column(db.String(100), nullable=False)
#     category = db.Column(db.String(100), nullable=False)


# class Url(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     recipe_id = db.Column(db.Integer, db.ForeignKey(
#         'recipe.id'), nullable=False)
#     url = db.Column(db.String(200), nullable=False)


# class Ingredient(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     recipe_id = db.Column(db.Integer, db.ForeignKey(
#         'recipe.id'), nullable=False)
#     ingredient = db.Column(db.String(100), nullable=False)


# db.create_all()

# # Create a new recipe
# recipe = Recipe(dish_name='Baked salmon', category='fish')
# db.session.add(recipe)
# db.session.commit()

# # Add a URL for the recipe
# url = Url(recipe_id=recipe.id, url='https://www.example.com/baked-salmon')
# db.session.add(url)
# db.session.commit()

# # Add some ingredients for the recipe
# ingredients = [Ingredient(recipe_id=recipe.id, ingredient='Salmon'),
#                Ingredient(recipe_id=recipe.id, ingredient='Lemon'),
#                Ingredient(recipe_id=recipe.id, ingredient='Olive oil')]
# db.session.add_all(ingredients)
# db.session.commit()
