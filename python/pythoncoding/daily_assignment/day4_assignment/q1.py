class BankAccount:
#constructor
    def __init__(self,acc_no,name,balance):
        self.__account_number=acc_no
        self.__account_holder = name
        self.__balance=balance

#getter
    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

#setter
    def set_account_holder(self,name):
        self.__account_holder = name

    def set_balance(self,amount):
        if amount>=0:
            self.__balance=amount
        else:
            print("Invalid balance amount")

    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            print("Deposited:",amount)
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance-=amount
            print("Withdrawan:",amount)

    def display(self):
        print("Account No:",self.__account_number)
        print("Account Holder:", self.__account_holder)
        print("Balance:", self.__balance)

