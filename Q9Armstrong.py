m=int(input("Enter the number : "))
num=m
sum=0
while(num>0):
    d=num%10
    sum+=d**3
    num//=10
if m == sum:
   print(m,"is an Armstrong number")
else:
   print(m,"is not an Armstrong number")
