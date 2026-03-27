library_books = ["Python Basics", "Data Structures", "Java Programming", "AI Introduction"]

def display_books():
    print("\nAvailable Books:")
    for book in library_books:
        print("-", book)

def borrow_book():
    book = input("Enter the book name to borrow: ")
    if book in library_books:
        library_books.remove(book)
        print("You have borrowed:", book)
    else:
        print("Sorry, this book is not available.")

def return_book():
    book = input("Enter the book name to return: ")
    library_books.append(book)
    print("Thank you for returning:", book)

# Main program loop
while True:
    print("\nLibrary Menu")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        display_books()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
