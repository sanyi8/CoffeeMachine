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

# loop through and access to the item i need like espresso.water
def ingredients(drink):
    """will find requirements for the drink chosen"""
    if drink in MENU:
        requirements = MENU[drink]  # get the requirements directly for the required drink
        ingredient = requirements["ingredients"]   # access ingredients
        cost = requirements["cost"]     # access cost
    print(f"Ingredients for {drink}: {ingredient}\n"
          f"{drink} is: ${cost}\n")

user_choice = input("What would you like? (espresso/latte/cappuccino): ")

# TODO 1. Print a report of all the coffee machine resources
## prompt user if they write report

# TODO 2. Check resources sufficient to make drink order against recipies
if user_choice == "espresso":
    ### address the dictionary regarding user_choice check resources available_res need to be >= than required_res
    ingredients("espresso")

elif user_choice == "latte":
    ingredients("latte")
elif user_choice == "cappuccino":
    ingredients("cappuccino")


# TODO 3. Coin payment: ask for each coins: quarters, dimes, nickles and pennies
## if not enough money refund
## if enough Make calculate change based on selected drink
## + deduct the resources
pennies = int(input("How many pennies: "))
nickels = int(input("How many nickels: "))
dimes = int(input("How many dimes: "))
quarters = int(input("How many quarters: "))

