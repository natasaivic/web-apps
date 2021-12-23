def create_table():
    sql = """
    CREATE TABLE quotes
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT NOT NULL,
    quote TEXT NOT NULL
    )"""
    return sql

def select_all_quotes():
    sql = """
    SELECT id, author, quote
    FROM quotes
    ORDER BY author ASC
    """
    return sql

def insert_new_quote(author, quote):
    sql = f"""
    INSERT INTO quotes
    (author, quote) VALUES ('{author}', '{quote}')
    """
    return sql

def delete_quote(id):
    sql = f"""
    DELETE FROM quotes
    WHERE id={id}
    """
    return sql

def select_quote(id):
    sql = f"""
    SELECT id, author, quote
    FROM quotes
    WHERE id={id}
    """
    return sql

def select_by_searchword(searchword):
    sql = f"""
    SELECT id, author, quote
    FROM quotes
    WHERE quote LIKE '%{searchword}%'
    """
    return sql

def update_quote(id, author, quote):
    author = author.replace("'", "''")
    quote = quote.replace("'", "''")
    sql = f"""
    UPDATE quotes
    SET author='{author}', quote='{quote}'
    WHERE id={id}
    """
    return sql