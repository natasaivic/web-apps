import sqlite3

def connect():
    connection = None
    try:
        connection = sqlite3.connect("bookmarks.db")
    except sqlite3.error as e:
        print(e)
        exit(0)
    return connection

def execute(sql):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def query(sql):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()    

def add_bookmark(label, url):
    sql = f"""
        INSERT INTO bookmarks (label, url, visited)
        VALUES ('{label}', '{url}', 0)
    """
    execute(sql)

def get_all():
    sql = """
        SELECT id, label, url, visited
        FROM bookmarks
        ORDER BY id DESC
    """
    return query(sql)

def get_by_searchword(searchword):
    sql = f"""
        SELECT id, label, url, visited
        FROM bookmarks
        WHERE label LIKE '%{searchword}%' OR url LIKE '%{searchword}%'
        ORDER BY id DESC
    """
    return query(sql)

def delete_bookmark(id):
    sql = f"""
        DELETE FROM bookmarks
        WHERE id = {id}
    """
    execute(sql)

def mark_as_visited(id):
    sql = f"""
        UPDATE bookmarks
        SET visited = 1
        WHERE id = {id}
    """
    execute(sql)

def mark_as_unvisited(id):
    sql = f"""
        UPDATE bookmarks
        SET visited = 0
        WHERE id = {id}
    """
    execute(sql)

def to_be_edited(id):
    sql = f"""
    SELECT label, url
    FROM `bookmarks`
    WHERE id = {id}
    """
    return query(sql)

def edited_bookmark(id, label, url):
    sql = f"""
    UPDATE `bookmarks`
    SET label = '{label}', url = '{url}'
    WHERE id = {id}
    """
    execute(sql)