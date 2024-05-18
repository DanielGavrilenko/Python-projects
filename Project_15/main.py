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
    "profit": 0
}


def do_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['profit']}")


def transaction(drink):
    coin01 = int(input("How many 0.01 coins do you want to pay?"))
    coin05 = int(input("How many 0.05 coins do you want to pay?"))
    coin10 = int(input("How many 0.10 coins do you want to pay?"))
    coin25 = int(input("How many 0.25 coins do you want to pay?"))
    sum: float = coin25 * 0.25 + coin10 * 0.1 + coin05 * 0.05 + coin01 * 0.01
    if sum >= MENU[drink]["cost"]:
        return sum
    else:
        return 0.0


def is_enough_ingredients(drink):
    for i in MENU[drink]['ingredients']:
        if resources[i] < MENU[drink]['ingredients'][i]:
            print(f"Sorry, not enough {i}")
            return 0
    return 1


def do_coffee(drink, sum):
    resources['profit'] += sum
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']


is_on = 1
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = 0
    elif choice == "report":
        do_report()
    else:
        if is_enough_ingredients(choice):
            result = transaction(choice)
            if result == 0.0:
                print("Invalid payment")
            else:
                do_coffee(choice, result)
