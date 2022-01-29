PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE registrar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
, profile_pic TEXT);
INSERT INTO registrar VALUES(1,'Natasa','Ivic','ivicsnatasa@gmail.com','4779164ef68a662cb1006d6fa3171914','1.jpg');
INSERT INTO registrar VALUES(2,'Vladimir','Ivic','vlada.ivic@gmail.com','202cb962ac59075b964b07152d234b70',NULL);
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    image_file TEXT NOT NULL,
    caption TEXT NOT NULL,
    likes INTEGER DEFAULT 0,
    create_on TEXT NOT NULL
);
INSERT INTO posts VALUES(1,1,'93f5e59a6e78235753c1770ffd0376a2.jpg','First time at Yosemite National Park with him, at Lower Yosemite Fall trail. <3',0,'Tuesday, January 04. 2022 at 22:33');
INSERT INTO posts VALUES(2,1,'36aa3ead81f6d31d88f7046e9923238a.jpg','Love of my life. <3',0,'Tuesday, January 04. 2022 at 22:38');
INSERT INTO posts VALUES(3,1,'523c107236870f25363825d50da173ee.jpg','At Yosemite <3',0,'Tuesday, January 04. 2022 at 22:42');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('registrar',2);
INSERT INTO sqlite_sequence VALUES('posts',3);
COMMIT;

CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    created_on TEXT NOT NULL
);

CREATE TABLE personal_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    current_city TEXT NOT NULL,
    hometown TEXT NOT NULL,
    bio TEXT NOT NULL
);

CREATE TABLE likes (
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL
);