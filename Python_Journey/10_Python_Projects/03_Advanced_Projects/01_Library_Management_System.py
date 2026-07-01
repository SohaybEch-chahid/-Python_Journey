books = []

while True:
    print("\n=== Library Management ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Book title: ")

        books.append({"title": title, "available": True})

    elif choice == "2":
        if not books:
            print("No books available.")

        for book in books:
            status = "Available" if book["available"] else "Borrowed"

            print(f"{book['title']} - {status}")

    elif choice == "3":
        title = input("Book title: ")

        for book in books:
            if book["title"].lower() == title.lower():
                if book["available"]:
                    book["available"] = False
                    print("Book borrowed.")
                else:
                    print("Already borrowed.")

    elif choice == "4":
        title = input("Book title: ")

        for book in books:
            if book["title"].lower() == title.lower():
                book["available"] = True
                print("Book returned.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
