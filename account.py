class Account:
    def __init__(self, name):
        self.__account_name = name  # String, name of account holder
        self.__account_balance = 0.0  # Float, total amount of money stored in account

    def deposit(self, amount):
        """
        Adds money to the account balance
        :param amount: Float, money added to the account
        :return:
            False if amount <= $0
            True if the deposit is successful
        """
        increase = float(amount)
        if increase <= 0.0:
            return False
        else:
            self.__account_balance += increase
            return True

    def withdrawal(self, amount):
        """
        Removes money from the account balance
        :param amount: Float, money removed from the account
        :return:
            False if amount <= $0 or amount > account balance
            True if the withdrawal is successful
        """
        decrease = float(amount)
        if decrease > self.__account_balance or decrease <= 0:
            return False
        else:
            self.__account_balance -= decrease
            return True

    def get_balance(self):
        """
        Gets the account balance
        :return: account balance
        """
        return self.__account_balance

    def get_name(self):
        """
        Gets the name of the account holder
        :return: account nmae
        """
        return self.__account_name
