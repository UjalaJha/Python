#zero division
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

try:
	c=a/b
	print(c)
	
except ZeroDivisionError as args:
	print("Exception:- ",args)
else:
	print("Successfully division done")

#value error
try:
    a=int(input("Enter no : "))
except ValueError as args:
        print("Exception:- ",args)
else:
	print("Successfully  done")

#syntax error
try:
    a=eval(input("Enter date: "))
except SyntaxError as args:
        print("Exception:- ",args)
else:
	print("Successfully  done")
#IOError
try:
        name=input("Enter filename : ")
        f=open(name,'r')
except IOError as args:
        print("Exception:- ",args)
else:
	print("Successfully  done")

#asserterror
try:
        x=int(input("Enter no between 5 and 10 : "))
        assert x>=5 and x<=10, "wrong input"
except AssertionError as args:
        print("Exception:- ",args)
else:
	print("Successfully  done")

#import error
try:
        import abclib
except ImportError as args:
        print("Exception:- ",args)
else:
	print("Successfully  done")


