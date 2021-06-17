import json
import os



CAPACITY_WATER = 1000
CAPACITY_MILK = 750
CAPACITY_COFFEE = 500

COINS = {
    "pennys" : 0.01,
    "nickels" : 0.05,
    "dimes" : 0.1,
    "quarters" : 0.25
}


def define_coffee_types(menu):
    coffee_types = {}
    i = 1
    for coffee_type in menu:
        coffee_types[i] = coffee_type
        i += 1
    return coffee_types


def load_file(filename):
    """ Loads data from json file and returns it as dictionary. 
    As parametr takes 'resources' or 'menu' - depends what file you want to open"""
    with open (f'{filename}.txt') as json_file:
        data_from_file = json.load(json_file)
    return data_from_file


def save_file(current_resources):
    """ Saves current resources to txt file """
    with open ("resources.txt", "w") as json_file:
        json.dump(current_resources, json_file)


def print_menu(menu, coffee_types):
    print()
    print("What do You want to order?")
    for num in coffee_types.keys():
        print(f"[{num}] - {coffee_types[num]} - ${menu[coffee_types[num]]['cost']}")


def print_resources(resources):
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print()


def refill_resources(resources):
    print("What resource You want to refill?")
    print("[1] - Water")
    print("[2] - Milk")
    print("[3] - Coffee")
    what_refill = input("Your choice: ")
    while True:
        if what_refill == '1':
            resources["water"] = CAPACITY_WATER
        elif what_refill == '2':
            resources["milk"] = CAPACITY_MILK
        elif what_refill == '3':
            resources["coffee"] = CAPACITY_COFFEE
        else:
            print("Wrong choice, try again.")
            continue
        # SAVE FILE TO RESOURCES.TXT
        save_file(resources)
        print()
        print("Successfully refilled!")
        print()
        return


def insert_coins():
    thrown_coins = {}
    for coin in COINS.keys():
        thrown_coin = ''
        while not thrown_coin.isnumeric():
            thrown_coin = input(f"How many {coin}? : ")
        thrown_coins[coin]  = (int(thrown_coin))
    print()
    return thrown_coins


def calculate_payment(coffe_cost, thrown_coins):
    thrown_money = 0
    for coin in thrown_coins.keys():
        thrown_money += thrown_coins[coin] * COINS[coin]
    if thrown_money < coffe_cost:
        print("Sorry! You didn't insert enoght money!")
        return False
    else:
        print(f"Here is ${round(thrown_money - coffe_cost, 2)} in change.")
    return True


def payment(coffee_type, MENU):
    coffee_cost = MENU[coffee_type]['cost']
    print("Please insert coins in machine!")
    thrown_coins = insert_coins()
    return calculate_payment(coffee_cost, thrown_coins)


def make_coffee(coffee_type, MENU, resources):
    """ Function takes coffee type from users_answer, then asks for pay and serves you a coffee """
    ingredients = MENU[coffee_type]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry! I don't have enought {ingredient}. Please refill!")
            return
        else: 
            resources[ingredient] -= ingredients[ingredient]
    save_file(resources)
    is_paymnet_succesfull = payment(coffee_type, MENU)
    if is_paymnet_succesfull:
        print(f"Here is your {coffee_type}! Enjoy!")
    else:
        print("Sorry, not enoght cash ;-(")


def main():
    # main variables
    MENU = load_file('menu')
    resources = load_file('resources')
    coffee_types = define_coffee_types(MENU)
    run = True
    # main loop
    os.system("cls")
    while run:
        print_menu(MENU, coffee_types)
        users_choice = input("Your choice: ")
        print()
        if users_choice in str(coffee_types.keys()):
            # call function make_coffe, as argument takes NAME of the coffee taked from coffe_types
            make_coffee(coffee_types[int(users_choice)], MENU, resources)
        # print report of resources
        elif users_choice == 'report': 
            print_resources(resources)
        elif users_choice == 'refill':
            refill_resources(resources)
        else:
            print("Wrong task - try again.")



if __name__ == '__main__':
    main()    




#TODO: 1. Add function to substract resources
