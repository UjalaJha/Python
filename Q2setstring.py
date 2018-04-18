
#create integer set from list
list1=[1,2,3,4,5]
b=[4,5]
s=set(list1)
print("integer set of list is : ")
print(s)

#character set
ch=set("Hello, how are you 5?")
print("character set of list is : ")
print(ch)

#set operation
print("Original Set")
print(s)

print("After removing an element from : ")
s.remove(1)
print(s)

print("After poping an element from : ")
s.pop()
print(s)


print("After discarding an element from : ")
s.discard(3)
print(s)

print("Intersection of both set : ")
print(s.intersection(b))


#string

str1="Hello ujala, how are you"
str2="i hope you did well today"

print("\nString is ")
print(str1)
print("Replace :")
print(str1.replace('ujala','gaurav'))


print("Count a :")
ch="a"
print(str1.count(ch,0,10))

print("Capitalize :")
print(str2.capitalize())

print("Join :")
print(" ".join(str2))

