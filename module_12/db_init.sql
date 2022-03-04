DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;

CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    author VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
    REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
    REFERENCES user(user_id)
);

INSERT INTO book(book_id, book_name, details, author) VALUES (1, 'A Game of Thrones', 'The first part of the game of thrones', 'George R. R. Martin');
INSERT INTO book(book_id, book_name, details, author) VALUES (2, 'A Clash of Kings', 'The second part of the game of thrones', 'George R. R. Martin');
INSERT INTO book(book_id, book_name, details, author) VALUES (3, 'A Storm of Swords', 'The third part of the game of thrones', 'George R. R. Martin');
INSERT INTO book(book_id, book_name, details, author) VALUES (4, 'A Feast for Crows', 'The fourth part of the game of thrones', 'George R. R. Martin');
INSERT INTO book(book_id, book_name, details, author) VALUES (5, 'A Dance with Dragons', 'The fifth part of the game of thrones', 'George R. R. Martin');
INSERT INTO book(book_id, book_name, details, author) VALUES (7, 'The Hobbit, or There and Back Again', 'Part of the Lord of the Rings', 'George R. R. Martin');
INSERT INTO book(book_id, book_name, details, author) VALUES (8, 'The Fellowship of the Ring', 'Part one of the Lord of the Rings', 'George R. R. Martin');
INSERT INTO book(book_id, book_name, details, author) VALUES (9, 'The Two Towers', 'Part two of the Lord of the Rings', 'George R. R. Martin');
INSERT INTO book(book_id, book_name, details, author) VALUES (9, 'The Return of the King', 'Part three of the Lord of the Rings', 'George R. R. Martin');

INSERT INTO store(store_id, locale) VALUES (1, '1000 Galvin Rd S, Bellevue, NE 68005');

INSERT INTO user(user_id, first_name, last_name) VALUES (1, 'Jon', 'Hunt');
INSERT INTO user(user_id, first_name, last_name) VALUES (1, 'Joe', 'Burrow');
INSERT INTO user(user_id, first_name, last_name) VALUES (1, 'Tee', 'Higgins');

INSERT INTO wishlist(wishlist_id, user_id, book_id) VALUES (2, 1, 2);
INSERT INTO wishlist(wishlist_id, user_id, book_id) VALUES (3, 2, 9);
INSERT INTO wishlist(wishlist_id, user_id, book_id) VALUES (4, 3, 6);

