list1=[1,2,3,"ujala",'a',1]
print(list1)
list2=['b','a',3,7,9,"raj"]
print(list2)
list3=["ujala",[1,2,3,5,6],['a',55]]
print(list3)
print("\naccessing element")
print(list3[1][2])

#list opperation

list4=[1,2,4,3,5]

print("\nList is")
print(list4)

list4.append(66)
print(list4)

list4.insert(0,34)
print(list4)

list4.remove(2)
print(list4)

list1.extend(list2)
print(list1)

list4.pop()
print(list4)

print(list4.count(1))

list4.sort()
print(list4)

indexx=list4.index(4)
print(indexx)
