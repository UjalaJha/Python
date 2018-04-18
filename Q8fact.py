def factorial(num):
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        print("factorial is : ")
        print(fact)

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

    
m=int(input("Enter the number : "))
factorial(m)
print(recur_factorial(m))


