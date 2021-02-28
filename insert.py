import mysql.connector
connection_object=mysql.connector.connect(host="localhost", user="root", passwd="Mahesh@27", database="crudoperations")
if(connection_object):
    print("connected to database")
else:
    print("not connected to database")
cursor_object=connection_object.cursor()
if(cursor_object):
    print("created cursor")
else:
    print("cursor creation failed")
try:
    sql_query="insert into student values(%s,%s,%s)"
    values=(190032081, "B.Pradeep Reddy", "CSE")
    insert_query=cursor_object.execute(sql_query,values)
    connection_object.commit()

except:
    connection_object.rollback()
print(cursor_object.rowcount,"record inserted")
cursor_object.close()
connection_object.close()