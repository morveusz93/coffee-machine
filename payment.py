

class Payment():
    def __init__(self, coffee_cost):
        self.coins = {
                "pennys" : 0.01,
                "nickels" : 0.05,
                "dimes" : 0.1,
                "quarters" : 0.25
            }
        self.thrown_money = 0
        self.coffee_cost = coffee_cost
        print("Please insert coins in machine!")
        self.thrown_coins = self.insert_coins()
        self.is_payment_succesful = self.calculate_payment()
    

    def insert_coins(self):
        self.thrown_coins = {}
        for coin in self.coins.keys():
            thrown_coin = ''
            while not thrown_coin.isnumeric():
                thrown_coin = input(f"How many {coin}? : ")
            self.thrown_coins[coin]  = (int(thrown_coin))
        print()
        return self.thrown_coins


    def calculate_payment(self):
        for coin in self.thrown_coins.keys():
            self.thrown_money += self.thrown_coins[coin] * self.coins[coin]
        if self.thrown_money < self.coffee_cost:
            print("Sorry! You didn't insert enoght money!")
            print(f"Here is ${round(self.thrown_money, 2)} in change.")
            return False
        else:
            print(f"Here is ${round(self.thrown_money - self.coffee_cost, 2)} in change.")
        return True



