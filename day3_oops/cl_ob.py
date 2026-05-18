# 1. Basic Empty Class Definition
'''class A:
 pass

# obj = A()

# 2. Class with a Variable 
class A:
 age = 10
print(A.age)

# 3. Using a Constructor (init) 

class A:
 def __init__(self):
    age = 10
    print(age)

obj = A()

# 4. Accessing Docstrings 

class A:
 """Learn Coding"""
age=10
 
obj=A()

print(A.__doc__)
print(obj.__doc__)'''


# 5. Defining Methods and using 'self' 

class A:
    age=10
    def fun(self):
     'arian' #doc
     name = "Learn Coding"
     print(name)

obj = A()
obj.fun()
print(A.age)
print(obj.fun.__doc__)


class A:
    def fun(self,age,name,add):  # using function
        print('name:', name, 'age:', age, 'add:', add)
obj=A()
obj.fun(12,'arian','bansdroni')

class A:
    def __init__(self,age,name,add): #using constructor
        print('name:', name, 'age:', age, 'add:', add)
obj=A(12,'arian','bansdroni')
obj=A(10,'akash','spara')
obj2=A(10,20,30)
        