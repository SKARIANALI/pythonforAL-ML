class A:
    a=10 #public
    _b=20 #protected
    __c=30 #private
    print(a,_b,__c)
    
    def add(self):
        self.__c=self.a+self._b
        print('addition :',self.__c)
obj=A()
obj.add()
print(obj.a)
print(obj._b)
#print(obj.__c) #private cannot access outside the class


class A: #parent 
    a=10 #public
    _b=20 #protected
    __c=30 #private
    print(a,_b,__c)
    
    def add(self):
        self.__c=self.a+self._b
        print('addition :',self.__c)
class B(A): # child (inherit)
    def show(self):
        print(self.a)
        print(self._b)
        #print(self.__c) #private cannot access outside the class 
obj=B()
obj.add()
obj.show()
print(obj.a)
print(obj._b)
#print(obj.__c) #private cannot access outside the class 



class A: 
    a=10 #public
    _b=20 #protected
    __c=30 #private
    print(a,_b,__c)
class B: 
    def show(self):
        print(A.a)
        print(A._b) 
        #print(A.__c) #private cannot access outside the class 
obj=B()
obj.show()
