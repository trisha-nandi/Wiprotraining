from operator import add

from MyPackage.arithmetic import subtract,multiply,divide
from MyPackage.geometry import circle_area,rectangle_area

print("Addition:", add(20,10))
print("Subtraction:", subtract(20,10))
print("Multiplication:",multiply(20,10))
print("Division:" ,divide(20,10))

print("Circle Area: ", circle_area(5))
print("Rectangle_Area: ",rectangle_area(5,7))