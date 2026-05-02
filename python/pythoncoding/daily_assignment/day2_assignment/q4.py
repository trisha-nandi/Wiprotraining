#create a dictonary with your name,age and fav hobby as keys and provide appropiate values
person = {
    "name": "Trisha",
    "age": "23",
    "hobby": "photography"
}
print("original dict:",person)

#access and print the value associte with your name
print("Name:",person["name"])

#add fav food and hobby and update it
person["fav_food"]="momo"
person["hobby"]="listening music"
print("updated dict:",person)

#print all keys and all the values
print("keys:",person.keys())
print("values:",person.values())

#remove age key
person.pop("age")
print("dict after removing age:",person)
