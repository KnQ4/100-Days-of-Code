from menu import *
money = 0

def check_resources(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"There is not enough resources for this {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}. Thank you!")
        global money
        money += drink_cost
        return True
    else:
        print("You do not have enough for the order. Here is your money back.")
        return False


def coffee_maker(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


machine_on = True

while machine_on:
    user_choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "status":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[user_choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                coffee_maker(user_choice, drink["ingredients"])

