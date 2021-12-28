import sqlite3

def connect():
    connection = None
    try:
        connection = sqlite3.connect("users.db")
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

def check_existing_email(email):
    """Will return true if email is exsting"""
    sql = f"""
        SELECT id
        FROM users
        WHERE email='{email}'
    """
    result = query(sql)
    return len(result) > 0

def create_new_user_account(firstname, surname, email, password):
    """Creates a new user in the users table"""
    sql = f"""
        INSERT INTO users
        (firstname, surname, email, password)
        VALUES
        ('{firstname}', '{surname}', '{email}', '{password}')
    """
    execute(sql)