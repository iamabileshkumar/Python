import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="###",
    database="###"
)
print(mydb.is_connected())
cursor=mydb.cursor()
cursor.execute("with cte as ( \
                select *, row_number() over(partition by sname order by marks desc) as rn \
                from studen \
                ) \
                select sname,sum(marks) \
                from cte \
                where rn<=2 \
                group by sname \
                ")
result=cursor.fetchall()
result1=cursor.fetchwarnings()
print(result,result1)
