import mysql.connector

pymysql.connect(db='base', user='root', passwd='pwd', unix_socket="/tmp/mysql.sock")


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)