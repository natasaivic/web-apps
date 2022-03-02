import sqlite3

def connection_db():
    connection = None
    try:
        connection = sqlite3.connect("to_do.db")
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

def get_all_tasks():
    sql = f"""
    SELECT id, task, done 
    FROM tasks
    """
    return query(sql)[0][0]

def save_new_task(task, done):
    sql = f"""
    INSERT INTO tasks
    (task, done)
    VALUES 
    ('{task}', '{done}')
    """
    try:
        execute(sql)
        return True 
    except:
        print(f"Error with query = '{sql}'")
        return False