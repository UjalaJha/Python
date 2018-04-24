from tkinter import *
class mybutton:
    def __init__(self,root):
        self.f=Frame(root,height=400,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f,text='RED',width=15,height=2,
                       command=lambda:self.buttonclick(1))
        self.b2=Button(self.f,text='GREEN',width=15,height=2,
                       command=lambda:self.buttonclick(2))
        self.b1.pack()
        self.b2.pack()

    def buttonclick(self,num):
        if num==1:
            self.f["bg"]='red'
        if num==2:
            self.f["bg"]='green'

root=Tk()
mb=mybutton(root)
root.mainloop()
