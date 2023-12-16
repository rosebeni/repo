#install Mysql on your computer
#https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python.

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'abac.win',
    user = 'root',
    passwd = 'K8$N05Pgywe)^sx23D*qeiY2%',
)

#prepare a cursor object
cursorObject = dataBase.cursor()

# Creare a database
cursorObject.execute("CREATE DATABASE dcrm")

print("All Done!")