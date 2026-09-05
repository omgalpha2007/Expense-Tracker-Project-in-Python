# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("Harry")
# print(s1.name)
# del s1.name   #delete the object propertiesor object itself

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass    #by addiing '__' we can create the object private
acc1=Account(9786969,"abcde")
print(acc1.acc_pass,acc1.acc_no)

#Single Inheritence-when one class(child) derives the properties & methods of another class(parent)
class Car:
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

#Creating multi-level inheritence
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type=type
car1=Fortuner("Petrol")
print(car1.type)
# car1.start()

#Multipple Inheritence
class A:
    varA="Welcome to Class A"
class B:
    varB="Welcome to Class B"
class C(A,B):
    varC="Welcome to class C"
c1=C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

#classmethod modification
class Person:
    name='anonymous'
    # def changename(self,name):
    #     Person.name=name

    @classmethod      #direct change the attributes of class
    def change_name(cls,name):
        cls.name=name
p1=Person()
p1.change_name("Surya Bhai")
print(p1.name)       
print(Person.name)

#property decorator
class Student:
   def __init__(self,phy,chem,math):
      self.phy=phy
      self.chem=chem
      self.math=math
      
   @property                #using property decorator for modification
   def cal_per(self):
      return str((self.phy + self.chem + self.math)/3)+"%"

stu1=Student(98,97,99)     #changing marks of one subject 
print(stu1.cal_per)

stu1.phy=78
print(stu1.cal_per)

#Operator Overloading /Polimorphism
class Complex():
   def __init__(self,real,img):
        self.real=real
        self.img=img
   def show(self):
         print(self.real,"i +",self.img,"j")
   def __add__(self,n2):       #used a Dunder function
        newReal=self.real + n2.real
        newImg=self.img + n2.img
        return Complex(newReal,newImg)
   def __sub__(self,n2):       #used a Dunder function
        newReal=self.real - n2.real
        newImg=self.img - n2.img
        return Complex(newReal,newImg)
   
n1=Complex(8,9)
print(n1.show())

n2=Complex(4,6)
print(n2.show())

n3=n1+n2
print(n3.show())

n4=n2-n1
print(n4.show())

#practise questions
#Define a cricle class to create a circle with radius r using the constructor
class Circle():
      def __init__(self,radius):
           self.radius=radius
      def area(self):
           return 3.14*self.radius**2

      def perimeter(self):
           return 2*3.14*self.radius
      
c1=Circle(21)
print(c1.area())
print(c1.perimeter())

#Define a employee class with attributes role ,department & salary
class Employee():
      def __init__(self,role,dep,sal):
          self.role=role
          self.dep=dep
          self.sal=sal

      def show(self):
          print("Role=",self.role)
          print("Department=",self.dep)
          print("Salary=",self.sal)
       

emp1=Employee("Accountant","Finance Dep","80k")
print(emp1.show())

class Engineer(Employee):
   def __init__(self,name,age):
      self.name=name
      self.age=age
      super().__init__("Engineer","IT","75k")
eng1=Engineer("Manoj Muthmare",26)
print(eng1.show())

#create a class Order which shows us product name & price
class Order:
     def __init__(self,item,price):
          self.item=item
          self.price=price
     def show_details(self):
          print(self.item,self.price)
     def __gt__(self,ord2):
          return self.price > ord2.price
     
ord1=Order("Biscuit",90)
ord2=Order("Tea",20)   
print(ord1 > ord2)   #true

