import MySQLdb
def insert_row(name,age,salary):
    conn=MySQLdb.connect(host='localhost',database='employee',user='root',password='')
    cursor=conn.cursor()
    str="insert into empinfo(name,age,salary)values('%s','%d','%f')"
    args=(name,age,salary)
    try:
        cursor.execute(str % args)
        conn.commit()
        print('One row inserted')
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

n=int(input("how many rows : "))
for i in range(n):
    x=input('Enter name : ')
    y=int(input('Enter age : '))
    z=float(input('Enter salary : '))
    insert_row(x,y,z)
    print('---------------------------------------')


conn=MySQLdb.connect(host='localhost',database='employee',user='root',password='')
cursor=conn.cursor()   
print('After Insertion : ' )
cursor.execute("select * from empinfo")
rows=cursor.fetchall()
print("total no of rows is:",cursor.rowcount)
for row in rows:
    name=row[0]
    age=row[1]
    salary=row[2]
    print('%-15s %-6d %15.2f'%(name,age,salary))

