import sqlite3


def db_connection():
    connection = None
    try:
        connection = sqlite3.connect("sorting-database.db")
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
    INSERT INTO bookmarks_sorting (label, url, visited)
    VALUES ('{label}', '{url}', 0)
    """
    execute(sql)


def select_all(sort_field, sort_order):
    sql = f"""
    SELECT * FROM bookmarks_sorting
    ORDER BY {sort_field} {sort_order}
    """
    return query(sql)

def delete_bookmark(id):
    sql = f"""
    DELETE FROM bookmarks_sorting
    WHERE id={id}
    """
    execute(sql)

def update_bookmark(id, label, url):
    sql = f"""
    UPDATE bookmarks_sorting
    SET label = '{label}', url = '{url}'
    WHERE id= {id}
    """
    execute(sql)

def select_bookmark(id):
    sql = f"""
    SELECT * FROM bookmarks_sorting
    WHERE id = {id}
    """
    return query(sql)
