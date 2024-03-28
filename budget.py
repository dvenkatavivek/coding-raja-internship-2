import json
import os
from datetime import datetime

# Function to load transactions from a file
def load_transactions():
    if os.path.exists("transactions.json"):
        with open("transactions.json", "r") as file:
            return json.load(file)
    else:
        return {"transactions": []}

# Function to save transactions to a file
def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

# Function to add a transaction
def add_transaction(transactions):
    transaction_type = input("Enter transaction type (Income/Expense): ").lower()
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transactions["transactions"].append({
        "type": transaction_type,
        "category": category,
        "amount": amount,
        "date": date
    })

    save_transactions(transactions)
    print("Transaction added successfully.")

# Function to calculate total income
def calculate_total_income(transactions):
    total_income = sum(transaction["amount"] for transaction in transactions["transactions"] if transaction["type"] == "income")
    return total_income

# Function to calculate total expenses
def calculate_total_expenses(transactions):
    total_expenses = sum(transaction["amount"] for transaction in transactions["transactions"] if transaction["type"] == "expense")
    return total_expenses

# Function to calculate remaining budget
def calculate_remaining_budget(transactions):
    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)
    remaining_budget = total_income - total_expenses
    return remaining_budget

# Function to analyze expenses by category
def analyze_expenses(transactions):
    expenses_by_category = {}
    for transaction in transactions["transactions"]:
        if transaction["type"] == "expense":
            category = transaction["category"]
            amount = transaction["amount"]
            if category in expenses_by_category:
                expenses_by_category[category] += amount
            else:
                expenses_by_category[category] = amount
    return expenses_by_category

# Function to display budget summary
def display_budget_summary(transactions):
    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)
    remaining_budget = calculate_remaining_budget(transactions)

    print("\n=== BUDGET SUMMARY ===")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

# Function to display expense analysis
def display_expense_analysis(transactions):
    expenses_by_category = analyze_expenses(transactions)
    print("\n=== EXPENSE ANALYSIS ===")
    for category, amount in expenses_by_category.items():
        print(f"{category}: ${amount:.2f}")

# Main function
def main():
    transactions = load_transactions()

    while True:
        print("\n===== BUDGET TRACKER =====")
        print("1. Add Transaction")
        print("2. View Budget Summary")
        print("3. View Expense Analysis")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            display_budget_summary(transactions)
        elif choice == "3":
            display_expense_analysis(transactions)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
