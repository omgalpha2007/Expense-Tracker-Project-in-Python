#Dictionary & Sets
# dict={"naam":"Shardha","cgpa":9.6,"place":"NewDelhi"}
# print(dict["cgpa"])
# dict["course"]="M.tech"
# print(dict)

# info={"name":"Andrew",
#       "age":36,
#       "marks":94.4,
#       "type":"Feminist",
#       "cars":["Bugatti Chorin SS","Ferari SF90","Pagani Hyuara","Koenigsegg Jesko","AM Valhala"],
#       "country":"Romenia"}
# print(info)

#null dictionary
null_dict={}
print(null_dict)

student={"name":"Ankush",  #nested dictionary
         "subjects":{
             "phy":76,
             "chem":69,
             "maths":91},
         "Class":12
         }
print(student)
print(student["subjects"])


#Dictionary Methods
print(student.keys())
print(info.values())
print(info.items())        #Returns all (key,val) pairs as tuples
print(info.get("cars"))
print(student.update(dict))

#print(len(list(info)))
new_dict={"Place":"New Majri","Age":17}
student.update(new_dict)
print(student)

print(info.__sizeof__())

#Sets In Python
num={1,2,4,6,8,5,9}
set2={9,2,7,0,2,5,8,5,1,0}
print(num,set2)
null_set= set()      #empty set syntax
print(null_set)
print(type(num))
print(len(set2))
print(type(null_set))

#Sets Methods
set2.add(7)      #add an element
print(set2)
set2.remove(0)   #removes the element
print(set2) 
num.clear()  #empties the set 
print(num)
print(set2.pop())    #remove a random element
num.add((2,3,5,4,2,7,6,9,5,0,8))
print(num)

set1={1,2,4,3,7,9,5,0}
set2={5,6,3,0,7,2,8,9,0}
print(set1.union(set2))        #combines both set values n retun new
print(set1.intersection(set2))          #combines common values n retun new 

#Practice Question

#store in dictionary
storage={"table":["a peice of furniture", "list of facts n figure"],"cat":"an small animal"}
print(storage)

#You are given a list of subjects for students.Assume one classroom is required for 1 subject.How man classrooms are needed by all the students
# "python","java","C++","python","javascript","java","python","C++","C"
subjects={"python","java","C++","python","javascript","java","python","C++","C"}
print("Total no. of classrooms required",len(subjects))

#WAP to enter marks of 3 subjects from the user n store them in  dictionary.Start with an empty dict n add 1 by 1.
result={}
print(result)
x=int(input("Enter phy's marks:"))
result.update({"phy":x})
y=int(input("Enter math's marks:"))
result.update({"math":y})
z=int(input("Enter chem's marks:"))
result.update({"chem":z})
print(result)
print(type(result))

#Figure out a way to store 9 & 9.0 as separate values in the set.
val={9,"9.0"}
print(val)

values={("float",9.0),("int",9)}
print(values)