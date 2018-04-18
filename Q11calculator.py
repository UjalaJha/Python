def sum(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y

m=int(input("Enter the first operand : "))
n=int(input("Enter the second operand : "))
op=int(input("1 Add \n2 Subtract \n3 Multiply \n4 Divide \ngive input : "))
if op==1:
    print(sum(m,n))
elif op==2:
    print(sub(m,n))
elif op==3:
    print(mul(m,n))
elif op==4:
    print(div(m,n))
