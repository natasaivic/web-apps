import sqlite3
import queries

# napravi konekciju sa bazom
def db_connection():
    connection = None
    try:
        connection = sqlite3.connect("quotes.db")
        print("Opened database successfully")
    except sqlite3.Error as e:
        print(e)
        exit(0)
    return connection

# conn = db_connection()
# conn.execute('CREATE TABLE quotes (id INTEGER PRIMARY KEY AUTOINCREMENT, author TEXT NOT NULL, quote TEXT NOT NULL)')
# conn.close()

# select all quotes
def get_all_quotes():
    conn = db_connection()
    cur = conn.cursor()
    query = queries.select_all_quotes()
    cur.execute(query)
    return cur.fetchall()

# add quotes
def add_quote(author, quote):
    conn = db_connection()
    cur = conn.cursor()
    query = queries.insert_new_quote(author, quote)
    cur.execute(query)
    conn.commit()

def delete_quote(id):
    conn = db_connection()
    cur = conn.cursor()
    query = queries.delete_quote(id)
    cur.execute(query)
    conn.commit()

def select_quote(id):
    conn = db_connection()
    cur = conn.cursor()
    query = queries.select_quote(id)
    cur.execute(query)
    return cur.fetchall()

def select_by_searchword(searchword):
    conn = db_connection()
    cur = conn.cursor()
    query = queries.select_by_searchword(searchword)
    cur.execute(query)
    return cur.fetchall()

def update_quote(id, author, quote):
    conn = db_connection()
    cur = conn.cursor()
    query = queries.update_quote(id, author, quote)
    cur.execute(query)
    conn.commit()
    

