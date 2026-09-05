# FUNCTION AND RECURSION
def sum(a,b):
    s=a+b
    print(s)
sum(9,8)

# def sqrt(n):
#     s=n*n    # or can be write s=n**2
#     print("The square root is",s)
# sqrt(9)

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("Fcatorial is",fact)
fact(5)

def print_meme():
    print("Oooo maaaaa gooo trueeeee lub")
print_meme()
print_meme()
print_meme()
print_meme()
print_meme()

#Create a fun for calculacting avg
# def avg(a,b,c,d):
#     s=(a+b+c+d)/4
#     return s
# print(avg(20,50,40,80))


#WAP to find length of a list
# cities=["Nagpur","Pune","Mumbai","Amsterdam","Chicago","New York","New Delhi","Ahemdabad"]
# def len_list(l):
#     return len(l)
# print(len_list(cities))

#WAP to convert USD to INR
def convert_to_INR(usd_val):
    inr_val=usd_val*93.7
    print("$",usd_val,"=","₹",inr_val)
convert_to_INR(49)

#Recusive function 

def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)

show(5)

#Factorial program by recursion
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

# def sum_n(n):
#     if n==0:
#         return 0
#     return n+sum_n(n-1)
# print(sum_n(20))

#Write a recurcive funtion to print all elements in a list

def print_list(l,ind=0):
    if ind==len(l):
        return
    print(l[ind])
    print_list(l,ind+1)

# film=["Toxic","Animal","KGF","Pushpa","Super 30","The Conjuring","Heridiatry","Desi Boyz","Baaghi","Marco"]
# print_list(film)
