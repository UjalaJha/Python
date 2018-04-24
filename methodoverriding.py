import math
class square:
    def area(self,x):
        print("Area = %.4f "%(x*x))
class circle(square):
    def area(self,x):
        print("Area = %.4f "%(x*x*x))

c=circle()
c.area(3)
          
