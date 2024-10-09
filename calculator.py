def addition(x,y):
    return print("Addition is", x+y)

def subtraction(x,y):
    return print("Subtraction is", x-y)
def multiplication(x=1,y=1):
    return print("Multiplication is", x*y)

def division(x,y):
    return print("Division is", x/y)

def people(*names):
    print ("people in my class are",names)

def myfunc(x,y,z,/,*,a):
    print(x+y+z+a)




multiplication()
myfunc(1,2,4,a=22)