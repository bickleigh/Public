"""
CS50 Introduction to Programming with Python
Module 9, Et Cetera
Final Project.

Objective: - To design and implement a project of my own choice subject to the following requirements:

* The project must be implemented in Python.
* The project must have a main function and three or more additional functions.
  At least three of those additional functions must be accompanied by tests that can be executed with pytest.
* The main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of the project.
* The 3 required custom functions other than main must also be in project.py and defined at the same
  indentation level as main (i.e., not nested under any classes or functions).
* The test functions must be in a file called test_project.py, which should also be in the “root” of The project.
  Be sure they have the same name as the custom functions, prepended with test_ (test_custom_function, for example,
  where custom_function is a function you've implemented in project.py).
* Additional classes and functions may be impimented as you see fit beyond the minimum requirement.
* Any pip-installable libraries that the project requires must be listed, one per line,
  in a file called requirements.txt in the root of the project.

For further details on project structure and how each element works see the README.MD file

"""


from fpdf import FPDF                                                               # Import project libararies
import json
import os




class RecipeBook:                                                                   # Define RecipeBook class to manage recipes
    def __init__(self):
        self.recipes = []

    def create_recipe(self):                                                        # Input recipe details and add the new recipe to self.recipes
        recipe_name = input("Enter the name of the recipe: ")
        category = input("Enter the category of the recipe: ")
        ingredients = input("Enter the ingredients (comma-separated): ").split(',')
        instructions = input("Enter the instructions: ")

        recipe = Recipe(recipe_name.strip(), [ingredient.strip() for ingredient in ingredients], instructions.strip(), category.strip())    # Create a Recipe object with the provided details

        self.recipes.append(recipe)                                                 # Add a new recipe to the list of recipes

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def display_all_recipes(self):                                                  # Define method to get all recipes
        print("\nAvailable Recipes:")
        for index, recipe in enumerate(self.recipes, start=1):
            print(f"{index}. {recipe}")

    def plan_meals(self, days_to_plan):                                             # Define meal plan function
        planned_meals = {}

        for day in range(1, days_to_plan + 1):
            print(f"Plan a meal for Day {day}:")


            self.display_all_recipes()                                              # Display available recipes


            recipe_index = int(input("Enter the index of the recipe to add (0 to skip): ")) # Ask the user to select a recipe by index number

            if recipe_index == 0:
                print(f"Day {day} is skipped.")
                continue

            if recipe_index < 1 or recipe_index > len(self.recipes):                 # Check user has selected a valid recipe
                print("\nInvalid recipe index. Please select a valid recipe.")
                continue

            selected_recipe = self.recipes[recipe_index - 1]
            planned_meals[f"Day {day}"] = selected_recipe                            # Add the selected recipe to the planned meals

        return planned_meals                                                         # Return planned_meals list

    def generate_shopping_list(self, planned_meals):                                 # Define function to create shopping list
        shopping_list = {}

        for day, recipe in planned_meals.items():
            for ingredient in recipe.ingredients:
                if ingredient not in shopping_list:
                    shopping_list[ingredient] = 1
                else:
                    shopping_list[ingredient] += 1

        return shopping_list

    def search_recipes_by_ingredients(self, available_ingredients):                  # Define function to search by ingrediant
        matching_recipes = []

        for recipe in self.recipes:
            if all(ingredient in recipe.ingredients for ingredient in available_ingredients):
                matching_recipes.append(recipe)

        return matching_recipes

    def find_recipe_by_name(self, name):                                             # define function to find and return a recipe by its name

        for recipe in self.recipes:
            if recipe.name == name:
                return recipe
        return None

    def find_recipes_by_category(self, category):                                    # Define a function to find and return a list of recipes in a specific category

        matching_recipes = [recipe for recipe in self.recipes if recipe.category == category]
        return matching_recipes

    def remove_recipe(self, name):                                                   # Define function to remove a recipe by its name (Note: function not used in this implementaion)
        recipe_to_remove = self.find_recipe_by_name(name)
        if recipe_to_remove:
            self.recipes.remove(recipe_to_remove)

    def add_recipe(self, recipe):                                                    # Add a new recipe to the list of recipes
        self.recipes.append(recipe)

    def get_all_recipes(self):                                                       # Method to return a list of all recipes
        return self.recipes

    def to_dict(self):                                                               # Convert the RecipeBook object to a dictionary for storage or serialization
        recipe_book_dict = {
            "recipes": [recipe.to_dict() for recipe in self.recipes]
        }
        return recipe_book_dict

    @classmethod
    def from_dict(cls, recipe_book_dict):                                            # Define a class method to create a RecipeBook object from a dictionary

        recipe_book = cls()
        for recipe_dict in recipe_book_dict.get("recipes", []):
            recipe = Recipe.from_dict(recipe_dict)
            recipe_book.add_recipe(recipe)
        return recipe_book


class Recipe:                                                                        # Define a class called recipe. This used to create a recipe instance of recipe
    def __init__(self, name, ingredients, instructions, category):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category

    def __str__(self):
        return f"Recipe: {self.name}\nCategory: {self.category}\nIngredients: {', '.join(self.ingredients)}"

    def to_dict(self):                                                               # Method to convert the Recipe object to a dictionary for storage or serialization

        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "category": self.category
        }

    @classmethod                                                                     # Class method to create a Recipe object from a dictionary
    def from_dict(cls, recipe_dict):

        return cls(
            recipe_dict["name"],
            recipe_dict["ingredients"],
            recipe_dict["instructions"],
            recipe_dict["category"]
        )


class RecipePDF(FPDF):                                                               # Define a FPDF class so we can print recipes to  a PDF file
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.cell(0, 30, "Recipe or Meal Plan PDF", align="C")

    def create_recipe_pdf(self, title, content):
        self.add_page()

        self.set_font("helvetica", "B", 20)
        self.set_text_color(0, 0, 0)
        self.set_xy(10, self.get_y() + 30)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT", align="C")
        self.multi_cell(0, 10, content, align="L")

def generate_recipe_pdf(title, content, pdf_file_name):                             # Custom function to generate recipe pdf and output to file
    pdf = RecipePDF()
    pdf.create_recipe_pdf(title, content)
    pdf.output(pdf_file_name)

def load_recipe_book(file_path="recipe.json"):                                      # Custom function to load recipe book from json file
    try:
        with open(file_path, "r") as file:
            recipe_book_data = json.load(file)
            return RecipeBook.from_dict(recipe_book_data)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        new_recipe_book = RecipeBook()
        save_recipe_book(new_recipe_book)
        return new_recipe_book

def save_recipe_book(recipe_book, file_path="recipe.json"):                         # Custom function to save the new recipe book with the provided file path
    with open(file_path, "w") as file:
        recipe_book_data = recipe_book.to_dict()
        json.dump(recipe_book_data, file, indent=4)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")                                # Custom function to clear screen prior to printing menu.

def main():

    recipe_book = RecipeBook()                                                      # Create new recipe book fromn RecipeBook() class
    recipe_book = load_recipe_book()                                                # Load the recipe book from a JSON file (if available)
    planned_meals = {}                                                              # Initialize planned_meals dict

    clear_screen()
    print("Welcome to the Recipe Organizer and Meal Planner!")                      # Display a welcome message and menu options
    while True:
        print("\nMain Menu:")
        print("1. Create a new recipe")
        print("2. Search for recipes by ingredients")
        print("3. Plan meals for the week")
        print("4. Generate a shopping list")
        print("5. Print a recipe to share with others")
        print("6. Exit")

        choice = input("Please select an option (1-6): ")

        if choice == "1":                                                            # Create a new recipe
            recipe_book.create_recipe()

        elif choice == "2":                                                           # Search for recipes by ingredients
            available_ingredients = input("\nEnter available ingredients (comma-separated): ").split(',') # Get available ingredients from the user
            matching_recipes = recipe_book.search_recipes_by_ingredients([ingredient.strip() for ingredient in available_ingredients]) # Call search_recipes_by_ingredients() to find matching recipes
            if matching_recipes:
                print("\nMatching Recipes:")                                         # Print the matching recipes
                for recipe in matching_recipes:
                    print(recipe.name)
            else:
                print("\nNo matching recipes found.")

        elif choice == "3":                                                          # Plan meals for the week. It's a good idea to do this first before you creat shopping list. ;)
            days_to_plan = int(input("\nEnter the number of days to plan meals for: "))
            planned_meals = recipe_book.plan_meals(days_to_plan)
            print("\nPlanned Meals:")
            for day, recipe in planned_meals.items():
                print(f"{day}: {recipe}")

        elif choice == "4":                                                          # Generate a shopping list
            if not planned_meals:
                print("\nPlease plan meals (Option 3) before generating a shopping list.")
            else:
                shopping_list = recipe_book.generate_shopping_list(planned_meals)
                print("\nShopping List:")
                for ingredient, quantity in shopping_list.items():
                    print(f"{ingredient}: {quantity}")

        elif choice == "5":                                                          # Print a recipe to share with others

            recipe_name_to_print = input("Enter the name of the recipe to print to PDF: ") # Ask the user for the name of the recipe to print

            recipe_to_print = recipe_book.find_recipe_by_name(recipe_name_to_print)   # Find the recipe by name
            if recipe_to_print:                                                       # Populate recipe_title and recipe_content
                recipe_title = recipe_to_print.name
                recipe_ingredients = "\n".join(recipe_to_print.ingredients)
                recipe_instructions = recipe_to_print.instructions
                recipe_content = f"""Ingredients:\n{recipe_ingredients}\n\nInstructions:\n{recipe_instructions}"""
                pdf_file_name = f"{recipe_name_to_print}.pdf"

                generate_recipe_pdf(recipe_title, recipe_content, pdf_file_name)      # Generate PDF and save

                print(f"\nPDF saved as {pdf_file_name}")
            else:
                print(f"\nNo recipe with the name '{recipe_name_to_print}' found.")

        elif choice == "6":                                                           # Call save_recipe_book() and Exit
            save_recipe_book(recipe_book)
            print("\nThank you for using the Recipe Organizer and Meal Planner. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

