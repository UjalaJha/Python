reclen=20
with open("cities.bin","wb") as f:
    n=int(input('How many entries?'))

    for i in range(n):
        city=input('City name :')
        ln=len(city)
        city=city+(reclen-ln)*' '
        city=city.encode()
        f.write(city)

with open("cities.bin","rb") as f:
    n=int(input('How record number'))
    f.seek(reclen*(n-1))
    str=f.read(reclen)
    print(str.decode())

