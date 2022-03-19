from menu import *

start = True
cost = 0

def enough_resources(order_resources):
    for item in order_resources:
        if order_resources[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_successful(money, cost_coffee):
    if money >= cost_coffee:
        change = round(money - cost_coffee, 2)
        print(f"Here is ${change} in change.")
        global cost
        cost += cost_coffee
        return True
    else:
        print("Sorry that's not enough money.")
        return False


def make_coffee(drink_name, order_resources):
    for item in order_resources:
        resources[item] -= order_resources[item]
    print(f"Here is your {drink_name} ☕ ")

while start:
    choice = input("What you would like? (espresso/latte/cappuccino): ")
    if choice == "off":
        start = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {cost}$")
    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





