#inheritance
class Person:  
    name = ""  
    age = 0  
 
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  

    def showName(self):  
        print('Name:- ',self.name)  
  
    def showAge(self):  
        print('Age:- ',self.age)  

class Student(Person):
    studentId = ""  
  
    def __init__(self, studentName, studentAge, studentId):  
        Person.__init__(self, studentName, studentAge)  
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  
     
person1 = Person("Ram", 23)  
person1.showName() 
person1.showAge()
student1 = Student("Shyam", 22, "102")  
print('StudentId:- ',student1.getId())  
student1.showName()
student1.showAge()    


#polymorphism and overiding
class Shape:
    def side(self) : 
        print('It is a polygon.')

class Triangle(Shape) :
    def side(self) : 
        print('It is a triangle.')
    def details(self) :
        print('It has 3 sides.')

class Rect(Shape) :
    def side(self) : 
        print('It is a rectangle.')
    def details(self) :
        print('It has 4 sides.')

class Pent(Shape) :
    def side(self) : 
        print('It is a pentagon.')
    def details(self) :
        print('It has 5 sides.')

s=Shape()
t=Triangle()
r=Rect()
p=Pent()
print('Overridden Method : ')
s.side()
t.side()
r.side()
p.side()
print('Polymorphism : ')
t.details()
r.details()
p.details()

#overloading

lass Human:
    def sayHello(self, name=None):
 
        if name is not None:
            print ('Hello' + name)
        else:
            print ('Hello')
 
# Create instance
obj = Human()
# Call the method
obj.sayHello()
# Call the method with a parameter
obj.sayHello('Ujala')
