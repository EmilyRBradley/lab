class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        increase = float(amount)
        if increase <= 0.0:
            return False
        else:
            self.__account_balance += increase
            return True

    def withdrawal(self, amount):
        decrease = float(amount)
        if decrease > self.__account_balance or decrease <= 0:
            return False
        else:
            self.__account_balance -= decrease
            return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
