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

profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coin():
    """ Return the total calculate from coin inserted"""
    print("Please insert a coin.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total


def is_resourcesufficient(order_ingeridients):
    """Return true if order to be made else return false"""
    for item in order_ingeridients:
        if resources[item] < order_ingeridients[item]:
            print("Sorry, there is no enough resources of {item}")
            return False
    return True


def is_transaction_successfull(money_received, drink_cost):
    """ Return True when payment is accepted else  return false"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    """ Deduct ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is you drink {drink_name}.")


machine_state = True
while machine_state:
    user_choice = input("What would you like? (espresso/latte/cappuccino) or type 'report' or 'off' :").lower()
    if user_choice == "off":
        machine_state = False
    elif user_choice == "report":
        print("The current resource values.")
        print("Water: ", resources["water"])
        print("Milk: ", resources["milk"])
        print("Coffee: ", resources["coffee"])
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resourcesufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successfull(payment, drink["cost"]):
                make_coffe(user_choice, drink["ingredients"])

print("Thanks for Visiting!!!!")