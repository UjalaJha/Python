import math
class opp:
    def add(self,x=None,y=None,z=None):
        if x!=None and y!=None and z!=None:
            print("Sum = %.4f "%(x+y+z))
        elif x!=None and y!=None:
            print("Sum = %.4f "%(x+y))

o=opp()
o.add(2,3)
o.add(2,3,4)
