
books = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("Library is empty.")
        else:
            print("\nBooks Available:")
            count = 1
            for book in books:
                print(count, ".", book)
                count = count + 1

    elif choice == "3":
        search = input("Enter book name to search:")
        if search in books:
            print("Book is available in the library")
        else:
            print("Book not found.")

    elif choice == "4":
        remove = input("Enter book name to remove:")
        if remove in books:
            books.remove(remove)
            print("Book removed successfully")
        else:
            print("Book not found")

    elif choice == "5":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")