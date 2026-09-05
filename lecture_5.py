# Loops in Python

# count=1
# while count<=5:
#     count+=1
#     print("Hello",count)
#print(count)

#printing no. upto 100
# i=1
# while i<=100:
#     i+=1
#     print(i)

#print the multiplication table of a number n
# n=int(input("Enter a no. for its table:"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",(n*i))
#     i+=1

# i=1
# while i<=10:
#     print(i**2)
#     i+=1

# Search for no. x in the tuple using loops
# t=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter the no. to search:"))
# i=0
# while i<len(t): 
#     if (t[i])==x:
#         print("Found at index",i)
#     i+=1

#use of break func
# i=0
# while i<6:
#     if i==3:
#         break
#     print(i)
#     i+=1

# use of continue func
# i=0
# while i<10:
#     if i==5:
#         i+=1
#         continue       #it skips the next code when i==5 and pionter go to while loop for restart after i==5
#     print(i)
#     i+=1


# program to print even no. from 1 to 100
# i=1
# while i<=100:
#     if (i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# FOR LOOP
# num=[1,2,3,4,5,6,7,8,9]
# for val in num:
#     print(val)
# else:
#     print("END")

# str="My Enemies Are Many,Mine Equals Are None."
# for i in str:
#     print(i)

t=(1,4,9,16,25,36,49,64,81,100)
for el in t:
    print(el)
    if (el==49):
        print("Found")
        el+=1
        break
    el+=1

#THE range() function
# for i in range(1,5,2):           #range(start,stop,step)
#     print(i)

# for i in range(10,1,-2):
#     print(i)

#WAP to fond sum upto n numbers  by while loop
n=int(input("Enter a number :"))
sum=0
i=1
while i in range(1,n+1):
    sum+=i
    i+=1
print("The sum of",n,"is",sum)

#WAP to find factorial of first n natural no.
int(input("Enter a no. for factorial:"))
fact=1
if n==0:
    print("The no. is zero")
elif n==1:
    print("The factorial of no. is 1")
elif n>1:
    for i in range(1,n+1):
        fact*=i
        i+=1
    print("The factorial of",n,"is",fact)
else:
    print("The factorial of negative no. is not exist")
