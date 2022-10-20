# imports
import time

# have a dictionary of ingredients and their associated meals
breakfast_ingredients = ("oats", "yogurt", "seeds")
lunch_ingredients = ("tofu", "pepper", "potatoes", "lentils")
snacks_ingredients = ("flour")
#meals (find a way of storing these)
breakfast_meals = {'porridge':['oats','yogurt', 'seeds'], 'pancakes':['flour','sugar']}
lunch_meals = {'lentil dhaal':['lentils', 'coconut milk', 'onion'], \
    'stir fry':['tofu', 'pepper', 'onion', 'soy sauce']}
snacks_meals = {'cookies':['flour', 'sugar', 'chocolate chips']}

def mainMenu():
    # ask for user input on the meal
    print("Please, select a type of meal by entering the number: \
        \n 1 - breakfast \
        \n 2 - lunch/dinner \
        \n 3 - snacks/others \
        \n 4 - I don't need to choose. Exit application.")

    # initialise empty value for the meal
    meal = 0
    # get input number
    control = True
    while control:
        choice = int(input("Your choice: "))
        meal = choice
        if choice == 1 or choice == 2 or choice == 3:
            control = False
            time.sleep(0.3)
            askIngredients(choice)
        elif choice == 4:
            control = False
            print("Exiting application.")
        else:
            print("Error selecting an available choice. Please, try again.")
            control = True


def askIngredients(choice):
    # ask for user input on ingredients
    print("Please, enter the name of the ingredients you have separated by a comma, \
selecting from the list.")
    time.sleep(0.5)
    if choice == 1:
        print(f"List of ingredients:  {breakfast_ingredients}")
    elif choice == 2:
        print(f"List of ingredients:  {lunch_ingredients}")
    else:
        print(f"List of ingredients:  {snacks_ingredients}")
    user_ingredients = input()
    user_ingredients = user_ingredients.split(", ")
    # iterate through the user ingredients, and alert of the ones that 
    # are not recognised
    findMeals(choice, user_ingredients)

def iterateMeals(meal_repo, ingredients_available):
    mealsFound = []
    for meal, ingredients in meal_repo.items():
        allIngredientsPresent = True
        while allIngredientsPresent:
            for ingredient_available in ingredients_available:
                print(ingredient_available)
                # search for it
                for ingredient in ingredients:
                    print(ingredient)
                    if ingredient == ingredient_available:
                        #allIngredientsPresent = True
                        print("found")
                        break
                    allIngredientsPresent = False
            break
        if allIngredientsPresent:
            mealsFound.append(meal)
    return mealsFound

def findMeals(choice, ingredients):
    time.sleep(0.8)
    if choice == 1:
        # iterate through meals
        mealsFound = iterateMeals(breakfast_meals, ingredients)
    elif choice == 2:
        # iterate through meals
        mealsFound = iterateMeals(lunch_meals, ingredients)
    else:
        # iterate through meals
        mealsFound = iterateMeals(snacks_meals, ingredients)
    output(mealsFound)

def output(mealsFound):
    time.sleep(0.8)
    if len(mealsFound) == 0:
        print("Sorry, no meals have been found with the \
ingredients you input. You can try again.")
    else:
        print("These are the meals you can make: ")
        print(mealsFound)
    time.sleep(1.2)
    print("Going back to main menu.")
    time.sleep(3.5)
    mainMenu()

# start the application
print("This is a tool to help you choose something \
to eat based on what you have on your fridge :)")
mainMenu()



