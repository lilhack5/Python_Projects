#
# Python:   3.10.7
#
# Author:   Bryan
#
# Purpose:  The Tech Academy - Python Course, Creating a sql database using Python.

# Allows me to use Sql.
import sqlite3

# Creates a new database.
conn = sqlite3.connect('test2.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

with conn:
    cur = conn.cursor()
    # create table for test2 database
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_test2( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT\
        )")
    for file in fileList:
            if file.endswith(".txt"):
               cur.execute("INSERT INTO tbl_test2 (col_file) VALUES (?)", (file,)) 
               print(file)
    
    conn.commit()
# close connection to database
conn.close()

