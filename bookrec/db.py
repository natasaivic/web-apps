import sqlite3
import random


def connection_db():
    connection = None
    try:
        connection = sqlite3.connect("database/bookrec.db")
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


def get_top_books(limit):
    rand_offset = random.randint(0, 100)
    sql = f"""
        select *  
        from books 
        order by numRatings desc 
        limit {rand_offset}, {limit}
    """
    books = query(sql)
    return books


def get_rand_books(limit):
    rand_offset = random.randint(0, 42000)
    sql = f"""
        select * 
        from books 
        where id > {rand_offset} 
        limit {limit}
    """
    books = query(sql)
    return books


def get_book_info(book_id):
    sql = f"""
        select * 
        from books 
        where id = {book_id}
    """
    book = query(sql)[0]
    return book


def get_similar_books(book_id, limit):
    sql = f"""
        select rec_ids 
        from recs 
        where book_id = {book_id}
        limit 1
    """
    result = query(sql)
    if len(result) == 0:
        return []
    similar_book_ids = result[0]['rec_ids']
    sql = f"""
        select * 
        from books 
        where id in ({similar_book_ids})
        limit {limit}
    """
    similar_books = query(sql)
    return similar_books


def get_all_books(limit=50000):
    sql = f"""
        select id, title, description, rating, pages, numRatings 
        from books 
        limit {limit}
    """
    books = query(sql)
    return books


def search_books(search_query, limit):
    sql = f"""
        select * 
        from books 
        where title like '%{search_query}%'
        order by numRatings desc 
        limit {limit}
    """
    results = query(sql)
    if len(results) == 0:
        return []

    return results

