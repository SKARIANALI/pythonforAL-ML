'''from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def show(self):
        pass
class square(shape):
    def show(self):
        print('4 sides')
class circle(shape):
    def show(self):
        print('circle') 
obj1=square()
obj1.show()
obj2=circle()
obj2.show()'''


'''from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def disp(self):
        pass
    
class square(shape):
    def disp(self):
        pass
        
class circle(square):
    def show(self):
        print('circle')
    def disp(self):
        print('square')
        
obj2=circle()
obj2.show()
obj2.disp()'''



from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def disp(self):
        pass
    
class square(shape):
    def disp(self):
        pass
        
class circle(square):
    def show(self):
        print('circle')
    #def disp(self):
        #print('square')
        
obj2=circle()
obj2.show()
#obj2.disp()


          