import sqlite3
import math

def connect():
    connection = None
    try:
        connection = sqlite3.connect("posts.db")
    except sqlite3.Error as e:
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

# Check login function
# return True if login is valid, otherwise return False
def check_loging(email, password):
    sql = f"""
        SELECT id
        FROM users
        WHERE email='{email}'
        AND password='{password}'
        AND active = 1
    """
    result = query(sql)
    if len(result) == 0:
        return False

    return True

def calc_offset(per_page, current_page):
    if current_page <= 1:
        return 0
    
    return (current_page - 1) * per_page

def get_feed_items(order, page):
    per_page = 5
    offset = calc_offset(per_page, page)

    sql = f"""
        SELECT image_path, caption
        FROM posts
        ORDER BY id {order}
        LIMIT {offset}, {per_page}
    """
    result = query(sql)
    return result

def get_number_of_pages(per_page = 5):
    sql = f"""
        SELECT COUNT(*)
        FROM posts
    """
    result = query(sql)
    return math.ceil(result[0][0] / per_page)