CREATE TABLE registrar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    image_file TEXT NOT NULL,
    caption TEXT NOT NULL,
    likes INTEGER DEFAULT 0,
    create_on TEXT NOT NULL
);

