class BankAccount(object):
    def __init__(self, deposit):
        self.amount = deposit

    def withdraw(self, amount):
        self.amount -= amount

    def deposit(self, amount):
        self.amount += amount

    def balance(self):
        return self.amount

# Let me create an instance of 'BankAccount' class with the initial
# balance as $2000.
myAccount = BankAccount(int(input("Enter the  current balance:")))
# Let me check if the balance is right.
print (myAccount.balance())
# Let me deposit my salary
myAccount.deposit(int(input("Enter the deposit amount:")))
# Let me withdraw some money to buy dinner.
myAccount.withdraw(int(input("Enter the withdraw amount:")))
# What's the balance left?
print ("The balance left In your account is: ",myAccount.balance())
