from tkinter import*
root=Tk()
c=Canvas(root,height=1000,width=1000,cursor='pencil')
c.pack()
id=c.create_rectangle(250,200,500,500,fill="green",outline="black")
id=c.create_polygon(200,200,250,100,500,100,550,200,fill="blue",outline="black")
id=c.create_rectangle(312,300,437,500,fill="yellow",outline="black")
id=c.create_rectangle(300,20,350,100,fill="brown",outline="black")
id=c.create_rectangle(400,230,480,280,fill="yellow",outline="black")

root.mainloop()
