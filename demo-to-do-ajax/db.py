import sqlite3


def connection_db():
    connection = None
    try:
        connection = sqlite3.connect("to_do_ajax.db")
        connection.row_factory = sqlite3.Row
    except sqlite3.Error as e:
        print(e)
        exit(0)
    return connection


def execute(sql):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def execute_and_get_last_id(sql):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def query(sql):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def select_all_tasks():
    sql = f"""
    SELECT *
    FROM tasks
    """
    tasks = query(sql)
    print(tasks)
    return tasks


def save_new_task(task):
    sql = f"""
        INSERT INTO tasks
        (task)
        VALUES
        ('{task}')
    """
    try:
        return execute_and_get_last_id(sql)
    except:
        print(f"Error with query = {sql}")
        return None

def delete_task(id):
    sql = f"""
        DELETE FROM tasks
        WHERE id = {id}
    """
    return execute(sql)