from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
get_report = CoffeeMaker()
get_report.report()
menu=Menu()

while turned_on:
    options = menu.get_items()
