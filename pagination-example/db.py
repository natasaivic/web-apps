import sqlite3
import math

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
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def query(sql):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def add_new_bookmark(label, url):
    sql = f"""
    INSERT INTO bookmarks (label, url, visited)
    VALUES ('{label}', '{url}', 0)
    """
    execute(sql)

def select_all(offset, size):
    sql = f"""
    SELECT * FROM bookmarks
    ORDER BY id ASC
    LIMIT {offset}, {size}
    """
    return query(sql)

def delete_bookmark(id):
    sql = f"""
    DELETE FROM bookmarks
    WHERE id={id}
    """
    execute(sql)


def number_of_pages(per_page = 5):
    sql = f"""
        SELECT COUNT(*)
        FROM bookmarks
    """
    result = query(sql)
    return math.ceil(result[0][0] / per_page)
