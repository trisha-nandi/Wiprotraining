
while True:
    num1=input("Enter first number:")
    num2 = input("Enter second number:")

    try:
        a=float(num1)
        b=float(num2)

        result= a/b

    except ValueError:
        print("Error: Please enter a valid mumbers\n")

    except ZeroDivisionError:
        print("Error: cannot divide by zero\n")

    else:
        print("Result:",result)
        break

    