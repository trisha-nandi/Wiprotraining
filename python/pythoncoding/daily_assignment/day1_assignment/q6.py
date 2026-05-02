
grade = input("enter your grade(A/B/C/F):").upper()

match grade:
    case'A':
        print("Excellent")
    case 'B':
        print("Good")
    case 'C':
        print("Average")
    case 'F':
        print("Fail")
    case _:
        print("Invalit grade")