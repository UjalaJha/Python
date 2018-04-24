#inner class
class person:
    def __init__(self):
        self.name='charles'
        self.db=self.dob()

    def display(self):
        print("name = ",self.name)

    class dob:
        def __init__(self):
            self.dd=10
            self.mm=10
            self.yy=10

        def display(self):
            print("dob = {}/{}/{}".format(self.dd,self.mm,self.yy))

p=person()
p.display()

r=p.db
r.display()


#static method
import math
class Sample:
    @staticmethod
    def cal(x):
        result=math.sqrt(x)
        return result
num=float(input('Enter Number : '))
res=Sample.cal(num)
print(res)
