import MySQLdb
conn=MySQLdb.connect(host='localhost',database='employee',user='root',password='')
cursor=conn.cursor()
str="insert into empinfo(name,age,salary)values('raj',20,2333)"
try:
    cursor.execute(str)
    conn.commit()
    print('One row inserted')
except:
    conn.rollback()
print('After Insertion : ' )
cursor.execute("select * from empinfo")
rows=cursor.fetchall()
print("total no of rows is:",cursor.rowcount)
for row in rows:
    name=row[0]
    age=row[1]
    salary=row[2]
    print('%-15s %-6d %15.2f'%(name,age,salary))
cursor.close()
conn.close()
