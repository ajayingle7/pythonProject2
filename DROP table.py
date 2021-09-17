import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    username= "root",
    password= "Admin",
    charset= "utf8",
    database= "poonam"
)
#drop table FROM database poonam

mycursor = mydb.cursor()
b=mycursor.execute('USE poonam')
a=mycursor.execute("DROP TABLE mytable")
print(b,a)
mydb.commit()