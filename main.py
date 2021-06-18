import json
import os
from files_menagment import save_file, load_file
from resources import Resources
from menu import MenuManager
from payment import Payment



def make_coffee(coffee_type, menu, resources):
    """ Function takes coffee type from users_answer, then asks for pay and serves you a coffee """
    ingredients = menu[coffee_type]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry! I don't have enought {ingredient}. Please refill!")
            return
        else: 
            save_file(resources)
            coffee_cost = menu[coffee_type]['cost']
            actual_payment = Payment(coffee_cost)
            if actual_payment.is_payment_succesful:
                print(f"Here is your {coffee_type}! Enjoy!")
                resources[ingredient] -= ingredients[ingredient]
            return



def main():
    # main variables
    resources_manager = Resources()
    resources = resources_manager.actual_resources
    menu_manager = MenuManager()
    menu = menu_manager.menu
    run = True
    # main loop
    os.system("cls")
    while run:
        menu_manager.print_menu()
        users_choice = input("Your choice: ")
        print()
        if users_choice in str(menu_manager.coffee_types.keys()):
            # call function make_coffe, as argument takes NAME of the coffee taked from coffe_types
            make_coffee(menu_manager.coffee_types[int(users_choice)], menu, resources)
        # print report of resources
        elif users_choice == 'report': 
            resources_manager.print_resources()
        elif users_choice == 'refill':
            resources_manager.refill_resources()
        elif users_choice == 'off' or users_choice == 'quit':
            print("Have a nice day!")
            run = False
        else:
            print("Wrong task - try again.")



if __name__ == '__main__':
    main()    
