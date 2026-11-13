class Bank:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("invalid amount")
        else:
            self.balance += amount
            print("balance amount:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("invalid amount")
        elif amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print("withdraw amount:", amount)
            print("balance amount:", self.balance)

    def display_balance(self):
        print("current balance is:", self.balance)

    def display_details(self):
        print("name :", self.name)
        print("email:", self.email)
        print("balance:", self.balance)


holder = Bank("mrudul", "mrudul@gmail.com", 5000)
holder.display_details()
holder.deposit(2000)
holder.withdraw(1000)
holder.display_balance()