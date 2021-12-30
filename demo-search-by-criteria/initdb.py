import sqlite3

conn = sqlite3.connect("reminders.sqlite")

cursor = conn.cursor()
query = "DROP TABLE IF EXISTS reminders"
cursor.execute(query)

cursor = conn.cursor()
query = """ CREATE TABLE reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    date DATE NOT NULL, 
    message TEXT NOT NULL, 
    done BOOLEAN NOT NULL 
)"""

cursor.execute(query)
conn.commit()
conn.close()
