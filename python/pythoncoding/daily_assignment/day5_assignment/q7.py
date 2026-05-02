num1 = input("Enter first number:")
num2 = input("Enter second number:")

try:
    a=float(num1)
    b=float(num2)
    result = a / b

except ValueError:
    print("Error: Please enter valid numeric values")

except ZeroDivisionError:
    print("Error: cannot divide by zero")

else:
    print("Result:",result)