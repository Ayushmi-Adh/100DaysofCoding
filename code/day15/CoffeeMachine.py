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


def report(resources_report):
    water = resources_report["water"]
    milk = resources_report["milk"]
    coffee = resources_report["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def ask_money():
    print("Please insert coins!!")
    quarters = float(input("How many Quarters?: "))*0.25
    dimes = float(input("How many Dimes?: "))*0.10
    nickels = float(input("How many Nickels?: "))*0.05
    pennies = float(input("How many pennies?: "))*0.01
    total = quarters + dimes + nickels + pennies
    return total


def sufficient_resources(customers_order):
    for items in customers_order:
        if customers_order[items] > resources[items]:
            print(f"Sorry!there is no sufficient {items}.")
            return False
        return True


def money_transaction(received_money, actual_cost):
    if received_money >= actual_cost:
        print(f"Here is ${round(received_money-actual_cost,2)} change. ")
        global money
        money += actual_cost
        return True
    else:
        print("Sorry! that is not enough money, Money refunded.")
        return False



def make_coffee(drink_name, customers_order):
    """Deduct the required ingredients from the resources."""
    for item in customers_order:
        resources[item] -= customers_order[item]
    print(f"Here is your {drink_name} ☕ . Enjoy!")


power_on = True
while power_on:
    ask_customer = input("What would you like to have?(Espresso/Latte/Cappuccino): ").lower()
    if ask_customer == "report":
        report(resources)
    elif ask_customer == "off":
        exit(0)
    else:
        coffee_choice = MENU[ask_customer]
        if sufficient_resources(coffee_choice["ingredients"]):
            payment = ask_money()
            if money_transaction(payment, coffee_choice["cost"]):
                make_coffee(ask_customer, coffee_choice["ingredients"])
