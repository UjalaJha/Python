#zero division error
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

try:
	c=a/b
	print(c)
	
except ZeroDivisionError as args:
	print("Exception:- ",args)
else:
	print("Successfully division done")



try:
        date=eval(input("Enter Date"))
except SyntaxError as args:
        print("Exception:- ",args)
else:
	print("Successfully  done")

try:
        name=input("Enter filename")
        f=open(name,'r')
except IOError as args:
        print("Exception:- ",args)
else:
	print("Successfully  done")

try:
        x=int(input("Enter no between 5 and 10"))
        assert x>=5 and x<=10, "wrong input"
except AssertionError as args:
        print("Exception:- ",args)
else:
	print("Successfully  done")

# A python program to create user-defined exception
 
# class MyError is derived from super class Exception
class MyError(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
 
try:
    raise(MyError(3*2))
 
# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occured: ',error.value)


