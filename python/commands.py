Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=5
b=str(a)
b
'5'
c=float(b)
c
5.0
d=str(c)
d
'5.0'
b
'5'
e=int(b)
e
5
x='hi'
y=int(x)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    y=int(x)
ValueError: invalid literal for int() with base 10: 'hi'
y=bool(x)
y
True
x='i'
y=ord(x)
y
105
print(hi)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(hi)
NameError: name 'hi' is not defined
print('hi')
hi
print(3+8)
11
print('ans'+6)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print('ans'+6)
TypeError: can only concatenate str (not "int") to str
print('ans:'+6)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print('ans:'+6)
TypeError: can only concatenate str (not "int") to str
print(6+'ans:'_
      
SyntaxError: '(' was never closed
print(6+'ans:')
      
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(6+'ans:')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('6'+'ans:')
      
6ans:
print('ans:'+'6)'
      print('ans:'+'6')
      
SyntaxError: '(' was never closed
print('ans:' + '6')
      
ans:6

print('ans:' + '6+3')
      
ans:6+3
print('ans:', 6+3)
      
ans: 9
print("my house")
      
my house
input()
      
hi
'hi'
input()
      
9876543234567890
'9876543234567890'
p=(input)
      
5665
      
5665
>>> p=input('type something: ')
...       
type something: 3456
>>> p
...       
'3456'
>>> p=int(input('type something: '))
...       
type something: 876543
>>> p
...       
876543
>>> p=float(input('type something: '))
...       
type something: 23456
>>> p
...       
23456.0
>>> p=float(input('type something: '))
...       
type something: jhgfd
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    p=float(input('type something: '))
ValueError: could not convert string to float: 'jhgfd'
>>> 
================= RESTART: C:/WiproTraining/Python/firstprgm.py ================
Hello world !!!
>>> 
======================================================== RESTART: C:/WiproTraining/Python/calculateSum.py ========================================================
sum: 13
