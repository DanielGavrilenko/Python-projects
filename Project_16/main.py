from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
turn_on = True
while turn_on:
    choice = input(f"What would you like? ({menu.get_items()}):")
    if choice == "report":
        coffee_machine.report()
        money.report()
    elif choice == "off":
        turn_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
