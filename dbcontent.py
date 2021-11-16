import pymysql
from pymysql import cursors

bdd = pymysql.connect(host="127.0.0.1", port=3306, db='classicmodels', user='root', password='')

cursor= bdd.cursor()

sql= 'select * from employees'

try:
    cursor.execute(sql)
    result = cursor.fetchall()
    for emp in result:
        print(emp)
except Exception: pass

bdd.close()        
