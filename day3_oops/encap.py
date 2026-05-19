class A:
    _a=10 #protected
    __b=20 #private
    def show(self):
        print('add :', self._a+self.__b)
obj=A()
obj.show()
print(obj._a)
print(A._a)
#print(obj.__b)
#print(A.__b)        

