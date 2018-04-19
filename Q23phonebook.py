with open("phone.dat","wb") as f:
    n=int(input('How many entries?'))

    for i in range(n):
        name=input('enter name :')
        phone=input('enter no.')
        name=name.encode()
        phone=phone.encode()
        f.write(name+phone)
