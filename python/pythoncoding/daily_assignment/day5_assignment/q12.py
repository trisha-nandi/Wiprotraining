
def add(a,b):
    try:
        result = a+b
        print("Result:",result)

    except TypeError:
        print("Error:Both inputs must be neumeric values")

add(15,5)
add(15,"Hey")