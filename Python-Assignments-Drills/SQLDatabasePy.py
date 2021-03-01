
##copied from folder A in local C:\\
import sqlite3

conn = sqlite3.connect('test.db') #CONNECT TO DB

with conn:
    cur = conn.cursor()                                     #SQL STATEMENT (NOT PYTHON); create a table if it doesn't exist already
    cur.execute("CREATE TABLE IF NOT EXISTS table_persons(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()                                                             #? for wildcare--3 columns
    cur.execute("INSERT INTO table_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Bob','Smith','bsmith@gmail.com'))
    cur.execute("INSERT INTO table_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sarah','Jones','sjones@gmail.com'))
    cur.execute("INSERT INTO table_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sally','Mae','salmae@gmail.com'))
    cur.execute("INSERT INTO table_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Kevin','Bacon','baconator@gmail.com'))
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()                                                             
    cur.execute("SELECT col_fname, col_lname, col_email FROM table_persons WHERE col_fname = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name; {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)
    















    

