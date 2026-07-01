contacts = {}

while True:
    print("\n=== Contact Manager ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")

        contacts[name] = phone

    elif choice == "2":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Search name: ")

        if name in contacts:
            print(f"Phone: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Delete name: ")

        if name in contacts:
            del contacts[name]
            print("Deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
