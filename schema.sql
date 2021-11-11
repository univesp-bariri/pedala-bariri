DROP TABLE IF EXISTS postsgastro;
DROP TABLE IF EXISTS postscultura;
DROP TABLE IF EXISTS postsrural;

CREATE TABLE postsgastro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE postscultural (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE postsrural (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
