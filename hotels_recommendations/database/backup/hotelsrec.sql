CREATE TABLE hotels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_id TEXT NOT NULL,
    city TEXT NOT NULL,
    name TEXT NOT NULL,
    province TEXT NOT NULL,
    reviews_rating INTEGER NOT NULL,
    reviews_text TEXT NOT NULL,
    reviews_title TEXT NOT NULL,
    websites TEXT NOT NULL
);

CREATE TABLE hotels_import (
    hotel_id TEXT,
    dateAdded TEXT,
    dateUpdated TEXT,
    address TEXT,
    categories TEXT,
    primaryCategories TEXT,
    city TEXT,
    country TEXT,
    keys TEXT,
    latitude INTEGER,
    longitude INTEGER,
    name TEXT,
    postalCode TEXT,
    province TEXT,
    reviews_date TEXT,
    reviews_dateSeen TEXT,
    reviews_rating INTEGER,
    reviews_sourceURLs TEXT,
    reviews_text TEXT,
    reviews_title TEXT,
    reviews_userCity TEXT,
    reviews_userProvince TEXT,
    reviews_username TEXT,
    sourceURLs TEXT,
    websites TEXT
);

-- drop table hotels_import;
-- .mode csv
-- .import database/hotel_reviews.csv hotels_import
-- insert into hotels select NULL, hotel_id, city, name, province, reviews_rating, reviews_text, reviews_title, websites from hotels_import;
