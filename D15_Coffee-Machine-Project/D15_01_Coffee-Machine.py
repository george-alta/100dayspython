LOGO = """☕☕☕☕☕"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            # "milk": 0,  # TODO, fix this workaround
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
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}  # 300  # 200  # 100


def pay(cost):
    """when provided the cost of the breverage, collects coins. Returns True if paid"""
    print(f"Please insert ${cost} in coins")
    paid = False
    total = 0
    while not paid:
        print(f"Paid so far: {round(total,2)}")
        total += int(input(f"how many quarters? (0.25): ")) * 0.25
        total += int(input(f"how many dimes? (0.10): ")) * 0.1
        total += int(input(f"how many nickles? (0.05): ")) * 0.05
        total += int(input(f"how many cents? (0.01): ")) * 0.01
        if total < cost:
            print(f"not enough coins. you need additional ${round(cost-total,2)}")
        elif total > cost:
            print(f"--> Paid. Change returned :${round(total-cost,2)}")
            paid = True
        else:
            print("--> Paid")
            paid = True
    return paid


def check_resources(choice):
    """input is the coffee of choice,
    and it will return if ther are enough ingredients to make it"""
    global resources
    for item in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][item] > resources[item]:
            print(f"Sorry. There is not enough {item}")
            return False
    else:
        return True


def report():
    global resources
    print(f"this is your report: {resources}")


coins = {"penny": 0.01, "dime": 0.1, "nickel": 0.05, "quarter": 0.25}


def coffee():
    global resources
    print(f"\n{LOGO}")
    print("Welcome to coffee machine")
    choice = input("What do you want today? espresso / latte / cappuccino : ").lower()
    if choice == "report":
        report()
    elif choice == "off":
        return False
    else:
        cost = MENU[choice]["cost"]
        if not check_resources(choice):
            return f"not enough resources"
        if pay(cost):
            # make coffee
            print(
                f"Making your coffee now....\n      ☕☕☕Here is your {choice.upper()}☕☕☕ Enjoy!  😄😄😄"
            )
            resources["money"] += cost
            for item in MENU[choice]["ingredients"]:
                resources[item] -= MENU[choice]["ingredients"][item]
    return True


machineon = True
while machineon:
    machineon = coffee()
print("Machine now off")
