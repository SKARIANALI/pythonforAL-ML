class A:
 age=10
 def __init__(self):
    name='arian'
    print('name: ',name,'age: ',self.age)

obj = A()


class A:
 def __init__(self):
    print('arian')
def __init__(self):
    print('ankush')
obj = A()


# Default cons

class A:
    name='arian'
    age=21
    def __init__(self):
        add='hari'
        print('add :' , add , 'name : ' , self.name)
    def show(self):
     print(self.age)
    
obj=A()
obj.show()


#parametrized cons

class A:
    name='arian'
    age=21
    def __init__(self,add,roll):
        print(add,roll,self.name)
    def show(self):
     print(self.age)
    
obj=A('bram',25)
obj.show()


    