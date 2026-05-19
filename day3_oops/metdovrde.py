class Parent:

    def show(self):
        print("Parent class")


class Child(Parent):
    def show(self): #override
        # super().show()       # access parent method
        print("Child class")


obj = Child()
obj.show()