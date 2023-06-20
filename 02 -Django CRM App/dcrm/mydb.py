# 1) Install MySQL on your computer
# 1) download from mysql website, use the community version
# 2) pip install mysql
# 3) pip install mysql-connector (AND mysql-connector-python)

import mysql.connector
import time


dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'Alchemist@Zotti2023!',
)

# Prepare a cursor object (cursorObjetct)

cursor_object = dataBase.cursor()

# Create a Database

cursor_object.execute("CREATE DATABASE crm_project_db")
print("All done sir!")