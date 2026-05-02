
text=input("Enter text to append:")
with open("log.txt","a")as file:
    file.write(text +"\n")

print("\nContents of log.txt:")
with open("log.txt","r")as file:
    print(file.read())