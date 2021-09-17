import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    username= "root",
    password= "Admin",
    charset= "utf8",
    database= "poonam"
)
#DELETE RECORD FROM TABLE

mycursor = mydb.cursor()
b=mycursor.execute('USE poonam')
a=mycursor.execute("DELETE FROM company WHERE NAME= 'Jagu'")
print(b,a)
mydb.commit()