import json
import os



CAPACITY_WATER = 1000
CAPACITY_MILK = 750
CAPACITY_COFFEE = 500


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
    print("What do You want to order?")
    for num in coffee_types.keys():
        print(f"[{num}] - {coffee_types[num]}")


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
        print("Successfully reilled!")
        print()
        return


def make_coffee(coffee_type):
    """ Function takes coffee type from users_answer, then asks for pay and serves you a coffee """
    print(f"Here is your {coffee_type}! Enjoy! \n")


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
        users_choice = input()
        print()
        if users_choice in str(coffee_types.keys()):
            make_coffee(coffee_types[int(users_choice)])
        # print report of resources
        elif users_choice == 'report': 
            print_resources(resources)
        elif users_choice == 'refill':
            refill_resources(resources)
        else:
            print("Wrong task - try again.")



if __name__ == '__main__':
    main()