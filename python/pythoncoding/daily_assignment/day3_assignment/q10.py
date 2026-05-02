#Use the OS Module:
#Write a program that imports the os module and uses it to:
#Print the current working directory
#Create a new directory and verify its existence.
#List all files and directories in the current directory
import os

print(os.getcwd())

os.mkdir("../path")

print(os.path.exists("../Path"))

print(os.listdir())

