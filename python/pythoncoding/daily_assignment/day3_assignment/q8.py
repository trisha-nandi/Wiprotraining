#Use the Random Module:
#Write a program that imports the random module and uses it to:
#Generate and print a random integer between 1 and 100.
#Create a list of random numbers  and print the list.
#Shuffle a list of numbers and print the shuffled list.

import random

random_integer=random.randint(1,100)
print("Random integer between 1 and 100:",random_integer)

random_list=[]
for i in range(10):
    random_list.append(random.randint(1,100))

print("List of random numbers:", random_list)

numbers = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(numbers)

print("Shuffled list:", numbers)