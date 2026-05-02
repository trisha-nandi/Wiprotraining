
colors = input("Enter traffic light color:").capitalize()

match colors:
    case"Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("Invalid color")