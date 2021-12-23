import sqlite3
import queries

def db_connection():
    connection = None
    try:
        connection = sqlite3.connect("reminders.sqlite")
    except sqlite3.error as e:
        print(e)
    return connection

def get_reminders():
    conn = db_connection()
    cursor = conn.cursor()
    query = queries.select_reminders()
    cursor.execute(query)
    
    return cursor.fetchall()

def get_by_searchword(searchword):
    conn = db_connection()
    cursor = conn.cursor()
    query = queries.select_by_searchword(searchword)
    cursor.execute(query) 
    return cursor.fetchall()

def add_reminder(date, message):
    conn = db_connection()
    cursor = conn.cursor()
    query = queries.insert_reminder(date, message)
    cursor.execute(query)
    conn.commit()

def delete_reminder(reminder_id):
    conn = db_connection()
    cursor = conn.cursor()
    query = queries.delete_reminder(reminder_id)
    cursor.execute(query)
    conn.commit()

def edit_reminder(reminder_id):
    conn = db_connection()
    cursor = conn.cursor()
    query = queries.edit_reminder(reminder_id)
    cursor.execute(query)
    
    return cursor.fetchall()

def edit_reminder_2(reminder_id, date, message):
    conn = db_connection()
    cursor = conn.cursor()
    query = queries.edit_reminder_2(reminder_id, date, message)
    cursor.execute(query)
    conn.commit()
    