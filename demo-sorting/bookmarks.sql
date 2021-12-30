CREATE TABLE bookmarks (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    label TEXT NOT NULL,
    url_ TEXT NOT NULL,
    visited INTEGER NOT NULL
);


INSERT INTO
  bookmarks (label, url_, visited = 0)
VALUES
  (
    "Jinja Templates",
    "https://jinja.palletsprojects.com/en/3.0.x/templates/"
  ), 
  (
      "MySQL Documentation",
      "https://dev.mysql.com/doc/"
  ),
  (
      "CSS",
      "https://www.w3.org/Style/CSS/"
  );