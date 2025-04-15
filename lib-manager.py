import json
import os

class LibraryManager:
    def __init__(self):
        self.library_file = "library.txt"
        self.library = []
        self.load_library()

    def load_library(self):
        """Load library data from file if it exists"""
        try:
            if os.path.exists(self.library_file):
                with open(self.library_file, "r") as file:
                    self.library = json.load(file)
                print("\nLibrary loaded successfully!")
        except (FileNotFoundError, json.JSONDecodeError):
            self.library = []

    def save_library(self):
        """Save library data to file"""
        with open(self.library_file, "w") as file:
            json.dump(self.library, file)
        print("\nLibrary saved to file. Goodbye!")

    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*40)
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        print("="*40)

    def add_book(self):
        """Add a new book to the library"""
        print("\n" + "="*40)
        print("Add a New Book")
        print("="*40)
        
        title = input("Enter the book title: ").strip()
        author = input("Enter the author: ").strip()
        
        while True:
            try:
                year = int(input("Enter the publication year: ").strip())
                break
            except ValueError:
                print("Please enter a valid year (e.g., 2023).")
        
        genre = input("Enter the genre: ").strip()
        
        read_input = input("Have you read this book? (yes/no): ").strip().lower()
        read = read_input in ['yes', 'y']
        
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read
        }
        
        self.library.append(book)
        print(f"\n'{title}' by {author} added successfully!")

    def remove_book(self):
        """Remove a book from the library"""
        print("\n" + "="*40)
        print("Remove a Book")
        print("="*40)
        
        if not self.library:
            print("Your library is empty!")
            return
            
        title = input("Enter the title of the book to remove: ").strip()
        
        for book in self.library:
            if book["title"].lower() == title.lower():
                self.library.remove(book)
                print(f"\n'{title}' removed successfully!")
                return
                
        print(f"\nBook with title '{title}' not found!")

    def search_books(self):
        """Search for books by title or author"""
        print("\n" + "="*40)
        print("Search for Books")
        print("="*40)
        
        if not self.library:
            print("Your library is empty!")
            return
            
        print("Search by:")
        print("1. Title")
        print("2. Author")
        
        while True:
            choice = input("Enter your choice (1-2): ").strip()
            if choice in ['1', '2']:
                break
            print("Invalid choice. Please enter 1 or 2.")
        
        search_term = input(f"Enter the {'title' if choice == '1' else 'author'} to search for: ").strip().lower()
        
        if choice == '1':
            matches = [book for book in self.library if search_term in book["title"].lower()]
        else:
            matches = [book for book in self.library if search_term in book["author"].lower()]
        
        if matches:
            print("\nMatching Books:")
            for i, book in enumerate(matches, 1):
                read_status = "Read" if book["read"] else "Unread"
                print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
        else:
            print("\nNo matching books found!")

    def display_all_books(self):
        """Display all books in the library"""
        print("\n" + "="*40)
        print("Your Library")
        print("="*40)
        
        if not self.library:
            print("Your library is empty!")
            return
            
        for i, book in enumerate(self.library, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

    def display_statistics(self):
        """Display library statistics"""
        print("\n" + "="*40)
        print("Library Statistics")
        print("="*40)
        
        total_books = len(self.library)
        print(f"Total books: {total_books}")
        
        if total_books > 0:
            read_books = sum(1 for book in self.library if book["read"])
            percentage_read = (read_books / total_books) * 100
            print(f"Percentage read: {percentage_read:.1f}%")
        else:
            print("Percentage read: 0.0%")

    def run(self):
        """Main program loop"""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_books()
            elif choice == '4':
                self.display_all_books()
            elif choice == '5':
                self.display_statistics()
            elif choice == '6':
                self.save_library()
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    manager = LibraryManager()
    manager.run()