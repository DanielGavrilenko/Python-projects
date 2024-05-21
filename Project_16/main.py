from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
turn_on = 1
while turn_on:
    drink_name = input(f"What would you like? ({menu.get_items()}):")
    if drink_name == "report":
        coffee_machine.report()
        money.report()
    elif drink_name == "off":
        turn_on = 0
    else:
        drink = menu.find_drink(drink_name)
        if coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
