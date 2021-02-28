import mysql.connector
connection_object=mysql.connector.connect(host="localhost",user="root",passwd="Mahesh@27",database="crudoperations")
if(connection_object):
    print("connected successfully to datbase")
else:
    print("not connected to database")
cursor_object=connection_object.cursor()
if(cursor_object):
    print("created cursor")
else:
    print("not created cursor");
try:
    insert_many_query="insert into student values(%s,%s,%s)"
    values=[(190031353,"P.Jhanavi","CSE"),(190030564,"G.Deepthi Sree","CSE")]
    insert_many=cursor_object.executemany(insert_many_query,values)
    connection_object.commit()
except:
    connection_object.rollback()
print(cursor_object.rowcount,"records inserted")
connection_object.close()
cursor_object.close()

