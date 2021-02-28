import mysql.connector
connection_object=mysql.connector.connect(host="localhost",user="root",passwd="Mahesh@27",database="crudoperations")
if(connection_object):
    print("connected to database")
else:
    print("not connected to database")
cursor_object=connection_object.cursor()
if(cursor_object):
    print("created cursor")
else:
    print("not created cursor")
try:
    cursor_object.execute("select * from student")
    # select * from student order by branch
    #select * from student order by branch desc
    values=cursor_object.fetchall()
    # fetchone
except:
    connection_object.rollback()
for i in values:
    print(i)
connection_object.close()
cursor_object.close()