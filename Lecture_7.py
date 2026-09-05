#File Handling 

#Opening,reading and closing a file
f=open("demo.txt","r")
data=f.readline()
print(data)
print(type(data))
f.close()

f=open("demo.txt","r")
line1=f.readline()
print(line1)
print(type(line1))
f.close()

#Over writting to a file
f1=open("demo2.txt","w")
f1.write("Surprise!Surprise!MF the king is back")
f1.close()

#Appending lines to new files
f2=open("demo3.txt","a")
f2.write("Hellooooo Everybody.\nWhat's up,enjoying the day or ruining it in overthinking\n ")
f2.close()

#Deleting a file
import os
os.remove("demo3.txt")

#Practice quetions
f=open("practice.txt","w+")
f.write("Hi everyone\n we are learning File I/O \n using Java.\n I like programming in Java.")
data=f.read()
print(data)
f.close()

with open("practice.txt","r") as f1:
    data=f1.read()

new_data=data.replace("Java","Python")
print(new_data)

#program for word checking
def check_line():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)):
            print("Found")
        else:
            print("Not Found")
check_line()

#for checikng no. in file and finding even no. among them 
count=0
with open("practice.txt","r") as f:
    data=f.read()
    print(data)
    num=data.split(",")
    print(num)
    for val in num :
        if (int(val))%2==0:
            count+=1
print(count)
