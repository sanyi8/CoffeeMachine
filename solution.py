# Menu and Resources dictionary with 3 entries
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

# variable for the report
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    '''Returns TRUE when order can be made, False if ingredients are insufficient'''
    #is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False #is_enough = False
        return True #return is_enough

def process_coins():
    '''returns the calculated coins inserted'''
    print("Please insert coins.")
    # summarise coins values
    total = int(input("How many quarters?: ")) * 0.25  # here we create the total
    # now just add values to total +=
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    '''Return True if payment is accepted, False when money is insufficient'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    '''deduct selected drink ingredients from resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕︎")

is_on = True

# follow the PDF use while as we need to keep asking
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # entering “off” to the prompt.
    if choice == "off":
        print("Machine turning off")
        is_on = False #break

    # Print report.
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
        # Check resources sufficient?
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])










