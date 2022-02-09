CREATE TABLE shows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    show_id TEXT NOT NULL,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    director TEXT NOT NULL,
    cast TEXT NOT NULL,
    release_year INTEGER NOT NULL,
    listed_in TEXT NOT NULL,
    description TEXT NOT NULL
);


CREATE TABLE shows_import (
    show_id TEXT,
    type TEXT,
    title TEXT,
    director TEXT,
    cast TEXT,
    country TEXT,
    date_added DATE,
    release_year INTEGER,
    rating TEXT,
    duration TEXT,
    listed_in TEXT,
    description TEXT
);

-- drop table shows_import;
-- .mode csv
-- .import database/netflix_shows.csv shows_import
-- insert into shows select NULL, show_id, type, title, director, `cast`, release_year, listed_in, description from shows_import;

CREATE TABLE recs (
    show_id TEXT NOT NULL,
    rec_ids TEXT NOT NULL
);
