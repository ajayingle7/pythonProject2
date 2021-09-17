import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    username= "root",
    password= "Admin",
    charset= "utf8",
    database= "poonam"
)


mycursor = mydb.cursor()
b=mycursor.execute('USE poonam')
a=mycursor.execute("INSERT INTO company (ID,NAME,AGE,SALARY) VALUES(5,'Jagu',28,15000)")
print(b,a)
mydb.commit()