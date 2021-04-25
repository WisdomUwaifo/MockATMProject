class Budget:
    def __init__(self, category, balance):
        self.category = category
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return 'account balance has been updated: $', self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient Funds'
            return 'The balance avalable', self.balance
        else:
            self.balance = self.balance - amount
            return 'Account balance has been updated', self.balance

    def transfer(self, amount):
        return self.withdraw(amount)

    def check_balance(self):
        return self.balance


category_one = Budget('food', 500)
category_two = Budget('clothing', 400)
category_three = Budget('gass', 30)
category_four = Budget('rent', 500)
category_five = Budget('unexpected expense', 200)


print(category_one.withdraw(300))
