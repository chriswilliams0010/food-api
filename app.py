from flask import jsonify, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)
db.create_all()


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey(
        'recipe.id'), nullable=False)
    url = db.Column(db.String(200), nullable=False)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey(
        'recipe.id'), nullable=False)
    ingredient = db.Column(db.String(100), nullable=False)


db.create_all()

# recipe endpoints
from models import Recipe
@app.route('/recipes', methods=['GET'])
def get_recipes():
    with app.app_context():
        # Get all recipes from the database
        recipes = Recipe.query.all()

        # Convert the recipes to a list of dictionaries
        recipe_list = []
        for recipe in recipes:
            recipe_list.append(
                {'id': recipe.id, 'dish_name': recipe.dish_name, 'category': recipe.category})

        # Return the list as a JSON response
        return jsonify(recipe_list)


@app.route('/recipes', methods=['POST'])
def create_recipe():
    with app.app_context():
        # Get the dish name and category from the request body
        data = request.get_json()
        dish_name = data['dish_name']
        category = data['category']

        # Create a new recipe and add it to the database
        recipe = Recipe(dish_name=dish_name, category=category)
        db.session.add(recipe)
        db.session.commit()

        # Return the new recipe as a JSON response
        return jsonify({'id': recipe.id, 'dish_name': recipe.dish_name, 'category': recipe.category})


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    with app.app_context():
    # Get the updated dish name and category from the request body
        data = request.get_json()
        dish_name = data['dish_name']
        category = data['category']

        # Get the recipe with the specified id from the database
        recipe = Recipe.query.get(recipe_id)

        # Update the recipe with the new dish name and category
        recipe.dish_name = dish_name
        recipe.category = category
        db.session.commit()

        # Return the updated recipe as a JSON response
        return jsonify({'id': recipe.id, 'dish_name': recipe.dish_name, 'category': recipe.category})


@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    with app.app_context():
        # Get the recipe with the specified id from the database
        recipe = Recipe.query.get(recipe_id)

        # Delete the recipe from the database
        db.session.delete(recipe)
        db.session.commit()

        # Return a JSON response indicating that the recipe was deleted
        return jsonify({'message': 'Recipe deleted'})


from models import Url
@app.route('/urls', methods=['POST'])
def create_url():
    with app.app_context():
        # Get the recipe id and url from the request body
        data = request.get_json()
        recipe_id = data['recipe_id']
        url = data['url']

        # Create a new url and add it to the database
        url = Url(recipe_id=recipe_id, url=url)
        db.session.add(url)
        db.session.commit()

        # Return the new url as a JSON response
        return jsonify({'id': url.id, 'recipe_id': url.recipe_id, 'url': url.url})


@app.route('/urls/<int:url_id>', methods=['PUT'])
def update_url(url_id):
    with app.app_context():
        # Get the updated url from the request body
        data = request.get_json()
        url = data['url']

        # Get the url with the specified id from the database
        url = Url.query.get(url_id)

        # Update the url with the new url
        url.url = url
        db.session.commit()

        # Return the updated url as a JSON response
        return jsonify({'id': url.id, 'recipe_id': url.recipe_id, 'url': url.url})


@app.route('/urls/<int:url_id>', methods=['DELETE'])
def delete_url(url_id):
    with app.app_context():
        # Get the url with the specified id from the database
        url = Url.query.get(url_id)

        # Delete the url from the database
        db.session.delete(url)
        db.session.commit()

        # Return a JSON response indicating that the url was deleted
        return jsonify({'message': 'Url deleted'})


from models import Ingredient
@app.route('/ingredients', methods=['POST'])
def create_ingredient():
    with app.app_context():
        # Get the recipe id and ingredient from the request body
        data = request.get_json()
        recipe_id = data['recipe_id']
        ingredient = data['ingredient']

        # Create a new ingredient and add it to the database
        ingredient = Ingredient(recipe_id=recipe_id, ingredient=ingredient)
        db.session.add(ingredient)
        db.session.commit()

        # Return the new ingredient as a JSON response
        return jsonify({'id': ingredient.id, 'recipe_id': ingredient.recipe_id, 'ingredient': ingredient.ingredient})


@app.route('/ingredients/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id):
    with app.app_context():
        # Get the updated ingredient from the request body
        data = request.get_json()
        ingredient = data['ingredient']

        # Get the ingredient with the specified id from the database
        ingredient = Ingredient.query.get(ingredient_id)

        # Update the ingredient with the new ingredient
        ingredient.ingredient = ingredient
        db.session.commit()

        # Return the updated ingredient as a JSON response
        return jsonify({'id': ingredient.id, 'recipe_id': ingredient.recipe_id, 'ingredient': ingredient.ingredient})


@app.route('/ingredients/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id):
    with app.app_context():
        # Get the ingredient with the specified id from the database
        ingredient = Ingredient.query.get(ingredient_id)

        # Delete the ingredient from the database
        db.session.delete(ingredient)
        db.session.commit()

        # Return a JSON response indicating that the ingredient was deleted
        return jsonify({'message': 'Ingredient deleted'})


@app.route('/import-urls', methods=['POST'])
def import_urls():
    with app.app_context():
        # Get the dictionary of dish names and URLs from the request body
        data = request.get_json()
        dishes = data['dishes']

        for dish_name, url in dishes.items():
            # Check if a recipe with the same dish name already exists in the database
            recipe = Recipe.query.filter_by(dish_name=dish_name).first()

            # If the recipe doesn't exist, create a new one
            if recipe is None:
                recipe = Recipe(dish_name=dish_name)
                db.session.add(recipe)
                db.session.commit()

            # Create a new url for the recipe
            url = Url(recipe_id=recipe.id, url=url)
            db.session.add(url)
            db.session.commit()

        # Return a JSON response indicating that the URLs were imported successfully
        return jsonify({'message': 'URLs imported successfully'})


if __name__ == '__main__':
    app.run()
