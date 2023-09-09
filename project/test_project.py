import pytest
import os
from fpdf import FPDF
from unittest.mock import patch
from project import RecipeBook, Recipe, load_recipe_book, save_recipe_book, generate_recipe_pdf


                                                                                    # Create a fixture to initialize a RecipeBook instance for testing
@pytest.fixture
def recipe_book():
    book = RecipeBook()
    recipe1 = Recipe("Beans on Toast", ["Bread", "Beans"], "Heat beans in a pan, Toast bread, place on a plate and pour over the beans", "Comfort")
    recipe2 = Recipe("Bread and Jam", ["Bread", "Jam"], "Butter bread and spread jam", "Comfort")
    recipe3 = Recipe("Hot Chocolate", ["Hot Chocolate", "Cream"], "Heat chocolate in a pan, add cream and serve", "Comfort")
    book.recipes = [recipe1, recipe2, recipe3]
    return book

@patch("builtins.input", side_effect=["Recipe Name", "Ingredient1,Ingredient2", "Instructions", "Category"])
def test_create_recipe(input_mock):
    recipe_book = RecipeBook()
    recipe_book.create_recipe()
    assert len(recipe_book.recipes) == 1

def test_find_recipe_by_name(recipe_book):
    recipe = recipe_book.find_recipe_by_name("Beans on Toast")
    assert recipe is not None
    assert recipe.name == "Beans on Toast"

def test_search_recipes_by_ingredients(recipe_book):
    ingredients = ["Bread", "Jam"]
    matching_recipes = recipe_book.search_recipes_by_ingredients(ingredients)
    assert len(matching_recipes) == 1

def test_generate_shopping_list(recipe_book):
    planned_meals = {
        "Day 1": recipe_book.recipes[0],
        "Day 2": recipe_book.recipes[1]
    }
    shopping_list = recipe_book.generate_shopping_list(planned_meals)
    assert shopping_list["Beans"] == 1
    assert shopping_list["Bread"] == 2
    assert shopping_list["Jam"] == 1

@pytest.fixture
def recipe_book_with_data(tmp_path):                                                    # Create a temporary directory and a recipe book with data

    recipe_book = RecipeBook()
    recipe1 = Recipe("Recipe1", ["ingredient1", "ingredient2"], "Instructions for Recipe1", "Category1")
    recipe2 = Recipe("Recipe2", ["ingredient2", "ingredient3"], "Instructions for Recipe2", "Category2")
    recipe3 = Recipe("Recipe3", ["ingredient3", "ingredient4"], "Instructions for Recipe3", "Category1")
    recipe_book.recipes = [recipe1, recipe2, recipe3]

                                                                                        # Save the recipe book to a temporary JSON file
    temp_json_file = tmp_path / "temp_recipe_book.json"
    save_recipe_book(recipe_book)                                                       # Pass the file path as a string
    return temp_json_file

@pytest.mark.usefixtures("recipe_book_with_data")
def test_save_recipe_book(tmp_path, recipe_book_with_data):
                                                                                        # Create a recipe book with data
    recipe_book = load_recipe_book()                                                    # Load the saved recipe book

                                                                                        # Create additional recipes
    recipe1 = Recipe("Recipe1", ["ingredient1", "ingredient2"], "Instructions for Recipe1", "Category1")
    recipe2 = Recipe("Recipe2", ["ingredient2", "ingredient3"], "Instructions for Recipe2", "Category2")
    recipe3 = Recipe("Recipe3", ["ingredient3", "ingredient4"], "Instructions for Recipe3", "Category1")

                                                                                        # Check if the loaded recipe book matches the one we created
    loaded_recipes = recipe_book.get_all_recipes()
    expected_recipes = [recipe1, recipe2, recipe3]

    assert len(loaded_recipes) == len(expected_recipes)

    for i, loaded_recipe in enumerate(loaded_recipes):
        expected_recipe = expected_recipes[i]
        assert loaded_recipe.name == expected_recipe.name
        assert loaded_recipe.ingredients == expected_recipe.ingredients
        assert loaded_recipe.instructions == expected_recipe.instructions
        assert loaded_recipe.category == expected_recipe.category

def test_generate_recipe_pdf(tmp_path):
                                                                                        # Test data
    recipe_title = "Spaghetti Carbonara"
    recipe_content = """
    Ingredients:
    - Spaghetti
    - Eggs
    - Bacon
    - Cheese

    Instructions:
    1. Cook spaghetti.
    2. Fry bacon.
    3. Mix with eggs and cheese.
    4. Enjoy!
    """

    pdf_file_name = str(tmp_path / "test_recipe.pdf")

                                                                                        # Generate the PDF
    generate_recipe_pdf(recipe_title, recipe_content, pdf_file_name)

                                                                                        # Check if the PDF file was created
    assert os.path.exists(pdf_file_name)

                                                                                        # Check the PDF file is not empty
    assert os.path.getsize(pdf_file_name) > 0