
numbers=[10,20,30,40,50]
index = input("Enter index:")

try:
    i=int(index)

    value=numbers[i]

except ValueError:
    print("Error: Please enter valid integer index")

except IndexError:
    print("Error: Index out of range")

else:
    print("Element at index",i,"is:",value)