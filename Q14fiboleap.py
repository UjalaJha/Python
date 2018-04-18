#fibo
n=20
print("fibo sequence : ")
t1=0
print(t1)
t2=1
print(t2)
i=1
for i in range(1,n-1):
    t3=t2+t1
    print(t3)
    t1=t2
    t2=t3
    i=i+1



#A leap year is exactly divisible by 4 except for century years(years ending with 00).
#The century year is a leap year only if it is perfectly divisible by 400.
#For example,= 2000

# Toget year (integer input) from the user
# year = int(input("Enter a year: "))

year=2016
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
