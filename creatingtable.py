import mysql.connector
connection_object=mysql.connector.connect(host="localhost",user="root",passwd="Mahesh@27",database="crudoperations")
if connection_object:
    print("connected successfully to databse")
else:
    print("not connected to database")
cursor_object=connection_object.cursor()
if cursor_object:
    print("created successfully  cursor")
else:
    print("not created cursor")

try:
    create_table=cursor_object.execute("create table student(id integer(10) primary key,name varchar(15),department varchar(5))")
    print("table created successfuly")
except:
    connection_object.rollback();

cursor_object.close()
connection_object.close()