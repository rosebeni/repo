#install Mysql on your computer
#https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python.

import mysql.connector
 
dataBase = mysql.connector.connect(
    host='localhost',
    user='beni',
    passwd='K8$N05Pgywe)^sx23D*qeiY2%',
)
 
# Prepare a cursor object
cursorObject = dataBase.cursor()
 
# Create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrm")
 
print("All Done!")