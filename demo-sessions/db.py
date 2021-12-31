import sqlite3

def connect():
    connection = None
    try:
        connection = sqlite3.connect("tweets.db")
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
    """
    result = query(sql)
    if len(result) == 0:
        return False
    return True

def register_user(email, password):
    """Creates a new user in the users table"""
    sql = f"""
        INSERT INTO users
        (email, password)
        VALUES
        ('{email}', '{password}')
    """
    execute(sql)

def get_user_id(email):
    sql = f"""
        SELECT id
        FROM users
        WHERE email='{email}'
    """
    result = query(sql)
    return result[0][0]

def get_tweets_by_user(user_id):
    sql = f"""
        SELECT tweet, create_on
        FROM tweets
        WHERE user_id='{user_id}'
        ORDER BY id DESC
    """
    result = query(sql)
    return result

def create_new_tweet(user_id, tweet, create_on):
    sql = f"""
        INSERT INTO tweets
        (user_id, tweet, create_on)
        VALUES
        ({user_id}, '{tweet}', '{create_on}')
    """
    execute(sql)

def get_latest_tweets():
    sql = f"""
        SELECT tweet, create_on, user_id
        FROM tweets
        ORDER BY id DESC
        LIMIT 10
    """
    result = query(sql)
    return result