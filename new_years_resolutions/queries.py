from sqlite3 import dbapi2

import db

def create_table():
    sql = """
    CREATE TABLE reminders_2022 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        message TEXT NOT NULL,
        done BOOLEAN NOT NULL
    )"""
    return sql

def select_all_reminders():
    sql = """
        SELECT id, date, message, done
        FROM reminders_2022
        ORDER BY date ASC
    """
    return db.query(sql)

def insert_reminder(date, message):
    sql = f"""
    INSERT INTO reminders_2022 (date, message, done) VALUES ('{date}','{message}', '0')
    """
    return db.execute(sql)

def verify_db_setup():
    sql = """
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' AND name='reminders_2022'
    """
    result = db.query(sql)
    if len(result) == 0:
        return False
        
    if result[0][0] == 'reminders_2022':
        return True
    return False

def delete_reminder(id):
    sql = f"""
    DELETE FROM reminders_2022
    WHERE id={id}
    """
    return db.execute(sql)

def select_reminder(id):
    sql = f"""
        SELECT id, date, message
        FROM reminders_2022
        WHERE id = {id}
    """
    return db.query(sql)

def update_database(id, date, message):
    sql = f"""
    UPDATE reminders_2022
    SET date='{date}', message='{message}'
    WHERE id={id}
    """
    return db.execute(sql)

    