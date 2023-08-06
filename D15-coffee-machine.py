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
money = 0


def resources_sufficient(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there's not enough {item}")
            return False
    return True


def process_coin():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies? "))
    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return total


def check_transaction(payment, drink):
    drink_price = MENU[drink]['cost']
    if payment >= drink_price:
        change = payment - drink_price
        global money
        money += drink_price
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's you {drink}☕. Enjoy!")

machine_running = True

while machine_running:

    drink = input(" What would you like? (espresso/latte/cappuccino)? ")
    if drink == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${money}")
    elif drink == 'off':
        machine_running = False
    else:
        if resources_sufficient(drink):
            payment = process_coin()
            if check_transaction(payment, drink):
                make_coffee(drink, MENU[drink]['ingredients'])
