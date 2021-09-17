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
a=mycursor.execute("UPDATE company SET SALARY = 50000 WHERE SALARY = 15000")
print(b,a)
mydb.commit()