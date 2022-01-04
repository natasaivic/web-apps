import sqlite3

def connect():
    connection = None
    try:
        connection = sqlite3.connect("bookmarks-session.db")
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

def add_bookmark(user_id, label, url, create_on):
    sql = f"""
        INSERT INTO bookmarks (user_id, label, url, visited, create_on)
        VALUES ('{user_id}', '{label}', '{url}', 0, '{create_on}')
    """
    execute(sql)

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

def check_email_and_password(email, password):
    sql = f"""
    SELECT id 
    FROM users
    WHERE email='{email}' AND password='{password}'
    """
    result = query(sql)
    if len(result) == 0:
        return False
    return True

def get_user_id(email):
    sql = f"""
    SELECT id 
    FROM users
    WHERE email='{email}'
    """
    result = query(sql)
    print(result)
    return result[0][0]

def check_registar(email):
    sql = f"""
    SELECT id
    FROM users
    WHERE email='{email}'
    """
    result = query(sql)
    if len(result) != 0:
        return False
    return True

def register_user(email, password):
    sql = f"""
        INSERT INTO users
        (email, password)
        VALUES
        ('{email}', '{password}')
    """
    execute(sql)

def get_bookmarks_by_user(user_id):
    sql = f"""
    SELECT id, label, url, create_on
    FROM bookmarks
    WHERE user_id = {user_id}
    """
    return query(sql)

def get_latest_bookmarks():
    sql = """
        SELECT user_id, label, create_on 
        FROM bookmarks
        ORDER BY id DESC
        LIMIT 10
    """
    result = query(sql)
    return result