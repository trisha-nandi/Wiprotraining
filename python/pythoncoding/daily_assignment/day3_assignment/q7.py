#Use the Math Module:
#Write a program that imports the math module and uses it to:
#Find the square root of a number.
#Calculate the sine of an angle .
#Find the greatest common divisor (GCD) of two numbers .

import math

num = float(input("Enter a number:"))
print("Square root:", math.sqrt(num))

angle = float(input("Enter angle(in radians):"))
print("Sine value:",math.sin(angle))

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
print("GCD:",math.gcd(a,b))