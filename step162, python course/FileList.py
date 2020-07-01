# Author        Derek Pruitt

# Python        3.8.3

# Assignment for school



file_List = ('information.docx','Hello.txt','myImage.png',\
             'myMovie.mpg','World.txt','data.pdf','myPhoto.jpeg')
for value in file_List:
    if value.endswith(".txt"):
        print(value)


        
import sqlite3

conn = sqlite3.connect('Step162.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_FileList(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_FileName TEXT, \
        col_Extension \
        )')


with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_FileList(col_FileName,col_Extension) VALUES(?,?)',\
                ('Hello','.txt'))
    cur.execute('INSERT INTO tbl_FileList(col_FileName,col_Extension) VALUES(?,?)',\
                ('World','.txt'))
    conn.commit()
conn.close()
