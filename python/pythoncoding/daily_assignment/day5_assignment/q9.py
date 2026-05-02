

class NegativeNumberError(Exception):
    pass
num = input("Enter a positive number:")

try:
    value= float(num)

    if value < 0:
        raise NegativeNumberError

    print("You entered:",value)
except ValueError:
    print("Error: Please enter a valid number")

except NegativeNumberError:
    print("Error:Negative numbers are not allowed")