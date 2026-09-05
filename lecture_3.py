marks=[67.5,64,89.6,79.3,58]
print(marks)
print(type(marks))
print(marks[3])
marks[2]="Isagi"
print(marks[2])
print(marks[1:])
print(marks[:5])
print(marks[2:6])

#LIST METHODS
l=[2,1,3]
print(l.append(5))
print(l)
l.sort()
int(l)
d=[4,6,8,7,9]
print(d)
l.extend(d)
print(l)
l.insert(4,"Hola Amigo")
print(l)
l.pop(4)
l.remove(7)
print(l)
print(min(l))
print(max(l))
print(sum(l))
l.clear()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()


#Creating a 2D list
lst=[]
r=int(input("How many rows :"))
c=int(input("How many columns :"))
for i in range(r):
    row=[]
    for j in range(c):
        ele=int(input("Element"+str(i)+","+str(j)+":"))
        row.append(ele)
    lst.append(row)
print("List created is:",lst)

#TUPLE IN Python 
tup=(1,3,2,4,5,9,5,2,3,5,3,)
print(type(tup))
print(tup[2])
t1=(3,)  #single element tuple
t2=("Hello","World")
print(t2)
print(tup.index(3))
print(tup.count(5))

#WAP to enter 3 fav movie name n store in list
l=[]
m1=input("Enter your 1st fav movie names :")
m2=input("Enter your 2nd fav movie names :")
m3=input("Enter your 3rd fav movie names :")
l.append(m1)
l.append(m2)
l.append(m3)
print(l)

#WAP to check a list contain a palindrome
l1=[1,2,3,4,4,3,2,1]
l2=[]
#l2.extend(l1) 
l2=l1.copy()
l2.reverse()
print(l2)
if l1==l2:
    print("Palindrome list")
else:
    print("Not a Palindrome list")