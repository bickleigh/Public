 # CS50’s Introduction to Programming with Python
### Instructor: David J. Malan of Harvard University - malan@harvard.edu

 # Final Project submission - Recipe Organizer and Meal Planner

### Written in Python by Stephen Robinson sarobinson.mail@gmail.com

### Video Demo:
In this brief video, I would like to introduce a basic tool written in Python, that will help the way you experience cooking and meal planning. The Recipe Management Software is designed to simplify recipe creation, making it more enjoyable and organized than ever before.

Whether you're a seasoned chef looking to streamline your recipes or someone just beginning their cooking adventure, the software has something to offer. It's a digital cookbook, meal planner, and shopping assistant, all rolled into one.

In this README.MD document we will explore the key features and functionalities of the Recipe Organizer and discover how easy it is to create, organize, and print out favorite recipes to share with others, plan your weekly meals, and generate shopping lists.

Click the link above and dive right in to see how the Recipe Organizer can help you with your cooking experience.

### Installation:

***Prerequisites:***
It is recommended, but not required, that this program be run in an anaconda environment. Anaconda can be found here: [Anaconda download](https://www.anaconda.com/download) If you are not going to use anaconda then you must have at least Python 3.x installed. [Python download](https://www.python.org/downloads/)

From Start menu on windows open up an anaconda command prompt:
We then setup the conda environment with:


***conda create -n project python=3.10.9***


We then activate the conda environment with:


***conda activate project***


Then cd directory to project


***cd project***


We should now be in the project directory:
Download the project code from here: [Github Project](https://github.com/bickleigh/Public.git)
unzip or copy code to the project directory.

and install the requirements.txt with:


***pip install -r requirements.txt***


Run the program with:


***python project.py***



Most important of all READ this README.MD file. Along with the demo video you will have full instructions on how the program works and is structured.

# Project Introduction:
This project came about as a suggestion from my wife who after my constant complaining about her cooking suggested that I should write her a Menu planning app. She was aware I was stuck to come up with ideas for my end of course final project submission, so she suggested this would be a perfect opportunity to show case the skills I had learned from the course. So was born the Recipe Management Software.

But first a little about myself and my background. I am 67 year old Retired Telecommunications engineer specializing in High speed data networks. I live in the south of the United Kingdom
I am a certified Master CNE in Novell operating systems and a Certified Microsoft solutions developer. No32679 The only formal training in software I had was in C# that I took for my Microsoft certification. Only later in my career did I self study and learn basic Python, Java script and C++. I started out as an Electrical Engineer and gravitated toward the IT service industry taking on many roles finally ending up in Technical Program management delivering multimillion pound projects primarily in the cable industry. Projects involved the delivery of large scale broadband networks across the UK. I had to retire early due to ill health caused by stress and general burnout. After a long convalescence I decided I needed to get back on the horse and see if I still had the right stuff. I had heard of the CS50 programme from my friends and decided this would be a perfect course to take as I had a strong interest in the new AGI technologies that were being developed.

# Getting Started.
The final project instructions are fairly straight forward. Once I had solved each of the course’s problem sets, it was time to implement the final project,

*Objective:* - To design and implement a project of my own choice subject to the following requirements:

* The project must be implemented in Python.
* The project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest.
* The main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of the project.
* The 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).
* The test functions must be in a file called test_project.py, which should also be in the “root” of The project. The test functions must have the same name as the custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).
* Additional classes and functions may be implemented as you see fit beyond the minimum requirement.
* Any pip-installable libraries that the project requires must be listed, one per line, in a file called requirements.txt in the root of the project.

 ## Project Overview:
The Recipe Organizer and Meal Planner is a Python command-line application designed to help users manage their recipes, plan meals, generate shopping lists, and print and share recipes with others. It provides a user-friendly interface for interacting with recipe data, allowing users to perform various tasks related to meal planning and recipe management.

## Limitations of the project:
The `project.py` program is fairly basic in nature and does not have all the bells and whistles of a modern GUI programme that most of todays users are use to. However the software simplifies the process of creating recipes, organizing, and planning meals by providing a user-friendly interface and functionalities to make the process of organising recipes easier. The program is be well-structured and organized. However, there are a few things that will need to be considered if any further improvements are to take place.

***File Paths:***
In the load_recipe_book and save_recipe_book functions, it uses a hard coded file path ("recipe.json"). It maybe better to make this path configurable so that the user can specify where they want to store their recipe book.

***Input Validation:***
The code assumes that user inputs are valid. While there is some input validation it would make the program more stable to add more robust input validation to handle cases where users enter unexpected or incorrect data.

***Error Handling:***
While there is some error handling in place, it would make sense to consider adding more detailed error messages to provide better feedback to the user when something goes wrong.

***User Experience:***
For a more user-friendly experience, adding clearer instructions and guidance for each menu option and perhaps provide clearer prompts to users. Or perhaps a GUI interface.

***Testing:***
Ensuring that the code functions as expected by thoroughly testing different scenarios and edge cases. Because of unfamiliarity with pytest library this part of the project was quite challenging. A thorough  understanding of the available methods and functions would enable more complex and thorough  test cases.

***Data Persistence:***
The project currently saves and loads the recipe book as a JSON file. If further expansion of this application is planned, using a database would provide better data management and scalability.

## Program Structure:

The program is structured into several classes and functions, each serving a specific purpose in managing recipes and meal planning. Here we explore the key components of the program:


**1. RecipeBook Class:**	At the core of the software lies the RecipeBook class. It does most of the heavy lifting and serves as a digital cookbook. It manages recipes efficiently, enabling users to store, retrieve, and organize their recipes easily.

**2. Recipe Creation:** The software offers a straightforward recipe creation feature. Users can input recipe details, such as name, category, ingredients, and instructions. These recipes are then added to the RecipeBook.

**3. Meal Planning:** Meal planning is made very easy with the RecipeBook. Users can plan meals for specific number of days ahead, selecting recipes from their collection. This feature assists in the process of organizing weekly menus.

**4. Shopping List Generation:** To simplify grocery shopping, the software generates a shopping list based on what meals have been planned. This ensures they have all the necessary ingredients at hand.

**5. Recipe Search:** Users can search for recipes by ingredients, enabling them to make the most of the ingredients they have on hand.

**6. PDF Recipe Printing:** The software has the ability to generate printable PDF recipes. Users can create formatted recipes, perfect for sharing or keeping in a physical cookbook.

## Program Classes, Functions and Methods
**1. RecipeBook Class:**
The RecipeBook class is the core component of the program. It is responsible for managing a collection of recipes.

**Attributes:**
 - *recipes:* A list that stores instances of the *Recipe* class.

**Methods:**
 - *create_recipe:* Prompts the user to input recipe details (name, category, ingredients, instructions) and adds the new recipe to the *recipes* list.
 - *add_recipe:* Adds a preexisting *Recipe* object to the recipes list.
 - *display_all_recipes:* Displays all stored recipes, including their names, categories, and ingredients.
 - *plan_meals:* Helps users plan meals for a specified number of days, allowing them to select recipes from the collection.
 - *generate_shopping_list:* Generates a shopping list based on the selected meal plan, consolidating ingredient quantities.
 - *search_recipes_by_ingredients:* Searches for recipes that can be prepared with a given set of available ingredients.
 - *find_recipe_by_name:* Locates a recipe by its name.
 - *find_recipes_by_category:* Finds all recipes belonging to a specified category.
 - *remove_recipe:* Removes a recipe from the collection based on its name. (note: not implemented in this version)
 - *get_all_recipes:* Retrieves a list of all stored recipes.
 - *to_dict:* Converts the RecipeBook object to a dictionary for storage or serialization.
 - *from_dict:* Creates a RecipeBook object from a dictionary.

 **2. Recipe Class:**
- The Recipe class represents individual recipes, storing their name, ingredients, instructions, and category.

**Attributes:**
 - *name:* The name of the recipe.
 - *ingredients:* A list of ingredients required for the recipe.
 - *instructions:* Step-by-step cooking instructions.
 - *category:* The category to which the recipe belongs (e.g., Italian, Asian).

**Methods:**
 - *to_dict:* Converts the Recipe object to a dictionary for storage or serialization.
 - *from_dict:* Creates a Recipe object from a dictionary.

 **3. Recipe PDF Class:**

 **Methods:**

 - *header:* Sets up the pdf font and title

 - *create_recipe_pdf:* Creates a new page and aligns the page ready to accept the recipe details


**4. Main Function:**
- The *main* function is the program's entry point and orchestrates user interactions with the RecipeBook object.
- It displays a main menu and handles user input to execute various functionalities, including creating recipes, searching by ingredients, planning meals, generating shopping lists, sharing recipes, and exiting the program.
- It uses the RecipeBook class to perform these actions.

**5. Custom Functions:**
- *load_recipe_book:* Custom function that loads a recipe book from a JSON file. If the file does not exist or is invalid, it creates a new RecipeBook instance.
- *save_recipe_book:* Custom function that saves the current recipe book to a JSON file.
- *generate_recipe_pdf:* Custom function that formats the recipe and saves to a file.


## Design Decisions:

**1. Separation of Concerns:**
 - The program follows the principle of separation of concerns by organizing code into distinct classes and functions. This separation enhances code readability and maintainability.

**2. User-Friendly Interface:**
 - The program offers a user-friendly command-line interface with clear menu options and prompts. This design decision ensures that users can easily navigate and interact with the application.

**3. Data Serialization:**
 - Recipe data is serialized to and deserialized from a JSON file. This approach allows users to save their recipe collection between sessions, providing data persistence.

**4. Recipe Printing:**
 - The program includes a feature to print recipes, so they can be shared with others. Users can enter the name of a recipe they wish to print, and the program sends the the recipe details ready for printing to a PDF file.

**5. Meal Planning and Shopping List:**
 - Users can plan meals for a specified number of days, selecting recipes from their collection. The program generates a consolidated shopping list based on the selected meal plan, simplifying grocery shopping.

**6. Extensibility:**
 - The code is designed to be extensible, allowing for future enhancements such as database integration, additional search options, or user authentication.

## Functionality Highlights:

 **Recipe Creation:**
 - Users can create new recipes by providing details such as name, category, ingredients, and instructions. These recipes are added to the collection for future reference.

 **Ingredient-Based Search:**
 - Users can search for recipes based on available ingredients, helping them decide what to cook with what they have on hand.

 **Meal Planning:**
 - The program supports meal planning for a specified number of days. Users can select recipes from their collection to plan meals efficiently.

**Shopping List Generation:**
 - After planning meals, the program generates a shopping list that consolidates ingredient quantities, making grocery shopping easier.

**Recipe Printing:**
 - Users can share their favorite recipes with others by entering the recipe's name. The program displays the recipe details for sharing.

.

## Conclusion:

The Recipe Organizer and Meal Planner is a versatile Python program that simplifies recipe management, meal planning, and shopping list generation. With its user-friendly interface and well-structured code, users can efficiently manage their recipes, plan meals, and share their culinary creations with ease. The program's extensible design allows for future enhancements and customization, making it a valuable tool for cooking enthusiasts and meal planners alike.




---
# Testing

### test_project.py

The test_project.py program contains a suite of pytest test functions designed to test the functionalities of the project.py program, which is responsible for managing recipes, meal planning, and PDF generation. The test cases cover various aspects of the program, including recipe creation, searching, meal planning, data persistence, and PDF generation.

#### Program Structure

The program structure is organized as follows:

- **Test Functions:** Each test function focuses on a specific aspect of the project.py program. They are designed to verify the correctness of various methods and functionalities.
- **Fixtures:** The program defines pytest fixtures to set up common testing scenarios, such as initializing a RecipeBook instance with sample data and creating a temporary JSON file for data storage.
- **Imports:** Necessary modules and functions from the project.py program are imported for testing.

#### Test Functions

**Fixture for RecipeBook Initialization:** A fixture function initializes a RecipeBook instance with sample recipes. This fixture ensures that we have a consistent starting point for testing various functionalities.

**1. test_create_recipe(input_mock)**
- **Purpose:** This test function verifies the create_recipe method in the RecipeBook class.
- **Logic:** It mocks user input to simulate recipe creation. After calling the method, it checks if a recipe has been added to the recipe book.
- **Design Decision:** This test ensures that the recipe creation process is functioning as intended.

**2. test_find_recipe_by_name(recipe_book)**
- **Purpose:** This test function checks the find_recipe_by_name method in the RecipeBook class.
- **Logic:** It uses a RecipeBook instance with predefined recipes and searches for a specific recipe by name. It then verifies that the correct recipe is returned.
- **Design Decision:** This test confirms the accuracy of recipe retrieval by name.

**3. test_search_recipes_by_ingredients(recipe_book)**
- **Purpose:** This test function tests the search_recipes_by_ingredients method in the RecipeBook class.
- **Logic:** It uses a RecipeBook instance with predefined recipes and searches for recipes based on a set of ingredients. The test ensures that the expected matching recipes are returned.
- **Design Decision:** This test validates the accuracy of recipe search by ingredients.

**4. test_generate_shopping_list(recipe_book)**
- **Purpose:** This test function verifies the generate_shopping_list method in the RecipeBook class.
- **Logic:** It uses a RecipeBook instance with predefined recipes and planned meals. The test checks if the generated shopping list contains the correct ingredients and quantities.
- **Design Decision:** This test ensures that the shopping list generation is accurate.

**5. test_save_recipe_book(tmp_path, recipe_book_with_data)**
- **Purpose:** This test function tests the load_recipe_book and save_recipe_book functions.
- **Logic:** It creates a RecipeBook instance with predefined data, saves it to a temporary JSON file, and then loads the saved data. The test checks if the loaded recipe book matches the original one.
- **Design Decision:** This test confirms the correctness of data persistence operations.

**6. test_generate_recipe_pdf(tmp_path)**
- **Purpose:** This test function checks the generate_recipe_pdf function.
- **Logic:** It generates a PDF document using sample recipe data and checks if the PDF file is created and not empty.
- **Design Decision:** This test verifies that the PDF generation functionality is working as expected.



### Design Decisions

- The test functions are designed to be isolated and focused on specific methods or features of the RecipeBook class and the generate_recipe_pdf function.
- Mocking user input is used to simulate user interactions for recipe creation.
- The use of fixtures helps set up common testing scenarios and ensures the consistency of test data.
- The test cases cover a range of functionalities to ensure adequate testing of the project.py program.
- Assertions are used to validate the expected outcomes of each test, ensuring that the program behaves correctly.

Overall, the test_project.py program provides reasonable testing for the project.py program, helping to ensure its correctness and reliability meeting the testing requirements of the final project.

---
If you have got this far I thank you for your patience and hope you enjoy the program

Roll on CS50x :)

Stephen Robinson September the 8th 2023


