import json
import os
from colorama import init, Fore, Style

# Initialize colorama for colored terminal output
init(autoreset=True)

LIBRARY_FILE = "library.json"

def load_library():
    """Load library data from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save library data to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def print_header(text):
    """Print a formatted header."""
    print(Fore.CYAN + Style.BRIGHT + f"\n{text}\n" + "=" * len(text))

def add_book(library):
    """Add a new book to the library."""
    print_header("Add a New Book")
    title = input(Fore.YELLOW + "Enter book title: ")
    author = input(Fore.YELLOW + "Enter author: ")
    while True:
        try:
            year = int(input(Fore.YELLOW + "Enter publication year: "))
            break
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a valid year.")
    genre = input(Fore.YELLOW + "Enter genre: ")
    read = input(Fore.YELLOW + "Have you read it? (yes/no): ").strip().lower() == "yes"
    
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    })
    save_library(library)
    print(Fore.GREEN + f'\n"{title}" has been added to your library.')

def remove_book(library):
    """Remove a book from the library."""
    print_header("Remove a Book")
    title = input(Fore.YELLOW + "Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print(Fore.GREEN + f'"{title}" has been removed.')
            return
    print(Fore.RED + "Book not found.")

def search_book(library):
    """Search for a book by title or author."""
    print_header("Search for a Book")
    query = input(Fore.YELLOW + "Enter book title or author to search: ")
    results = [book for book in library if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
    
    if results:
        print(Fore.GREEN + "\nSearch Results:")
        for book in results:
            print(Fore.BLUE + f'{book["title"]} by {book["author"]} ({book["year"]}) - ' +
                  (Fore.GREEN + "Read" if book["read"] else Fore.RED + "Unread"))
    else:
        print(Fore.RED + "No books found.")

def display_books(library):
    """Display all books in the library."""
    print_header("Your Library")
    if not library:
        print(Fore.RED + "No books in the library.")
        return
    
    for book in library:
        print(Fore.BLUE + f'{book["title"]} by {book["author"]} ({book["year"]}) - ' +
              (Fore.GREEN + "Read" if book["read"] else Fore.RED + "Unread"))

def display_statistics(library):
    """Show total books and percentage of read books."""
    print_header("Library Statistics")
    total_books = len(library)
    if total_books == 0:
        print(Fore.RED + "No books in the library.")
        return
    
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100
    
    print(Fore.GREEN + f"Total books: {total_books}")
    print(Fore.GREEN + f"Books read: {read_books} ({percentage_read:.2f}%)")

def main():
    """Main function to handle menu and user input."""
    library = load_library()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for a clean UI
        print(Fore.MAGENTA + Style.BRIGHT + "\n📖 Personal Library Manager 📖")
        print(Fore.CYAN + "1. Add a book")
        print(Fore.CYAN + "2. Remove a book")
        print(Fore.CYAN + "3. Search for a book")
        print(Fore.CYAN + "4. Display all books")
        print(Fore.CYAN + "5. Display statistics")
        print(Fore.CYAN + "6. Exit")
        
        choice = input(Fore.YELLOW + "\nChoose an option: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print(Fore.MAGENTA + "Goodbye! 👋")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
        
        input(Fore.YELLOW + "\nPress Enter to continue...")  # Pause before refreshing menu

if __name__ == "__main__":
    main()