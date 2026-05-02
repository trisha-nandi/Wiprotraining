
while True:
    user_input=input("Enter an integer:")

    try:
        num=int(user_input)
    except ValueError:
        print("Error: please enter a valid integer\n")
    else:
        print("You entered:",num)
        break
