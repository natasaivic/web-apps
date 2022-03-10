import sqlite3
import random

def connection_db():
    connection = None
    try:
        connection = sqlite3.connect("database/hotelrec.db")
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

def query(sql):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def get_best_rated_hotels(limit):
    rand_offset = random.randint(0,200)
    sql = f"""
    SELECT *
    FROM hotels
    ORDER BY reviews_rating DESC
    LIMIT {rand_offset}, {limit}
    """
    hotels = query(sql)
    print(hotels)
    return hotels

def get_random_hotels(limit):
    rand_offset = random.randint(0,2000)
    sql = f"""
    SELECT *
    FROM hotels
    WHERE id > {rand_offset}
    ORDER BY reviews_rating DESC
    LIMIT {limit}
    """
    hotels = query(sql)
    print(hotels)
    return hotels

def get_all_hotels():
    sql = f"""
    SELECT *
    FROM shows
    """
    hotels = query(sql)
    return hotels
    