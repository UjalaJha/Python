from tkinter import *
from tkinter import messagebox
import MySQLdb
root=Tk()
conn=MySQLdb.connect(host='localhost',database='form',user='root',password='')
cursor=conn.cursor()
def sub():
    name=e1.get()
    passw=e2.get()
    gender=var.get()
    interest1=var2.get()
    interest2=var3.get()
    country=var4.get()
    languages =var5.get()
    print(name,passw,gender,interest1,interest2,country,languages)
    messagebox.showinfo("Submission","Form Submitted")
    
    try:
        #str1="select * from reg"
        str="insert into reg(name,passw,gender,interest1,interest2,country,languages)values('%s','%s','%d','%d','%d','%s','%d')"
        args=(name,passw,gender,interest1,interest2,country,languages)
        #cursor.execute(str)
        cursor.execute(str % args)
        #row=cursor.fetchone()
        conn.commit()
        print("done")
        #print(row)
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    
def exit():
    root.destroy()

f=Frame(root,height=600,width=500)
f.propagate(0)
f.pack()

lbl=Label(text="Registration Form",font=('Arial',14)).place(x=180,y=50)
l1=Label(text="Enter Name : ",font=('Arial',14)).place(x=50,y=100)
e1=Entry(root,width=25,fg='blue',bg='yellow',font=('Arial',14))
e1.place(x=200,y=100)


l2=Label(text="Enter Password : ",font=('Arial',14)).place(x=50,y=150)
e2=Entry(root,width=25,fg='blue',bg='yellow',font=('Arial',14),show='*')
e2.place(x=200,y=150)


var=IntVar()
l2=Label(text="Enter Gender : ",font=('Arial',14)).place(x=50,y=200)
r1=Radiobutton(f,height=2,variable=var,value=1,
               fg='blue',font=('Arial',14),text='Male')
r2=Radiobutton(f,height=2,variable=var,value=2,
               fg='blue',font=('Arial',14),text='Female')
r1.place(x=200,y=190)
r2.place(x=300,y=190)



var2=IntVar()
var3=IntVar()
l3=Label(text="Enter Interest : ",font=('Arial',14)).place(x=50,y=250)
c1=Checkbutton(f,variable=var2,
               fg='blue',font=('Arial',14),text='Java')
c2=Checkbutton(f,variable=var3,
               fg='blue',font=('Arial',14),text='C++')
c1.place(x=200,y=250)
c2.place(x=300,y=250)

l3=Label(text="Enter Country : ",font=('Arial',14)).place(x=50,y=300)
var4=StringVar()
choices = ['India', 'USA']
option = OptionMenu(root, var4, *choices)
option.place(x=200,y=300)

var5=IntVar()
l4=Label(text="Languages Known : ",font=('Arial',14)).place(x=50,y=350)
w=Spinbox(root,textvariable=var5,from_ =0, to=5)
w.place(x=230,y=360)

b1=Button(root,text="SUBMIT",command=sub,width=15,height=2)
b1.place(x=100,y=400)

b2=Button(root,text="EXIT",command=exit,width=15,height=2)
b2.place(x=220,y=400)

root.mainloop()
