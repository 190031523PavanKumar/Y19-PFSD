import mysql.connector
connection_object=mysql.connector.connect(host="localhost",user="root",passwd="Mahesh@27")
if(connection_object):
    print("connection successful")
else:
    print("not connected")
cursor_object=connection_object.cursor();
if(cursor_object):
    print("cursor object created successfully")
else:
    print("not created cursor object")
try:
    create_database=cursor_object.execute("create database crudoperations")
    print("created database successfully")
except:
    connection_object.rollback()



cursor_object.close()
connection_object.close()