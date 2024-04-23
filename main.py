import random


class Customer:
    def __init__(self, name, email, customer_id):
        self._name = name
        self._email = email
        self._customer_id = customer_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def customer_id(self):
        return self._customer_id

    def get_customer_info(self):
        print("Customer Information:")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Customer ID: {self.customer_id}")
        print("-----------------------")


class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self._balance = initial_balance
        self._owner = owner
        self._account_number = self.generate_account_number()

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @property
    def account_number(self):
        return self._account_number


    def generate_account_number(self):
        return random.randint(1000000000, 9999999999)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount! Amount should be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount! Amount should be greater than 0 and less than or equal to balance.")

    def get_account_info(self):
        print("Account Information:")
        print(f"Owner: {self.owner.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")
        print("-----------------------")


customer1 = Customer("John Doe", "john.doe@example.com", "C12345")
customer1.get_customer_info()

account1 = BankAccount(customer1, 1000)
account1.get_account_info()

account1.deposit(500)
account1.withdraw(200)
account1.get_account_info()
