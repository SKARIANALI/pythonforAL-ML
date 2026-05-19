from abc import ABC, abstractmethod #abs module
class Car(ABC):
 def show(self):
  print("Every car has four wheels")

 @abstractmethod
 def speed(self):
  pass
class Maruti(Car):
 def speed(self):
  print("Speed is 100 km/h")
class Suzuki(Car):
 def speed(self):
  print("Speed is 70 km/h")
  
obj1 = Maruti()
obj1.show()
obj1.speed()

obj2 = Suzuki()
obj2.show()
obj2.speed()