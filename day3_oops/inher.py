'''class A:
    age=10
    def __init__(self):
        pass
    def show(self):
        address='hari'
        print('add :',address,'age:',self.age)
class B(A):
    def disp(self):
        reg_no=1234
        print(reg_no)
obj=B()
obj.disp()
obj.show()'''

# Simple 
'''class A:
    def __init__(self):
     self.num1 = int(input("Enter first number: "))
     self.num2 = int(input("Enter second number: "))

    def add(self):
     print("Addition:", self.num1 + self.num2)

    def sub(self):
     print("Subtraction:", self.num1 - self.num2)

class B(A):
     def mul(self):
      print("Multiplication:", self.num1 * self.num2)

     def div(self):
      print("Division:", self.num1 / self.num2)

     def rem(self):
      print("Remainder:", self.num1 % self.num2)
   
obj=B()
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.rem()'''

# Multilevel(1 parent-mul child)

'''class A:
    def __init__(self):
     self.num1 = int(input("Enter first number: "))
     self.num2 = int(input("Enter second number: "))

    def add(self):
     print("Addition:", self.num1 + self.num2)

    def sub(self):
     print("Subtraction:", self.num1 - self.num2)

class B(A):
     def mul(self):
      print("Multiplication:", self.num1 * self.num2)

     def div(self):
      print("Division:", self.num1 / self.num2)

class C(B):
     def rem(self):
      print("Remainder:", self.num1 % self.num2)
  
obj=C()
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.rem()'''


# Multiple ( mul parent - 1 child )

'''class Akhilesh:
  back = "Oracle Database and Java"
  def back_end(self):
   print("Back end task implemented using",self.back)

class Ankush:
  def front_end(self):
   front = "HTML, CSS, JavaScript"
   print("Front end task implemented by using",front)

class TeamLead(Akhilesh, Ankush):
  def show(self):
   print("Dynamic website created successfully")

t = TeamLead()
t.back_end()
t.front_end()
t.show()'''

# Hierarchical

class Father:
  surname = "Kushwaha"

  def show(self):
    print("My surname is", self.surname)

class Sun1(Father):
 def disp(self):
  print("My name is Ankit", self.surname)

class Sun2(Father):
 def out(self):
  print("My name is Ankush", self.surname)


s1 = Sun1()
s2 = Sun2()
s1.disp()
s1.show()
s2.out()
s2.show()