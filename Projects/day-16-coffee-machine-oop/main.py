from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    drink = input(f"What would you like? ({menu.get_items()}): ").lower()

    if drink == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        order = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    elif drink == "off":
        is_on = False
    else:
        print("Bad choice, enter data again.")
