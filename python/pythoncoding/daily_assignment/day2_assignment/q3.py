#create a set of 5 unique colors
color = {"white","black","red","green","blue"}
print("original set:",color)

#Add new color to the set and remove an existing color
color.add("pink")
color.remove("black")
print("updated set:",color)

#create another set with 3 diff color.find the intersection,union and differece between both sets
color1 ={"yellow"," red","blue"}

print("intersection:" ,color & color1)
print("union:", color | color1)
print("difference:", color - color1)

#check if a specific color in the set and print the result
print("is  red in the set", "red" in color)

#convert list with duplicates to set
fruit_list=["Apple","Mango","Banana","Mango","Grapes" ,"Orange"]
unique_fruit = set(fruit_list)
print("unique_fruit:", unique_fruit)

