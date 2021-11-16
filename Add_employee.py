import pymysql
from pymysql import cursors

bdd = pymysql.connect(host="127.0.0.1", port=3306, db='classicmodels', user='root', password='')

cursor= bdd.cursor()

sql= "insert into employees values('%d', '%s', '%s', '%s', '%s', '%s', null , '%s')"

try:
    cursor.execute(sql % (1800, 'mohamedi', 'mohamed', 'x5555', 'm@gmail.com', 1, 'ts' ))
    bdd.commit()
    nb =cursor.rowcount
    if nb == 1:
        print('employe insert')
    else:
      print('employe nom insert')    
    
except Exception:
    bdd.rollback()
    print("error of insert")

bdd.close()        
