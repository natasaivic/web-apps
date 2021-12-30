import sqlite3

def db_connection():
    connection = None
    try:
        connection = sqlite3.connect("bookmarks.db")
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

def add_bookmark(label, url):
    sql = f"""
    INSERT INTO bookmarks (label, url_, visited)
    VALUES ('{label}', '{url}', 0)
    """
    execute(sql)

def list_all(sort_field, sort_order):
    sql = f"""
    SELECT * 
    FROM bookmarks
    ORDER BY {sort_field} {sort_order}
    """
    return query(sql)

