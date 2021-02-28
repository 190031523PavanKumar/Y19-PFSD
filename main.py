import mysql.connector
connection_obj=mysql.connector.connect(host="localhost",user="root",passwd="Mahesh@27");
cursor_object= connection_obj.cursor()
try:
    dbs=cursor_object.execute("show databases")
except:
    connection_obj.rollback();
for i in cursor_object:
    print(i)
cursor_object.close()
connection_obj.close()