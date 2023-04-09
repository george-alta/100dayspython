from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def coffee():
    print("welcome to coffee machine")

    while True:
        choice = input(f"Select one of our options {menu.get_items()}")
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
            return True
        if choice == "off":
            return False

        drink = menu.find_drink(choice)
        if drink == None:
            continue
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)


while True:
    if coffee() == False:
        break
