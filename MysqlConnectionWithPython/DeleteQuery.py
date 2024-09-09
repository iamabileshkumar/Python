import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="############",
    database="#####"
)
cursor=mydb.cursor()
cursor.execute("delete from data_q where (id<=10) and (id>=1)")
mydb.commit()
cursor.execute("Select * from data_q")
print(cursor.fetchall())

