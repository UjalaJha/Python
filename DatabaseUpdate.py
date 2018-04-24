import MySQLdb
def update_row(name):
    conn=MySQLdb.connect(host='localhost',database='employee',user='root',password='')
    cursor=conn.cursor()
    str="update empinfo set salary=salary+10000 where name='%s'"
    args=(name)
    try:
        cursor.execute(str % args)
        conn.commit()
        print('One row updated')
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

n=input("Enter Name : ")
update_row(n)
    


conn=MySQLdb.connect(host='localhost',database='employee',user='root',password='')
cursor=conn.cursor()   
print('After updation : ' )
cursor.execute("select * from empinfo")
rows=cursor.fetchall()
print("total no of rows is:",cursor.rowcount)
for row in rows:
    name=row[0]
    age=row[1]
    salary=row[2]
    print('%-15s %-6d %15.2f'%(name,age,salary))

