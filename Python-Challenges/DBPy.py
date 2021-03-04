
import sqlite3
connection = sqlite3.connect(':memory:')

rosterValues=(('Jean-Baptist Zorg', 'Human', 22), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalor', -5))

with sqlite3.connect('Roster.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?,?,?)", rosterValues)

    #UPDATE Species of Korben Dallas to Human
    c.execute("UPDATE Roster SET Species='Human' WHERE Species='Meat Popsicle'")

    #DISPLAY names and IQs of everyone classified as human
    c.execute("SELECT Name, IQ from Roster WHERE Species='Human'")
    for row in c.fetchall():
        print(row)

connection.close()
    
    
