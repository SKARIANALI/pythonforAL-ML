class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Creating objects
d = Dog()
c = Cat()

# Same method name, different behavior
d.sound()
c.sound()

#This is called runtime polymorphism or method overriding in OOP.


print(len('ankush')) # string
print(len(['ankush'])) # list