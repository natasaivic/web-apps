PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
id INTEGER primary key autoincrement,
email TEXT NOT NULL,
password TEXT NOT NULL);
INSERT INTO users VALUES(1,'nata@bettertutor.org','2ecface7be4ff3017ac0989971fb7e69');
INSERT INTO users VALUES(2,'vlada.ivic@gmail.com','ba0df2e9424399e91c96ae3dec31a65a');
CREATE TABLE tweets (
id integer primary key autoincrement,
user_id integer not null,
tweet text not null,
create_on text not null);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('users',2);
COMMIT;
