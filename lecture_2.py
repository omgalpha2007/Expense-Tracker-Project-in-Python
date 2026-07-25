str1="This is a string"
str2='YOU ARE STUPID'
str3='''3 qoutes string'''

#concatenation
print(str+str2)

#replication 
print(3*str2)

#membership (in or not in)
print("a" in "neha")
print("e" in "om")

#escape sequence characters
str="This is a string \n"
str4="This is a string \n You're learning python"
str5="str2"+"\t gives the space of a tab" 
print(str,str4,str5) 
print(len(str2))
print(str2[:14])
print(str[3:])
print(str3[-5:-2])

#String Functions

str="i am a coder."
print(str)
print(str.endswith("er."))
print(str.capitalize())
print(str.replace("coder","engineer"))
print(str.find("am"))
print(str.count("e"))

#WAP to input user's name & print its length
name=input("Enter 1st name :")
print(len(name))

#WAP to find the occurance of $ in a str
occ="hii, $I am $ dollar symbol of $99.99"
print(occ.count("$"))

#CONDITIONAL STATEMENTS 
'''FOR CHECKING AGE'''
age=int(input("Enter your age"))
if (age>=18):
     print("You are eligible for voting and driving")
else:
    print("You have to wait for few more years")

#grading to student 
marks=int(input("Enter your marks"))
if(marks>=90):
    print("Grade='A'")
elif(90>marks>=80):
    print("Grade='B'")
elif(80>marks>=70):
    print("Grade='C'")
else:
    print("Grade='D'")


#WAP TO FIND GREATEST NO.
a=int(input("Enter a no."))
b=int(input("Enter a no."))
c=int(input("Enter a no."))
if(a>b and a>c):
    print(a,"is greatest among 3.")
elif(b>a and b>c):
    print(b,"is greatest among 3.")
else:
    print(c,"is greatest among 3.")


#CHECKING MULTIPLE OF 7
num=int(input("Enter a number:"))
if(num%7==0):
    print(num,"is multiple of 7")
else:
    print(num,"is not multiple of 7")