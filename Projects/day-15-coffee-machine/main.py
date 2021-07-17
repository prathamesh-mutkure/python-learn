from data import MENU, resources


def print_report():
    print(f"""
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}
    """)


def check_resources(coffee_name):
    ingredients = MENU[coffee_name]["ingredients"]

    check_water = ingredients["water"] <= resources["water"]
    check_coffee = ingredients["coffee"] <= resources["coffee"]
    check_milk = ingredients["milk"] <= resources["milk"]

    return check_water and check_milk and check_coffee


def buy_coffee(coffee_name, money):
    coffee = MENU[coffee_name]
    change = money - MENU[coffee_name]["cost"]

    resources["water"] -= coffee["ingredients"]["water"]
    resources["milk"] -= coffee["ingredients"]["milk"]
    resources["coffee"] -= coffee["ingredients"]["coffee"]
    resources["money"] += coffee["cost"]

    print(f"Here is ${change} in change.")
    print(f"Here is your {coffee_name} ☕️. Enjoy!")


def process_order(coffee_name):
    if check_resources(coffee_name):
        print("Please insert coins.")

        quarters = int(input("how many quarters?: ")) * 0.25
        dimes = int(input("how many dimes?: ")) * 0.1
        nickles = int(input("how many nickles?: ")) * 0.05
        pennies = int(input("how many pennies?: ")) * 0.01

        dollars = quarters + dimes + nickles + pennies

        if dollars >= MENU[coffee_name]["cost"]:
            buy_coffee(coffee_name, dollars)
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("Not sufficient resources")


is_on = True

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        print_report()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        process_order(order)
    elif order == "off":
        continue_ordering = False
    else:
        print("Bad choice, enter data again.")
