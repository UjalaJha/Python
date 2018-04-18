

#accept integer convert to bytearray
listinteger=[1,2,3,4,5]
print( "list of integers is : " )
print(listinteger)
bytearrayinteger=bytearray(listinteger)
print( "Converting into bytearray : " )
for i in bytearrayinteger: print(i)


#create range of 1st 10 integer, odd 3-15 list
r=list(range(10))
print("range of 1st 10 integer : ")
print(r)
odd=list(range(3,17,2))
print("odd integer from 3-15 : ")
print(odd)


#create integer set from list
list1=[1,2,3,4,5]
s=set(list1)
print("integer set of list is : ")
print(s)

ch=set("Hello, how are you?")
print("character set of list is : ")
print(ch)

print("removing an element from list and adding ")
s.remove(1)
s.add(21)
print(s)
print("Union of both set")
print(s.union(ch))
