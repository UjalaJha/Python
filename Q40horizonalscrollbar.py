from tkinter import *

class myscrollbar:
        def __init__(self, root):
            #text widget
            self.t=Text(root,width=70,height=15,wrap=NONE)
            #text crowd
            for i in range(50):
                self.t.insert(END,"This is some text")
            #text to root window at top
            self.t.pack(side=TOP,fill=X)
            #create scroll bar and attach to text widget
            self.h=Scrollbar(root ,bg='green',orient=HORIZONTAL,command=self.t.xview)
            #attach text widget to horizontal scroll bar
            self.t.configure(xscrollcommand=self.h.set)
            #scroll to root window at bottom
            self.h.pack(side=BOTTOM,fill=X)

root=Tk()
ms=myscrollbar(root)
root.mainloop()
            
