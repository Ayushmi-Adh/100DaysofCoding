from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


get_report = CoffeeMaker()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


turned_on = True

while turned_on:
    options = menu.get_items()
    choice = input(f"What would you like to order?({options}): ").lower()
    if choice == "off":
        turned_on = False
    elif choice == "report":
        get_report.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



