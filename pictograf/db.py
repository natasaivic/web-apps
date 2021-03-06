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

def update_new_password(id, new_password):
    sql = f"""
    UPDATE registrar
    SET password = '{new_password}'
    WHERE id = '{id}'
    """
    execute(sql)

def match_old_password(id, old_password):
    sql = f"""
    SELECT password
    FROM registrar
    WHERE id = {id}
    """
    result =  query(sql)
    print(result)
    if result[0][0] == old_password:
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

def get_user_profile_pic(email):
    sql = f"""
    SELECT profile_pic
    FROM registrar
    WHERE email='{email}'
    """
    return query(sql)[0][0]

def get_profile_first_name(user_id):
    sql = f"""
    SELECT name
    FROM registrar
    WHERE id='{user_id}'
    """
    return query(sql)[0][0]

def get_profile_last_name(user_id):
    sql = f"""
    SELECT surname
    FROM registrar
    WHERE id='{user_id}'
    """
    return query(sql)[0][0]

def get_profile_profile_pic(user_id):
    sql = f"""
    SELECT profile_pic
    FROM registrar
    WHERE id='{user_id}'
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

def save_new_post(user_id, image_file, caption, create_on):
    sql = f"""
    INSERT INTO posts
    (user_id, image_file, caption, likes, create_on)
    VALUES 
    ('{user_id}', '{image_file}', '{caption}', 0, '{create_on}')
    """
    execute(sql)

def get_posts_by_user(user_id):
    sql = f"""
    SELECT id, image_file, caption, create_on
    FROM posts
    WHERE user_id='{user_id}'
    ORDER BY id DESC
    """
    return query(sql)

def get_latest_posts():
    sql = """
    SELECT user_id, image_file, caption, create_on, profile_pic, posts.id
    FROM posts LEFT JOIN registrar AS users ON users.id = posts.user_id
    ORDER BY posts.id DESC
    LIMIT 10
    """
    result = query(sql)
    return result

def update_profile_pic(id, file_name):
    sql = f"""
    UPDATE registrar
    SET profile_pic = '{file_name}'
    WHERE id = '{id}'
    """
    execute(sql)

def save_info(user_id, current_city, hometown, bio):
    sql = f"""
    INSERT INTO personal_info
    (user_id, current_city, hometown, bio)
    VALUES
    ('{user_id}', '{current_city}', '{hometown}', '{bio}')
    """
    execute(sql)

def get_info_by_user(user_id):
    sql = f"""
    SELECT current_city, hometown, bio
    FROM personal_info
    WHERE user_id = {user_id}
    ORDER BY id DESC
    LIMIT 1
    """
    result = query(sql)

    if len(result) == 0:
        return ["n/a", "n/a", "n/a"]
    return result[0]

def save_new_comment(user_id, post_id, comment, created_on):
    sql = f"""
    INSERT INTO comments
    (user_id, post_id, comment, created_on)
    VALUES 
    ('{user_id}', '{post_id}', '{comment}', '{created_on}')
    """
    execute(sql)

def get_comments_by_post(post_id):
    sql = f"""
    SELECT id, user_id, comment, created_on
    FROM comments 
    WHERE post_id='{post_id}'
    """
    result = query(sql)
    return result

def get_likes_by_post(post_id):
    sql = f"""
    SELECT COUNT(*)
    FROM likes 
    WHERE post_id='{post_id}'
    """
    result = query(sql)
    return result[0][0]

def delete_comment(id):
    sql = f"""
    DELETE FROM comments
    WHERE id={id}
    """
    execute(sql)

def remove_post(post_id):
    sql = f"""
    DELETE FROM posts
    WHERE id={post_id}
    """
    execute(sql)

def remove_comments(post_id):
    sql = f"""
    DELETE FROM comments
    WHERE post_id = {post_id}
    """
    execute(sql)

def remove_likes(post_id):
    sql = f"""
    DELETE FROM likes
    WHERE post_id = {post_id}
    """
    execute(sql)

def check_like(user_id, post_id):
    sql = f"""
    SELECT COUNT(*) 
    FROM likes
    WHERE user_id = {user_id}
    AND post_id = {post_id}
    """
    result = query(sql)
    if result[0][0] == 0:
        return False
    return True

def add_like(user_id, post_id):
    sql = f"""
    INSERT INTO likes
    (user_id, post_id)
    VALUES
    ('{user_id}', '{post_id}')
    """
    execute(sql)

def remove_like(user_id, post_id):
    sql = f"""
    DELETE FROM likes
    WHERE user_id = '{user_id}' AND post_id = '{post_id}'
    """
    execute(sql)
