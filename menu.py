from files_menagment import load_file



class MenuManager():
    def __init__(self):
        self.menu = load_file('menu')
        self.coffee_types = define_coffee_types(self.menu)

    
    def print_menu(self):
        print()
        print("What do You want to order?")
        for num in self.coffee_types.keys():
            print(f"[{num}] - {self.coffee_types[num]} - ${self.menu[self.coffee_types[num]]['cost']}")


def define_coffee_types(menu):
    coffee_types = {}
    i = 1
    for coffee_type in menu:
        coffee_types[i] = coffee_type
        i += 1
    return coffee_types

