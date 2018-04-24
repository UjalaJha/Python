class BookX:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
class BookY:
    def __init__(self,pages):
        self.pages=pages

b1=BookX(150)
b2=BookY(100)
print("total pages = ",b1+b2)


class BookX:
    def __init__(self,pages):
        self.pages=pages
    def __gt__(self,other):
        return self.pages+other.pages
class BookY:
    def __init__(self,pages):
        self.pages=pages

b1=BookX(150)
b2=BookY(100)

if(b1>b2):
    print("BookX has more pages")
else:
    print("BookY has more pages")
