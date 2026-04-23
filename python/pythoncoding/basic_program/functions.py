#functions
'''def add(n1,n2):   #parameter
    sum = n1+n2
    return sum'''
'''
def add(n1,n2):
    return n1 + n2


def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2'''


#driver
'''num1=int(input('Enter a number'))
num2=int(input('Enter another number'))

result = add(num1,num2)     #position
print('Add : ',result)
result = sub(num1,num2)     
print('Sub : ',result)
result = mul(num1,num2)     #argument
print('Mul : ',result)'''

#ARBITARY

#def add(nums):
  #  sum = 0
 #   for n in nums:
#      sum += n
 #   return sum


#numbers=list()
#count=int(input('Howmany?'))
#for _ in range(1,count):
 #   numbers.append(int(input('No')))
  #  print(numbers)

#print(add( [6,8]))
#print(add([5,6]))
#print(add([ 5,6,8,4]))

#lambda
'''num1=int(input('Enter a number'))
num2=int(input('enter another number'))

add = lambda n1,n2 : n1+n2

print(add(num1, num2))'''


numbers = [1,2,3,4,5,6,7,8,9,10]

sq = lambda nums : [num*num     for num in nums  if num%2!=0]
print(sq(numbers))

#sq = lambda nums : [num*num     for num in nums]
#print(tuple(numbers))