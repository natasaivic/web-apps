import sqlite3

def db_connection():
    connection = None
    try:
        connection = sqlite3.connect("bookmarks_second.db")
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

def add_new_bookmark(label, url):
    sql = f"""
    INSERT INTO bookmarks_second (label, url, visited)
    VALUES ('{label}', '{url}', 0)
    """
    execute(sql)

def select_all_bookmarks(offset, limit):
    sql = f"""
    SELECT * FROM bookmarks_second 
    ORDER BY id ASC
    LIMIT {offset}, {limit} 
    """
    return query(sql)

def delete_bookmark(id):
    sql = f"""
    DELETE FROM bookmarks_second
    WHERE id={id}
    """
    execute(sql)

def max():
    sql = f"""
    SELECT COUNT(*)
    from bookmarks_second
    """
    return query(sql)
