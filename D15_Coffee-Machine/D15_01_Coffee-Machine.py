LOGO = """☕☕☕☕☕"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0, # TODO, fix this workaround
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
    "water": 300, #300
    "milk": 200, #200
    "coffee": 100, #100
    "money": 0
}

def pay(cost):
    """when provided the cost of the breverage, collects coins. Returns True if paid """
    print(f"Please insert ${cost} in coins")
    paid = False
    quarters = 0
    dimes = 0
    nickles = 0
    cents = 0
    total = 0
    while not paid:
        print(f"Paid so far: {total}")
        quarters += int(input(f"how many quarters? (0.25): "))
        dimes += int(input(f"how many dimes? (0.10): "))
        nickles += int(input(f"how many nickles? (0.05): "))
        cents += int(input(f"how many cents? (0.01): "))
        total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + cents * 0.01
        # print(total)
        if total < cost:
            print(f"not enough coins. you need additional ${round(cost-total,2)}")
        elif total > cost:
            print(f"--> Paid. Change returned :${round(total-cost,2)}")
            paid = True
        else:
            print("--> Paid")
            paid = True
    return paid

def check_resources(required):
    global resources
    if (required[0]>resources["water"]) or (required[1]>resources["milk"]) or (required[2]>resources["coffee"]):
        print("not enough resources")
        return False
    else: return True

def report():
    global resources
    print(f"this is your report: {resources}")

coins = {"penny":0.01,"dime":0.1,"nickel":0.05,"quarter":0.25}

def coffee():
    global resources
    print(f"\n{LOGO}")
    print("Welcome to coffee machine")
    choice = input("What do you want today? espresso / latte / cappuccino : ").lower()
    if choice == "report": report()
    elif choice == "off": return False
    else:
        cost = MENU[choice]["cost"]
        if not check_resources([MENU[choice]["ingredients"]["water"],MENU[choice]["ingredients"]["milk"],MENU[choice]["ingredients"]["coffee"]]):
            return(f"not enough resources")
        if pay(cost):
            #make coffee
            print(f"Making your coffee now.\nenjoy your ☕☕☕☕☕ {choice.upper()} 😄😄😄")
            resources["money"] += cost
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
            resources["water"] -= MENU[choice]["ingredients"]["water"]
    return True


#check resources sufficient
#process coins. how many of each. process change
#check successful transaction
#make coffee and deduct resources
#turn off the machine if answer is off
machineon= True
while machineon:
    machineon: coffee()
print("Machine now off")