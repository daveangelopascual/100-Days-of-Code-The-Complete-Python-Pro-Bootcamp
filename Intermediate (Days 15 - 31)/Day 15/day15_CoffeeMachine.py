menu = {
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
value = {
    "money": 0.00,
}

def runReport():
    print("\nCurrent State Resources")
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${value["money"]}")

def restock():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("\nResources Restocked!")
    runReport()

def cashout():
    print(f"Withdrawing ${resources["money"]} in coins.\nNew balance is $0.00")
    resources["money"] = 0

def dispenseBeverage(beverage):
    print("Dispensing beverage now...")
    print(f"Here is your {beverage}. Enjoy!\n")

QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
PENNY_VALUE = 0.01

def depositMoney(beverage):
    print(f"Beverage Cost: {beverage["cost"]}\nPlease enter coins:")
    quarters = float(input("Enter number of quarters: "))
    dimes = float(input("Enter number of dimes: "))
    nickels = float(input("Enter number of nickels: "))
    pennies = float(input("Enter number of pennies: "))
    total_change = quarters * QUARTER_VALUE + dimes * DIME_VALUE + nickels * NICKEL_VALUE + pennies * PENNY_VALUE
    
    if(beverage["cost"] > total_change):
        print("Sorry insufficient coins. Returning change...")
        return False
    elif(beverage["cost"] < total_change):
        print(f"Thank you! Returning ${total_change - beverage["cost"]}")
        return True  
    else:
        print("Thank you!")
        return True

"""Main"""
machine_on = True
options = ['espresso', 'latte', 'cappuccino', 'off', 'report', 'restock', 'cashout']
while(machine_on):
    choice = input("\nWelcome to the coffee machine!\nespresso, latte, or cappucino.\nWhat would you like to drink?: ")
    while choice not in options:
        choice = input("Invalid input!\nWhat would you like to drink?: ")
    
    if choice == 'report':
        runReport()
    elif choice == 'off':
        break
    elif choice == 'restock':
        restock()
    elif choice == 'cashout':
        cashout()
    else:
        resources_met = True
        beverage = menu[choice]
        ingredients = beverage["ingredients"]
        ingredient_list = ingredients.keys()
        for ingredient in ingredient_list:
            if resources[ingredient] < ingredients[ingredient]:
                resources_met = False
        if (resources_met):
            if depositMoney(beverage):
                value["money"] += beverage["cost"]
                for ingredient in ingredient_list:
                    resources[ingredient] -= ingredients[ingredient]
                dispenseBeverage(choice)
        else:
            print("Restock the machine! Resources Insufficient.")
        