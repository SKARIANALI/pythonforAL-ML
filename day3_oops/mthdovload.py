# multiple methods with the same name but different parameters 

class A:
    #def show(self):
        #print('welcome')
    #def show(self,firstname=''):
        #print('welcome',firstname)  
    def show(self,firstname='',lastname=''): #replace first 2 lines
        print('welcome',firstname,lastname)
        
obj=A()
obj.show()
obj.show('arian')
obj.show('arian','ali')


'''Python does not support traditional method overloading like Java (same method name with different parameters).

But we can achieve it using:

default arguments
variable arguments (*args)'''

class Demo:

    def add(self, a=None, b=None, c=None):

        if a is not None and b is not None and c is not None:
            print("Sum of 3 numbers:", a + b + c)

        elif a is not None and b is not None:
            print("Sum of 2 numbers:", a + b)

        else:
            print("Invalid input")


obj = Demo()

obj.add(10, 20)
obj.add(10, 20, 30)