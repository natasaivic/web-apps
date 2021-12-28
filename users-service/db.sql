CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstname TEXT NOT NULL,
  surname TEXT NOT NULL,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  active INTEGER DEFAULT 1 NOT NULL
);

-- INSERT INTO users (firstname, surname, email, password, active)
-- VALUES ('Natasa', 'Ivic', 'nata@bettertutor.org', '2ecface7be4ff3017ac0989971fb7e69', 1);