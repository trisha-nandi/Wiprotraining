#Write a user-defined function "find_largest(a, b, c)" that takes three numbers as
#arguments and returns the largest of the three. Use the function in a program to find and
#print the largest of three given numbers.
def find_largest(a,b,c):
    if a>= b and a>=c:
        return a
    elif b>= a and b>=c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = find_largest(a,b,c)
print("Largest number is:", largest)