CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id TEXT NOT NULL,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    rating REAL NOT NULL,
    description TEXT NOT NULL,
    genres TEXT NOT NULL,
    characters TEXT NOT NULL,
    pages INTEGER NOT NULL,
    publisher TEXT NOT NULL,
    publishDate TEXT NOT NULL,
    awards TEXT NOT NULL,
    numRatings INTEGER NOT NULL,
    coverImg TEXT NOT NULL
);

CREATE TABLE books_import (
    book_id TEXT,
    title TEXT,
    series TEXT,
    author TEXT,
    rating REAL,
    description TEXT,
    language TEXT,
    isbn TEXT,
    genres TEXT,
    characters TEXT,
    bookFormat TEXT,
    edition TEXT,
    pages INTEGER,
    publisher TEXT,
    publishDate TEXT,
    firstPublishDate TEXT,
    awards TEXT,
    numRatings INTEGER,
    ratingsByStars TEXT,
    likedPercent INTEGER,
    setting TEXT,
    coverImg TEXT,
    bbeScore INTEGER,
    bbeVotes INTEGER,
    price REAL
);

-- drop table books_import;
-- .mode csv
-- .import backup/bestbooks.csv books_import

-- INSERT INTO books SELECT null, book_id, title, author, rating, description, genres, characters, pages, publisher, publishDate, awards, numRatings, coverImg FROM books_import WHERE language = 'English';

CREATE TABLE recs (
    book_id TEXT NOT NULL,
    rec_ids TEXT NOT NULL
);