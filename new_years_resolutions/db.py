import sqlite3

def connect():
    connection = None
    try:
        connection = sqlite3.connect("reminders.db")
    except sqlite3.Error as e:
        print(e)
        exit(0)
    
    return connection


def execute(sql):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def query(sql):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    
    return cur.fetchall()

