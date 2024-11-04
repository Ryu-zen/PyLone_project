import json
import os

# File to store financial data
DATA_FILE = 'finances.json'

# Load existing finances from the JSON file
def load_finances():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"income": [], "expenses": []}

# Save finances to the JSON file
def save_finances(finances):
    with open(DATA_FILE, 'w') as file:
        json.dump(finances, file)

# Add income
def add_income(finances):
    amount = float(input("Enter the income amount: "))
    description = input("Enter a description for this income: ")
    finances["income"].append({"amount": amount, "description": description})
    save_finances(finances)
    print(f"Income of ${amount} added!")

# Add expense
def add_expense(finances):
    amount = float(input("Enter the expense amount: "))
    description = input("Enter a description for this expense: ")
    finances["expenses"].append({"amount": amount, "description": description})
    save_finances(finances)
    print(f"Expense of ${amount} added!")

# Display all finances
def display_finances(finances):
    total_income = sum(item["amount"] for item in finances["income"])
    total_expenses = sum(item["amount"] for item in finances["expenses"])
    balance = total_income - total_expenses

    print("\n--- Financial Overview ---")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Balance: ${balance}\n")

    print("Income Records:")
    for income in finances["income"]:
        print(f"- ${income['amount']} ({income['description']})")
    
    print("\nExpense Records:")
    for expense in finances["expenses"]:
        print(f"- ${expense['amount']} ({expense['description']})")

# Main function to run the Finance Tracker
def main():
    finances = load_finances()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Finances")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_income(finances)
        elif choice == '2':
            add_expense(finances)
        elif choice == '3':
            display_finances(finances)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
