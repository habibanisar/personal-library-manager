# import json

# # List to store books as dictionaries
# library = []

# # Load library from file at start
# def load_library():
#     global library
#     try:
#         with open("library.txt", "r") as file:
#             library = json.load(file)
#     except FileNotFoundError:
#         library = []  # If file doesn't exist, start with empty library

# # Save library to file on exit
# def save_library():
#     with open("library.txt", "w") as file:
#         json.dump(library, file)
#     print("Library saved to file.")

# def add_book():
#     """Function to add a book to the library"""
#     title = input("Enter the book title: ")
#     author = input("Enter the author: ")
#     year = int(input("Enter the publication year: "))  # Convert to integer
#     genre = input("Enter the genre: ")
#     read = input("Have you read this book? (yes/no): ").lower()
#     read_status = True if read == "yes" else False  # Convert to boolean
    
#     # Create book dictionary
#     book = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "genre": genre,
#         "read": read_status
#     }
    
#     library.append(book)  # Add book to library
#     print("Book added successfully!")

# def remove_book():
#     """Function to remove a book from the library"""
#     title = input("Enter the title of the book to remove: ")
#     for book in library:
#         if book["title"].lower() == title.lower():  # Case-insensitive match
#             library.remove(book)
#             print("Book removed successfully!")
#             return
#     print("Book not found!")

# def search_book():
#     """Function to search for a book by title or author"""
#     print("Search by:")
#     print("1. Title")
#     print("2. Author")
#     choice = input("Enter your choice: ")
    
#     if choice == "1":
#         title = input("Enter the title: ")
#         matches = [book for book in library if title.lower() in book["title"].lower()]
#     elif choice == "2":
#         author = input("Enter the author: ")
#         matches = [book for book in library if author.lower() in book["author"].lower()]
#     else:
#         print("Invalid choice!")
#         return
    
#     if matches:
#         print("Matching Books:")
#         for i, book in enumerate(matches, 1):
#             read_status = "Read" if book["read"] else "Unread"
#             print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
#     else:
#         print("No matching books found!")

# def display_all_books():
#     """Function to display all books in the library"""
#     if not library:
#         print("Your library is empty!")
#     else:
#         print("Your Library:")
#         for i, book in enumerate(library, 1):
#             read_status = "Read" if book["read"] else "Unread"
#             print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# def display_statistics():
#     """Function to display library statistics"""
#     total_books = len(library)
#     if total_books == 0:
#         print("Total books: 0")
#         print("Percentage read: 0.0%")
#         return
    
#     read_books = sum(1 for book in library if book["read"])
#     percentage_read = (read_books / total_books) * 100
    
#     print(f"Total books: {total_books}")
#     print(f"Percentage read: {percentage_read:.1f}%")

# def main():
#     load_library()  # Load library at start
#     while True:
#         print("\nMenu")
#         print("Welcome to your Personal Library Manager!")
#         print("1. Add a book")
#         print("2. Remove a book")
#         print("3. Search for a book")
#         print("4. Display all books")
#         print("5. Display statistics")
#         print("6. Exit")
        
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             add_book()
#         elif choice == "2":
#             remove_book()
#         elif choice == "3":
#             search_book()
#         elif choice == "4":
#             display_all_books()
#         elif choice == "5":
#             display_statistics()
#         elif choice == "6":
#             save_library()  # Save before exiting
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice! Please try again.")

# if __name__ == "__main__":
#     main()


import streamlit as st
import json
import os

# Initialize library
if 'library' not in st.session_state:
    st.session_state.library = []

# Load library from file
def load_library():
    try:
        if os.path.exists("library.txt"):
            with open("library.txt", "r") as file:
                st.session_state.library = json.load(file)
    except FileNotFoundError:
        st.session_state.library = []

# Save library to file
def save_library():
    with open("library.txt", "w") as file:
        json.dump(st.session_state.library, file)

# Add a book
def add_book(title, author, year, genre, read):
    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read
    }
    st.session_state.library.append(book)
    save_library()
    st.success("Book added successfully!")

# Remove a book
def remove_book(title):
    for book in st.session_state.library:
        if book["title"].lower() == title.lower():
            st.session_state.library.remove(book)
            save_library()
            st.success("Book removed successfully!")
            return True
    st.error("Book not found!")
    return False

# Search for books
def search_book(search_term, search_by):
    if search_by == "Title":
        matches = [book for book in st.session_state.library if search_term.lower() in book["title"].lower()]
    else:  # Author
        matches = [book for book in st.session_state.library if search_term.lower() in book["author"].lower()]
    return matches

# Display all books
def display_all_books():
    if not st.session_state.library:
        st.write("Your library is empty!")
    else:
        st.write("### Your Library")
        for i, book in enumerate(st.session_state.library, 1):
            read_status = "Read" if book["read"] else "Unread"
            st.write(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Display statistics
def display_statistics():
    total_books = len(st.session_state.library)
    if total_books == 0:
        st.write("Total books: 0")
        st.write("Percentage read: 0.0%")
    else:
        read_books = sum(1 for book in st.session_state.library if book["read"])
        percentage_read = (read_books / total_books) * 100
        st.write(f"Total books: {total_books}")
        st.write(f"Percentage read: {percentage_read:.1f}%")

# Streamlit UI
def main():
    # Load library at start
    load_library()

    # Title and welcome message
    st.title("Personal Library Manager")
    st.write("Welcome to your Personal Library Manager!")

    # Sidebar menu
    menu = ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add a Book":
        st.subheader("Add a Book")
        with st.form("add_book_form"):
            title = st.text_input("Book Title")
            author = st.text_input("Author")
            year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
            genre = st.text_input("Genre")
            read = st.checkbox("Have you read this book?")
            submit = st.form_submit_button("Add Book")
            if submit:
                if title and author and genre:
                    add_book(title, author, year, genre, read)
                else:
                    st.error("Please fill in all required fields (Title, Author, Genre).")

    elif choice == "Remove a Book":
        st.subheader("Remove a Book")
        title = st.text_input("Enter the title of the book to remove")
        if st.button("Remove Book"):
            if title:
                remove_book(title)
            else:
                st.error("Please enter a title.")

    elif choice == "Search for a Book":
        st.subheader("Search for a Book")
        search_by = st.radio("Search by:", ("Title", "Author"))
        search_term = st.text_input(f"Enter the {search_by.lower()}")
        if st.button("Search"):
            if search_term:
                matches = search_book(search_term, search_by)
                if matches:
                    st.write("### Matching Books")
                    for i, book in enumerate(matches, 1):
                        read_status = "Read" if book["read"] else "Unread"
                        st.write(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
                else:
                    st.write("No matching books found!")
            else:
                st.error(f"Please enter a {search_by.lower()} to search.")

    elif choice == "Display All Books":
        st.subheader("All Books")
        display_all_books()

    elif choice == "Display Statistics":
        st.subheader("Library Statistics")
        display_statistics()

if __name__ == "__main__":
    main()