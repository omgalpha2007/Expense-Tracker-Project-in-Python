#OOPs in Python 
#making a class
# class Student:
#     name="David Gogggins"

# #creating object
# s1=Student()
# print(s1.name)

# class Car:
#     color="Blue"
#     brand="Mercedes"
# car1=Car()
# print(car1.color)
# print(car1.brand)

#__init__ function
# class Student:
#     def __init__(self,name,marks):
#             self.name=name
#             self.marks=marks
#             print(self)
#             print("Adding new student in database.....")

# s1=Student("Om Gupta",92)
# print(s1.name,s1.marks)

# s2=Student("Shreyash",87)
# print(s2.name,s2.marks)

# s3=Student("Shnayaa",95)
# print(s3.name,s3.marks)

# class Student:
#     #default constructor
#     def __init__(self):
#           pass

#     #parameterized constructors
#     def __init__(self,name,marks,class_room):
#             self.name=name
#             self.marks=marks
#             self.class_room=class_room
#             print(self)
#             print("Adding new student in database.....")

# s1=Student("Om Gupta",92,"Class A")
# print(s1.name,s1.marks,s1.class_room)

# s2=Student("Shreyash",87,"Class B")
# print(s2.name,s2.marks,s2.class_room)

# s3=Student("Shnayaa",95,"Class C")
# print(s3.name,s3.marks,s3.class_room)

class Student:
    class_room="Class A"    #class attribute (in class all parameter have something same in there field)
    college_name="IIT Roorkee"
    def __init__(self,name,marks):
            self.name=name      #object attribute
            self.marks=marks

    def welcome(self):        #methods (it is function defines inside a class)
          print("Welcome to the college!",self.name)
    
    def get_marks(self):
          return self.marks

s1=Student("Tony",92)
s1.welcome()
print(s1.name,s1.college_name,s1.class_room)
print(s1.get_marks())

#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a ethod to print the average 
class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def avg(self):
        return (self.marks1 + self.marks2 + self.marks3)/3    

# s1=Student("Kartik",69,78,57)
# print(s1.name,s1.marks1,s1.marks2,s1.marks3,"Average is",s1.avg())

# Abstraction: Hiding the implimentation details of a class and only showing the essential features to the user.
# Encapsulation: Wrapping data and functions into a single unit(object)


#create Account class with 2 attributes- balance & account no.Create methods foe debit,credit & printing the balance
class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    
    def debit(self):
        debit=int(input("Enter ammount to debit:"))
        return ("₹",self.balance-debit,"is debited")

    def credit(self):
        cr=int(input("Enter the credited amount:"))
        return (cr,"is credited sucessfully") 
     
    def get_bal(self):
        return self.balance

acc1=Account(25890,808573545)
acc1.debit()
acc1.credit()
acc1.get_bal()        

#Abstraction-"hiding the implimentation details of a class and only showing the essential features to the user"
#Encapsulation-"wrapping data and functions into a single unit."