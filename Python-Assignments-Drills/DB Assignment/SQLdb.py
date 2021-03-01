import sqlite3

conn = sqlite3.connect('test1.db') #CONNECT to db

with conn:
    cur = conn.cursor()                                     #BELOW IS SQL STATEMENT (NOT PYTHON); create a table if it doesn't exist already
    cur.execute("CREATE TABLE IF NOT EXISTS tblFiles(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_txt TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
#CREATE TUPLE
    fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt', \
            'data.pdf','myPhoto.jpg')

#ITERATE to find .txt, add to db, and print
    for f in fileList:
        if f.endswith(".txt"):
            cur.execute("INSERT INTO tblFiles(col_txt) VALUES (?)", (f,)) #trailing comma for tuple
            print(f)
conn.close()
    

