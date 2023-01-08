import data


def resources(x):

    if x == "espresso":
        if data.menu["espresso"]["ingredients"]['water'] <= data.resources["water"]:
            if data.menu["espresso"]["ingredients"]["coffee"] <= data.resources["coffee"]:
                return x
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False

    if x == "latte":
        if data.menu["latte"]["ingredients"]["water"] <= data.resources["water"]:
            if data.menu["latte"]["ingredients"]["coffee"] <= data.resources["coffee"]:
                if data.menu["latte"]["ingredients"]["milk"] <= data.resources["milk"]:
                    return x
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False

    if x == "cappuccino":
        if data.menu["cappuccino"]["ingredients"]["water"] <= data.resources["water"]:
            if data.menu["cappuccino"]["ingredients"]["coffee"] <= data.resources["coffee"]:
                if data.menu["cappuccino"]["ingredients"]["milk"] <= data.resources["milk"]:
                    return x
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False


def coins(z):
    print("Please insert coins.")
    total_user = float(input("How many quarters?: ")) * 0.25
    total_user += float(input("How many dime?: ")) * 0.10
    total_user += float(input("How many nickel?: ")) * 0.05
    total_user += float(input("How many pennies?: ")) * 0.01
    z = round(total_user, 2)
    return z


def transaction(x, y):
    if x == "espresso":
        if data.menu["espresso"]["cost"] < y:
            change = y - data.menu["espresso"]["cost"]
            change = round(change, 2)
            print(f"Here is ${change} dollars in change.")
            print("Here is your espresso. Enjoy!")
            data.resources["water"] -= data.menu["espresso"]["ingredients"]['water']
            data.resources["coffee"] -= data.menu["espresso"]["ingredients"]['coffee']
            y = data.menu["espresso"]["cost"]
            return y
        elif data.menu["espresso"]["cost"] > y:
            print("Sorry that's not enough money. Money refunded.")
            y = 0
            return y

    if x == "latte":
        if data.menu["latte"]["cost"] < y:
            change = y - data.menu["latte"]["cost"]
            change = round(change, 2)
            print(f"Here is ${change} dollars in change.")
            print("Here is your latte. Enjoy!")
            data.resources["water"] -= data.menu["latte"]["ingredients"]['water']
            data.resources["coffee"] -= data.menu["latte"]["ingredients"]['coffee']
            data.resources["milk"] -= data.menu["latte"]["ingredients"]["milk"]
            y = data.menu["latte"]["cost"]
            return y
        elif data.menu["latte"]["cost"] > y:
            print("Sorry that's not enough money. Money refunded.")
            y = 0
            return y

    if x == "cappuccino":
        if data.menu["cappuccino"]["cost"] < y:
            change = y - data.menu["cappuccino"]["cost"]
            change = round(change, 2)
            print(f"Here is ${change} dollars in change.")
            print("Here is your cappuccino. Enjoy!")
            data.resources["water"] -= data.menu["cappuccino"]["ingredients"]['water']
            data.resources["coffee"] -= data.menu["cappuccino"]["ingredients"]['coffee']
            data.resources["milk"] -= data.menu["cappuccino"]["ingredients"]["milk"]
            y = data.menu["cappuccino"]["cost"]
            return y
        elif data.menu["cappuccino"]["cost"] > y:
            print("Sorry that's not enough money. Money refunded.")
            y = 0
            return y


def coffee_machine():
    machine_power = True
    final_status = 0
    while machine_power:
        coins_total = 0
        a = input("What would you like(espresso/latte/cappuccino): ")
        if a == "espresso" or a == "latte" or a == "cappuccino":
            if not resources(a):
                print("Not enough resources in coffee machine! ")
            else:
                machine_money = coins(coins_total)
                final_money = transaction(a, machine_money)
                final_status += final_money
        elif a == "report":
            print(f"Water: {data.resources['water']}ml\nMilk: {data.resources['milk']}ml\nCoffe: "
                  f"{data.resources['coffee']}g\nMoney: ${final_status}")
        elif a == "off":
            machine_power = False
        else:
            print("type again")


coffee_machine()
