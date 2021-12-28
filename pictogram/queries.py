def users():
    sql = """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL
    )
    """
    return sql

def new_sign_up(email):
    sql = f"""
    INSERT INTO users 
        (email) 
    VALUES 
        ("{email}")
    """
    return sql

