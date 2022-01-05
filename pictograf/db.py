import sqlite3

def connection_db():
    connection = None
    try:
        connection = sqlite3.connect("pictograf.db")
    except sqlite3.Error as e:
        print(e)
        exit(0)
    return connection


def execute(sql):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def query(sql):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def check_email_and_password(email, password):
    sql = f"""
    SELECT id 
    FROM registrar
    WHERE email='{email}' AND password='{password}'
    """
    result = query(sql)
    if len(result) == 0:
        return False
    return True

def check_email_in_registrar(email):
    sql = f"""
    SELECT id
    FROM registrar
    WHERE email='{email}'
    """
    result = query(sql)
    if len(result) == 0:
        return True
    return False

def get_user_id(email):
    sql = f"""
    SELECT id 
    FROM registrar
    WHERE email='{email}'
    """
    return query(sql)[0][0]

def get_user_first_name(email):
    sql = f"""
    SELECT name
    FROM registrar
    WHERE email='{email}'
    """
    return query(sql)[0][0]

def get_user_last_name(email):
    sql = f"""
    SELECT surname
    FROM registrar
    WHERE email='{email}'
    """
    return query(sql)[0][0]

def new_user_registration(name, surname, email, password):
    sql = f"""
    INSERT INTO registrar
    (name, surname, email, password)
    VALUES 
    ('{name}', '{surname}', '{email}', '{password}')
    """
    execute(sql)

def save_new_post(user_id, image_file, caption):
    sql = f"""
    INSERT INTO posts
    (user_id, image_file, caption, likes)
    VALUES 
    ('{user_id}', '{image_file}', '{caption}', 0)
    """
    execute(sql)

def get_posts_by_user(user_id):
    sql = f"""
    SELECT id, image_file, caption
    FROM posts
    WHERE user_id='{user_id}'
    """
    return query(sql)

