import sqlite3
import queries

def db_connection():
    connection = None
    try:
        connection = sqlite3.connect("pictogram.db")
    except sqlite3.Error as e:
        print(e)
        exit(0)
    return connection

def execute(sql):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(sql)

    conn.commit()

def query(sql):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(sql)

    return cur.fetchall()

def new_sign_up(email):
    query = queries.new_sign_up(email)
    execute(query)
