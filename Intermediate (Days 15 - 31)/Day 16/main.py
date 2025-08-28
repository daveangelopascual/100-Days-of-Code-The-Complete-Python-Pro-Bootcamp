from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
drinks = Menu()
machine = CoffeeMaker()
payout = MoneyMachine()
while machine_on:
    options = drinks.get_items()
    choice = input(f"What would you like to drink? ({options[0:-1]}): ")
    match choice:
        case "off":
            machine_on = False
        case "report":
            machine.report()
            payout.report()
        case _:
            option = drinks.find_drink(choice)
            if option == "False":
                continue
            else:
                proceed = machine.is_resource_sufficient(option)
                if not proceed:
                    continue
                else:
                    price = 0
                    for item in drinks.menu:
                        if option == item.name:
                            price = item.cost
                    print(price)
                    machine.make_coffee(option)

