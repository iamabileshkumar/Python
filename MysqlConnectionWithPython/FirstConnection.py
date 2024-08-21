import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="###",
    database="###"
)
print(mydb.is_connected(),"Database Connected Successfully")
cursor=mydb.cursor()
cursor.executemany("insert into data_q values(%s,%s)",((1,1),(10,10)))
mydb.commit()
cursor.execute("select * from data_q")
df=pd.DataFrame(cursor)
print(df)