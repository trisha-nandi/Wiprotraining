
text=input("Enter some text:")
with open("Output.txt","w")as file:
    file.write(text)

with open("Output.txt", "r") as file:
    print("File Content:",file.read())



