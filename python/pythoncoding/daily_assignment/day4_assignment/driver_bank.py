from q1 import BankAccount

acc1 = BankAccount(100,"Trisha",10000)

print("\n Account Details: ")
acc1.display()
print("\n Deposit is: ")
acc1.deposit(2000)

acc1.withdraw(3000)

acc1.display()