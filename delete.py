import mysql.connector
connection_object=mysql.connector.connect(host="localhost",user="root",passwd="Mahesh@27",database="crudoperations")
if(connection_object):
    print("connected to database")
else:
    print("not connected to database")
cursor_object=connection_object.cursor()
if(cursor_object):
    print("cursor object successfully created")
else:
    print("cursor object not created")
try:
    query="delete from student where id='190032080'"
    delete_query=cursor_object.execute(query)
    connection_object.commit()
except:
    connection_object.rollback()

print(cursor_object.rowcount,"record deleted")
cursor_object.close()
connection_object.close()