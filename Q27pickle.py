import pickle

class Emp:
    def __init__(self,idt,name):
        self.id=idt
        self.name=name
    def display(self):
        print(name)
        print(idt)
        

# take user input to take the amount of data
f=open('emp.dat','wb')
n = int(input('Enter the number of data : '))


# take input of the data
for i in range(n):
    idt = int(input('Enter id'))
    name=input('Enter name')
    


e=Emp(idt,name)


# dump information to that file
pickle.dump(e,f)

# close the file
f.close()


# open a file, where you stored the pickled data
f=open('emp.dat','rb')

while True:
    try:
        data = pickle.load(f)
        data.display()
    except EOFError:
        print('end')
        break
    

# close the file
f.close()
