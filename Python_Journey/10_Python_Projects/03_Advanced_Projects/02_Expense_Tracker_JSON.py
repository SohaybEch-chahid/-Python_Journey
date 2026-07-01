import json
import os

FILE_NAME = "expenses.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
else:
    expenses = []


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Expense Name: ")
        amount = float(input("Amount: "))

        expenses.append({"name": name, "amount": amount})

        save_data()

    elif choice == "2":
        for expense in expenses:
            print(f"{expense['name']} - ${expense['amount']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print(f"Total Spending: ${total}")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
