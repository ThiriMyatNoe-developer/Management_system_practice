# ### Problem 4: Expense Tracking System

# **Scenario:**

# You want to build a personal expense tracking system to manage your daily spending.

# The system should help users record their expenses and understand where their money goes.

# **Requirements:**

# 1. Store expense records using a list of dictionaries.
# 2. Each expense must contain:
#    - Expense ID
#    - Category
#    - Amount
#    - Description
# 3. Allow users to add new expenses.
# 4. Allow users to delete an expense by Expense ID.
# 5. Display all expense records.
# 6. Calculate the total expenses.
# 7. Calculate the total amount spent in each category.
# 8. Display all unique expense categories using a set.
# 9. Allow users to search expenses by category.
# 10. Allow users to set a monthly budget.
# 11. Display a warning when total expenses exceed the monthly budget.

# **Expected Features:**
# - Add Expense
# - Delete Expense
# - View All Expenses
# - Search by Category
# - Category Summary
# - Total Expenses
# - Budget Warning
# - Exit

# ---

expenses = []
monthly_budget = 0
while True:
    print("\n===== Expense Tracking System =====")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. View All Expenses")
    print("4. Search by Category")
    print("5. Category Summary")
    print("6. Total Expenses")
    print("7. Set Monthly Budget")
    print("8. Budget Warning")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")
    
    if choice == "1":
        expense_id = input("Enter Expense ID:")
        if expense_id in expenses:
            print("Expense Id already exists.")
        else:
            category =input("Enter Expense Category:")
            amount=float(input("Enter Expense Amount:"))
            description=input("Enter Expense Descripption")
            expenses.append({
                "id": expense_id,
                "category": category,
                "amount": amount,
                "description": description
        })
            print("Product added successfully.")
            
    elif choice =="2":
        expense_id = input("Enter Remove Expense ID:")
        found = False
        for expense in expenses:
            if expense["id"] == expense_id:
                expenses.remove(expense)
                print("Expense removed successfully.")
                found = True
                break
        else:
            print("Expense not found.")
            
    elif choice =="3":
        print("\n-- All Expenses --")
        for expense in expenses:
            print(f"ID:{expense['id']},Category:{expense['category']},Amount:{expense['amount']},Description:{expense['description']}")
    
    elif choice =="4":
        search_category = input("Enter categorry to search:")
        found =False
        for expense in expenses:
            if expense["category"].lower() == search_category.lower():
                print(f"ID:{expense['id']},Category:{expense['category']},Amount:{expense['amount']},Description:{expense['description']}")
                found = True
        if not found:
            print("No expenses found in this category:")
            
    elif choice == "5":
        category_summary = {}
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in category_summary:
                category_summary[category] += amount
            else:
                category_summary[category] = amount
        print("\n-- Category Summary --")
        for category, total in category_summary.items():
            print(f"Category: {category}, Total Amount: {total}")
            
    elif choice == "6":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Expenses:", total)
        
    elif choice == "7":
        monthly_budget = float(input("Enter your monthly budget: "))
        print("Monthly budget set to:", monthly_budget)
        
    elif choice == "8":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Monthly Budget:", monthly_budget)
        print("Total Expenses:", total)

        if monthly_budget == 0:
            print("Please set your monthly budget first.")

        elif total > monthly_budget:
            print("WARNING! You have exceeded your monthly budget.")

        else:
            remaining = monthly_budget - total
            print("You are within your budget.")
            print("Remaining Budget:", remaining)
            
    elif choice == "9":
        print("Existing the Expense Tracking System .")
        break
    
    else:
        print("Invalid choice. Please choose a number between 1 and 9.")
        


