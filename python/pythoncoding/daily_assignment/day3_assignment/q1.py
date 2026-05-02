#Take a list of numbers as input and print the largest and smallest numbers in the list.
n=[12,45,76,9,85]
print(f"Max:{max(n)}; Min:{min(n)}")

#Take a string as input and print the length of the string.
s=input("Enter a string: ")
print("Length if string: ",len(s))

#Take a list of names as input and print the list in alphabetical order.
names=input("Enter names(space seperated): ").split()
print("Names in alphabetical order:",sorted(names))

#Take a list of numbers as input and print the total sum of the elements in the list.
n1=list(map(int, input("enter numbers for sum:").split()))
print("Total sum: ",sum(n1))

#Takes a string as input and print the string in uppercase.
s2=input("Enter a string: ")
print("Uppercase string:",s2.upper())