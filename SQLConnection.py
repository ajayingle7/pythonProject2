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
a=mycursor.execute("SELECT AGE FROM company WHERE NAME = 'AJAY' ")
c = mycursor.fetchall()
print(b,a,c)