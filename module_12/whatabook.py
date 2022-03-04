import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

"""Show Main Menu Method"""
def show_menu():
    print("\n Whatabook Main Menu ")

    print("\n 1. View Books\n  2. View Store Locations\n  3. View My Account\n 4. Exit Program")

    try:
        menu_id = int(input(" Please choose a number from the menu such as 1 for View Books "))

        return menu_id

    except ValueError: 
        print(" Sorry, the number you entered is not a choice in the menu, closing the program")

        sys.exit(0)
    
"""Method to Display the List of Available Books""" 
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, details, author FROM book")
    
    books = _cursor.fetchall()
    
    print("\n The following is a list of our currently available books ")

    for book in books:
        print("\n\n Book ID: {} Book Name: {} Book Details: {} Book Author: {}".format(book[0], book[1], book[2], book[3]))

"""Method to Display the one location that Whatabook operates from"""
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale FROM store")

    stores = _cursor.fetchall()

    print("\n Displaying our current store locations ")

    for store in stores:
        print("\n\n Store ID: {}\n Store Locale: {}\n ".format(store[0], store[1])) 

"""Method to Validate the user by entering a User ID and will close program if an incorrect User ID in inputted"""
def validate_user():
    
    try:
        user_id = int(input(" Please choose from User ID 1, 2, or 3"))

        if user_id < 0 or user_id > 3:
            print("Sorry, that User ID has not been created yet, closing the program")
        
        return user_id
    
    except ValueError:
        print("Sorry, that User ID does not exist, closing the program")

    sys.exit(0)

"""Method to Display account menu and allow three choices for the user to either view their wishlist, add a book, or go back to the main menu"""
def show_account_menu():

    try:
        print(" Displaying account menu ")
        print(" 1. User Wishlist\n     2. Add Book\n    3. Main Menu ")
        choice = int(input(" Please make a selection from the account menu such as 1 to view User Wishlist "))

        return choice
    
    except ValueError: 
        print("Sorry, the number you entered does not have a corresponding option, closing the program ")

        sys.exit(0)

"""Method to show the user's wishlist"""
def show_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + "FROM wishlist " + "INNER JOIN user ON wishlist.user_id = user.user_id " + "INNER JOIN book ON wishlist.book_id = book.book_id" + "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()

    print("\n Displaying items in user's wishlist")

    for book in wishlist:
        print("\n\n Book Name: {}\n Author: {}\n ".format(book[4], book[5]))

"""Method to display books that are not currently in the wishlist and are available to be added to the wishlist"""
def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, details, author  " + "FROM book " + "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)
    
    books_to_add = _cursor.fetchall()

    print("\n Displaying books not currently in wishlist ")

    for book in books_to_add:
        print("\n Book ID: {}\n Book Name: {} Author: {}".format(book[0], book[1], book[2]))

"""Method to actually add the book into the user's wishlist"""
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor() 

    print("Welcome to Whatabook")

    user_selection = show_menu()

    while user_selection != 4:
        """If user selects 1 display books"""
        if user_selection == 1:
            show_books(cursor)
            sys.exit(0)
        """If user selects 2 show locations"""
        if user_selection == 2:
            show_locations(cursor)
            sys.exit(0)
        """If user selects 3 validate them and then display the account menu"""
        if user_selection == 3:
            users_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, users_id)

                if account_option == 2: 
                    show_books_to_add(cursor, users_id)
                    book_id = int(input(" Please enter the book ID that you would like to add to your wishlist "))
                    add_book_to_wishlist(cursor, users_id, book_id)
                    db.commit()
                    print("\n The book with Book ID {} was successfully added to your wishlist ".format(book_id))

                if account_option < 0 or account_option > 3:
                    print("Sorry, that option does not exist")

                account_option = show_account_menu()

            if user_selection < 0 or user_selection > 4:
                print(" Sorry, that option does not exist")

            user_selection = show_menu()

        print("Program terminated")


except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:

    db.close()
