import MySQLdb
from tkinter import *
root=Tk()
def retrieve_row(name):
    conn=MySQLdb.connect(host='localhost',database='employee',user='root',password='')
    cursor=conn.cursor()
    try:
        str="select *from empinfo where name='%s'"
        args=(name)
        cursor.execute(str % args)
        row=cursor.fetchone()
        if row is not None:
            lbl=Label(text=row,font=('Arial',14)).place(x=50,y=200)
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def display(self):
    conn=MySQLdb.connect(host='localhost',database='employee',user='root',password='')
    cursor=conn.cursor()
    str=e1.get()
    lbl=Label(text="You entered : "+str,font=('Arial',14)).place(x=50,y=150)
    retrieve_row(str)

f=Frame(root,height=350,width=600)
f.propagate(0)
f.pack()
lbl=Label(text="Enter Employee name : ",font=('Arial',14)).place(x=50,y=100)
e1=Entry(root,width=15,fg='blue',bg='yellow',font=('Arial',14))
e1.place(x=300,y=100)
e1.bind("<Return>",display)
root.mainloop()

         
