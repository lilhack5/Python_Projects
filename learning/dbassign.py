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


with conn:
    cur = conn.cursor()
    # create table for test2 database
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_test2( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT\
        )")
    conn.commit()
# close connection to database
conn.close()

conn = sqlite3.connect('text2.db')

# add data into tbl_test2
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_test2(col_file) VALUES (?)", \
                ('information.docx'))
    cur.execute("INSERT INTO tbl_test2(col_file) VALUES (?)", \
                ('Hello.txt'))
    cur.execute("INSERT INTO tbl_test2(col_file) VALUES (?)", \
                ('myImage.png'))
    cur.execute("INSERT INTO tbl_test2(col_file) VALUES (?)", \
                ('myMovies.mpg'))
    cur.execute("INSERT INTO tbl_test2(col_file) VALUES (?)", \
                ('World.txt'))
    cur.execute("INSERT INTO tbl_test2(col_file) VALUES (?)", \
                ('data.pdf'))
    cur.execute("INSERT INTO tbl_test2(col_file) VALUES (?)", \
                ('myPhoto.jpg'))
    conn.commit()
conn.close()

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file WHERE col_file = '.txt'")
    varType = cur.fetchall()
    for item in varType:
        msg = "File: {}".format(item[0])
    print(msg)
