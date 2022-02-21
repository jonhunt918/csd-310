import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (1, 'A Game of Thrones', 'The first part of the game of thrones', 'George R. R. Martin')")
    cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (2, 'A Clash of Kings', 'The second part of the game of thrones', 'George R. R. Martin')")
    cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (3, 'A Storm of Swords', 'The third part of the game of thrones', 'George R. R. Martin')")
    cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (4, 'A Feast for Crows', 'The fourth part of the game of thrones', 'George R. R. Martin')")
    cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (5, 'A Dance with Dragons', 'The fifth part of the game of thrones', 'George R. R. Martin')")
    cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (7, 'The Hobbit, or There and Back Again', 'Part of the Lord of the Rings', 'George R. R. Martin')")
    cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (8, 'The Fellowship of the Ring', 'Part one of the Lord of the Rings', 'George R. R. Martin')")
    cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (9, 'The Two Towers', 'Part two of the Lord of the Rings', 'George R. R. Martin')")
    cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (9, 'The Return of the King', 'Part three of the Lord of the Rings', 'George R. R. Martin')")

    book = cursor.fetchall()

    cursor.execute("INSERT INTO store(store_id, locale) VALUES (1, '1000 Galvin Rd S, Bellevue, NE 68005')")

    store = cursor.fetchall()

    cursor.execute("INSERT INTO user(user_id, first_name, last_name) VALUES (1, 'Jon', 'Hunt')")
    cursor.execute("INSERT INTO user(user_id, first_name, last_name) VALUES (1, 'Joe', 'Burrow')")
    cursor.execute("INSERT INTO user(user_id, first_name, last_name) VALUES (1, 'Tee', 'Higgins')")

    user = cursor.fetchall()

    cursor.execute("INSERT INTO wishlist(wishlist_id, user_id, book_id) VALUES (2, 1, 2")
    cursor.execute("INSERT INTO wishlist(wishlist_id, user_id, book_id) VALUES (3, 2, 9")
    cursor.execute("INSERT INTO wishlist(wishlist_id, user_id, book_id) VALUES (4, 3, 6")

    wishlist = cursor.fetchall()




except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_denied_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
