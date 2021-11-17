import pymysql
from xml.dom import minidom
from pymysql import cursors

root = minidom.Document()
cnr = root.createElement("cnr")
root.appendChild(cnr)

    
bdd = pymysql.connect(host="127.0.0.1", port=3306, db='classicmodels', user='root', password='')

cursor= bdd.cursor(pymysql.cursors.DictCursor)

sql= 'select * from employees'
try:
    cursor.execute(sql)
    result = list(cursor.fetchall())
    #result.sort(key=order)
    for emp in result:
        emp1=root.createElement("employees")
        emp1.setAttribute("id", str(emp["employeeNumber"]))
        nom = root.createTextNode("%s %s" % (emp["firstName"], emp["lastName"]))
        emp1.appendChild(nom)
        cnr.appendChild(emp1)
        
    file = open("cnr2.xml", "w")
    file.write(root.toprettyxml("\t"))
    file.close()
except Exception as e:
    print(e)

bdd.close()        
