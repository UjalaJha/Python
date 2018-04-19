from tkinter import *
from tkinter import messagebox

root = Tk()
def Ack():
   messagebox.showinfo("Submission", "Form Submitted!")

def exit_():
    root.destroy()

root.title("Personal Details")
frame1 = Frame(root, bd='3', relief='groove',width='100')
frame1.grid(sticky='n')

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_separator()
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit", command=exit_)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
    
name = Label(frame1, text="Name",width='15',height='2').grid(row='0',column='0')
email = Label(frame1, text="Email",width='15',height='2').grid(row='1',column='0')
gender = Label(frame1, text="Gender",width='15',height='2').grid(row='2',column='0')
pno = Label(frame1, text="Contact No.",width='15',height='2').grid(row='5',column='0')

e1 = Entry(frame1,width='25').grid(row='0',column='1')
e2 = Entry(frame1,width='25').grid(row='1',column='1')
var = IntVar()
R1 = Radiobutton(frame1, text="Male", variable=var, value=1,height='2').grid(row='2',column='1')
R2 = Radiobutton(frame1, text="Female", variable=var, value=2,height='2').grid(row='2',column='2')
e3 = Entry(frame1,width='25').grid(row='5',column='1')

lang = Label(frame1, text="No. of Known Languages",width='25',height='2').grid(row='6',column='0')
w = Spinbox(frame1, from_=0, to=5).grid(row='6',column='1')

Country = Label(frame1, text="Country",width='15',height='2').grid(row='7',column='0')
var=StringVar()
choices = ['India', 'USA']
option = OptionMenu(root, var, *choices)
option.place(x=190,y=190, height=25, width=100)


interest = Label(frame1, text="Interests",width='15',height='2').grid(row='8',column='0')
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(frame1, text = "Painting", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
C2 = Checkbutton(frame1, text = "Acting", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
C3 = Checkbutton(frame1, text = "Others", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
C1.grid(row='8',column='1')
C2.grid(row='8',column='2')
C3.grid(row='8',column='3')




B1 = Button(frame1, text ="Submit", command = Ack,width='15',height='2',relief='raised').grid(row='9',column='1')
B2 = Button(frame1, text ="Exit", command = exit_,width='15',height='2').grid(row='9',column='2')



