f=open('phoneb.dat','wb')
n=int(input('entries total? : '))
for i in range(n):
    name=input('Name : ')
    name=name.encode()
    phone=input('Phone : ')
    phone=phone.encode()
    f.write(name+phone)
f.close()

