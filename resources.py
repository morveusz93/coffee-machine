from files_menagment import save_file, load_file



CAPACITY_WATER = 1000
CAPACITY_MILK = 750
CAPACITY_COFFEE = 500

class Resources():
    def __init__(self):
        self.actual_resources = load_file('resources')


    def print_resources(self):
        print(f"Water: {self.actual_resources['water']} ml")
        print(f"Milk: {self.actual_resources['milk']} ml")
        print(f"Coffee: {self.actual_resources['coffee']} g")
        print()


    def refill_resources(self):
        print("What resource You want to refill?")
        print("[1] - Water")
        print("[2] - Milk")
        print("[3] - Coffee")
        what_refill = input("Your choice: ")
        while True:
            if what_refill == '1':
                self.actual_resources["water"] = CAPACITY_WATER
            elif what_refill == '2':
                self.actual_resources["milk"] = CAPACITY_MILK
            elif what_refill == '3':
                self.actual_resources["coffee"] = CAPACITY_COFFEE
            else:
                print("Wrong choice, try again.")
                continue
            return self.new_method()

    def new_method(self):
        # SAVE FILE TO RESOURCES.TXT
        save_file(self.actual_resources)
        print()
        print("Successfully refilled!")
        print()
