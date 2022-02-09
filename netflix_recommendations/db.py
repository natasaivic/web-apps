import sqlite3
import random


def connection_db():
    connection = None
    try:
        connection = sqlite3.connect("database/showrec.db")
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


def get_newest_shows(limit):
    rand_offset = random.randint(0, 100)
    sql = f"""
    SELECT * 
    FROM shows
    ORDER BY release_year DESC
    LIMIT {rand_offset}, {limit}
    """
    shows = query(sql)
    return shows


def get_rand_shows(limit):
    rand_offset = random.randint(0, 2000)
    sql = f"""
    SELECT * 
    FROM shows
    WHERE id > {rand_offset}
    ORDER BY release_year DESC
    LIMIT {limit}
    """
    shows = query(sql)
    return shows


def get_show_data(id):
    sql = f"""
    SELECT *
    FROM shows
    WHERE id = {id}
    """
    show = query(sql)[0]
    print(show)
    return show


def get_similar_shows(id, limit):
    sql = f"""
    SELECT rec_ids 
    FROM recs 
    WHERE show_id = {id}
    LIMIT 1
    """
    result = query(sql)
    
    if len(result) == 0:
        return []
        
    similar_shows_ids = result[0]['rec_ids']
    sql = f"""
    SELECT * 
    FROM shows 
    WHERE id in ({similar_shows_ids})
    LIMIT {limit}
    """
    similar_shows = query(sql)
    return similar_shows


def get_all_shows():
    sql = f"""
    SELECT id, type, title, director, `cast`, release_year, listed_in, description
    FROM shows
    """
    shows = query(sql)
    return shows
