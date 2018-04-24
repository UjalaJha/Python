
reclen=20
f=open('city.bin','wb')
n=int(input('entries total? : '))

for i in range(n):
    name=input('Name : ')
    ln=len(name)
    name=name+(reclen-ln)*' '
    name=name.encode()
    f.write(name)
f.close()

f=open('city.bin','rb')
n=int(input('entries record no : '))
f.seek(reclen*(n-1))
str=f.read(reclen)
print(str.decode())
f.close()
