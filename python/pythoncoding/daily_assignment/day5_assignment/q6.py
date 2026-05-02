filename=input("Enter file name:")

try:
    with open(filename,"r")as file:
        content = file.read()
        print("\nFile contents:")
        print(content)

except FileNotFoundError:
    print("Eroor: File not found")