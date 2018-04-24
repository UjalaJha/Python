import MySQLdb
conn=MySQLdb.connect(host='localhost',database='emp',user='root',password='')
cursor=conn.cursor()
def retrive(empid):
    try:
        str="select * from empinfo where empid = '%d'"
        args=(empid)
        cursor.execute(str % args)
        row=cursor.fetchone()
        if row is not None:
            #print(row)
            empid=row[0]
            name=row[1]
            age=row[2]
            salary=row[3]
            print('%-4d %-6s %-4d %-10.5f'%(empid,name,age,salary))
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    
empid=int(input("enter the empid : "))
retrive(empid)
