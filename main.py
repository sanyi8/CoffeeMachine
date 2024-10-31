from idlelib.help import copy_strip

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

remake = True
print(f"MACHINE RES. START: {resources}")

# Loop through and access to the item I need like espresso water
def ingredients(drink):
    """will find requirements for the drink chosen"""
    if drink in MENU:   # menu dictionary
        require = MENU[drink]  # require is the items to make the drink from MENU
        ingredient = require["ingredients"]   # access ingredients
        cost = require["cost"]     # access cost

        # track ingredients and their required amounts with a dictionary
        required_ingredients = []

        # loop through the ingredients and prepare for checking
        for item, amount in ingredient.items():
            required_ingredients.append((item, amount))   # add item and amount to required_ingredients

        # check if resources are sufficient
        sufficient = True
        for item, amount in required_ingredients:
            print(f"RESOURCES in the machine: {resources}") # SELF CHECK
            missing_items = []
            if resources[item] < amount:
                sufficient = False     # Let User know about missing ingredient
                missing_items.append(item)
                print(f"Sorry we don't have enough {missing_items} to make Your {drink}")
                return
            elif resources[item] >= amount:
                resources[item] -= amount
                print(f"RESOURCES AFTER DRINK: {resources}") # SELF CHECK

    print(f"Ingredients for {drink}: {ingredient}\n"
          f"{drink} is: ${cost}\n"
          f"please pay with coins for {drink}")

    # coins handling AND check which can be whole number only
    def coins():
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies: "))
        user_coins = quarters * 0.25 + dimes * .1 + nickels * .05 + pennies * .01

        if user_coins >= cost:
            change = user_coins - cost
            print(f"You will get back: {change}")
            print(f"Here is your {drink}")
        elif user_coins < cost:
            print(f"Not enough money for {drink} here is your money back: {user_coins}")
            return
        else:
            print("Number required!")

    coins()

    # ask user to make another one
    remake = input(f"Would you like another coffee? Yes/No: \n").lower()
    if remake == "yes":
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        ingredients(user_choice)
    else:
        print("OK, Bye!")

user_choice = input("What would you like? (espresso/latte/cappuccino): ")

if user_choice == "espresso":
    ingredients("espresso")
elif user_choice == "latte":
    ingredients("latte")
elif user_choice == "cappuccino":
    ingredients("cappuccino")

# TODO 1. Print a report of all the coffee machine resources
## prompt user if they write report

# TODO 4. Check resources sufficient?
## a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
## b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
## c. The same should happen if another resource is depleted, e.g. milk or coffee.



# TODO 2. Check resources sufficient to make drink order against recipies
## address the dictionary regarding user_choice check resources available_res need to be >= than required_res


# TODO 3. Coin payment: ask for each coins: quarters, dimes, nickles and pennies
## if not enough money refund
## if enough Make calculate change based on selected drink
## + deduct the resources