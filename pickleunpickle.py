import pickle
class emp:
    def __init__(self,name,idt):
        self.name=name
        self.idt=idt
    def display(self):
        print(self.name,self.idt)

f=open('employee.dat','wb')
n=int(input('entries total? : '))

for i in range(n):
    idt=int(input('ID : '))
    name=input('Name : ')
    e=emp(name,idt)
    pickle.dump(e,f)

f.close()

f=open('employee.dat','rb')
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("END")
        break
f.close()
