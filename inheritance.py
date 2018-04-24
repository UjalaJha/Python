class father:
    def __init__(self,property=0):
        self.property=property

    def display(self):
        print("Father Property= ",self.property)
class son(father):
    def __init__(self,property1=0,property=0):
        super().__init__(property)
        self.property1=property1

    def display(self):
        print("Total Property= ",self.property+self.property1)


s=son(2000,20)
s.display()
