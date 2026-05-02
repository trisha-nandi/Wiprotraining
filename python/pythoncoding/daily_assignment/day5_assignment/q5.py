num_str = input("Enter a number: ")

try:
    num= int(num_str)
    print("Integer value:", num)

except ValueError:

    print("Error: Please enter a valid numeric value")