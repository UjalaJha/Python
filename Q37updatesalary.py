import MySQLdb
conn=MySQLdb.connect(host='localhost',database='emp',user='root',password='')
cursor=conn.cursor()
def update(amount):
    try:
        print('Before Updated')
        str="select *from empinfo"
        cursor.execute(str)
        row=cursor.fetchall()
        for row in row:
            #print(row)
            empid=row[0]
            name=row[1]
            age=row[2]
            salary=row[3]
            print('%-4d %-10s %-4d %-10.5f'%(empid,name,age,salary))

        print('After Updated')
        str="update empinfo set salary=salary+'%d'"
        args=(amount)
        cursor.execute(str % args)
        conn.commit()
        str="select *from empinfo"
        cursor.execute(str)
        row=cursor.fetchall()
        for row in row:
            #print(row)
            empid=row[0]
            name=row[1]
            age=row[2]
            salary=row[3]
            print('%-4d %-10s %-4d %-10.5f'%(empid,name,age,salary))
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    
amount=int(input("Enter the amount with which you want to increase the salary : "))
update(amount)
