#Create a list with 5 different types of fruits.Print the list.

fruit_list=["Apple","Mango","Banana", "Grapes" ,"Orange"]
print(fruit_list)

#Add two fruits and remove one fruit

fruit_list.append("Papaya")
fruit_list.append("Lemon")
fruit_list.remove("Banana")
print("Updated list : ",fruit_list)

#acces the second and fourth fruits in the list.print them

print("second fruit:",fruit_list[1])
print("Fourth fruit:",fruit_list[3])

#slice first three fruits
print("First three fruits:",fruit_list[0:3])

#Find length of list
print(len(fruit_list))