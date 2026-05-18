# pre-defined function 
print(len('arian'))

# user-defined 

def calculator(a, b):
 print("Addition:", a + b)
 print("Subtraction:", a - b)
 print("Multiplication:", a * b)
 print("Division:", a / b)  
 
calculator(18, 4)


def greet():
 print('arian')
greet()


def greet():
 print('arian')

print(greet()) #none


def greet():
 return "Good Evening"

message = greet()
print(message)  

# Positional Arguments
def name(first,second):
    print('my name is : ',first,second)
    
name('arian','ali')

# Keyword Arguments 

def greet(first_name, last_name):
    print('my name is :',first_name,last_name)

greet(last_name="Kumar" , first_name="Ankit")


# Default Arguments

def greet(name="Guest"):
 print("Good Evening", name)
 
greet()
greet('arian')


# Variable-Length Arguments

def test(*args):
        print(args)
        print(len(args))
        print(type(args))
test()
test('arian','suman')

# keyword 

def greet(**kwargs):
    print(kwargs)
    print(type(kwargs))

greet(name="arian", age=25)
