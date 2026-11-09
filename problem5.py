# Problem 5: Restaurant Order Management System

# **Scenario:**

# You are developing an order management system for a restaurant.

# Customers can view the menu, place orders, and receive their bills. Restaurant staff can manage orders and track their status.

# **Requirements:**

# 1. Store restaurant menu items using a dictionary.
# 2. Each menu item must contain:
#    - Item ID
#    - Item Name
#    - Price
#    - Category
# 3. Allow customers to view all menu items.
# 4. Allow customers to place an order by selecting an Item ID and quantity.
# 5. Store each customer's order using a list of dictionaries.
# 6. Allow customers to add multiple items to one order.
# 7. Prevent customers from ordering items that do not exist in the menu.
# 8. Calculate the subtotal for each order.
# 9. Apply a 5% service charge to the subtotal.
# 10. Generate a unique Order ID for each order.
# 11. Store order information using a dictionary.
# 12. Allow restaurant staff to view all orders.
# 13. Allow staff to update order status:
#     - Pending
#     - Preparing
#     - Completed
#     - Cancelled
# 14. Prevent users from updating an order that does not exist.
# 15. Display the final bill with item names, quantities, prices, and total amount.
# 16. Allow the program to continue running until the user chooses to exit.

# **Expected Features:**
# - View Menu
# - Place Order
# - View Order
# - View All Orders
# - Update Order Status
# - Generate Bill
# - Exit

# ---

# ## Practice Rules

# 1. Do not use OOP (class and object).
# 2. Do not use functions (def).
# 3. Do not use databases.
# 4. Do not use file handling.
# 5. Use only the Python concepts you have already learned:
#    - Variables
#    - Data Types
#    - If / Else Conditions
#    - For Loops
#    - For-Else
#    - While Loops
#    - Lists
#    - Tuples
#    - Sets
#    - Dictionaries


menu = {
    "1": {"name": "Fried Rice", "price": 5000, "category": "Food"},
    "2": {"name": "Coffee", "price": 2500, "category": "Drink"},
    "3": {"name": "Chicken Rice", "price": 6000, "category": "Food"}
}

orders = {}
order_count = 1

while True:
    print("\n===== Restaurant Order System =====")
    print("1. View Menu")
    print("2. Place Order")
    print("3. View Order")
    print("4. View All Orders")
    print("5. Update Order Status")
    print("6. Generate Bill")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for item_id, item in menu.items():
            print(item_id, item["name"], item["price"], item["category"])

    elif choice == "2":
        order_items = []

        while True:
            item_id = input("Enter Item ID: ")

            if item_id in menu:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    item = {
                        "name": menu[item_id]["name"],
                        "price": menu[item_id]["price"],
                        "quantity": quantity
                    }

                    order_items.append(item)
                    print("Item added successfully.")
                else:
                    print("Invalid quantity.")
            else:
                print("Item not found.")

            more = input("Add more items? (yes/no): ")

            if more.lower() != "yes":
                break

        if len(order_items) > 0:
            order_id = "O" + str(order_count)
            order_count += 1

            subtotal = 0

            for item in order_items:
                subtotal += item["price"] * item["quantity"]

            service_charge = subtotal * 0.05
            total = subtotal + service_charge

            orders[order_id] = {
                "items": order_items,
                "subtotal": subtotal,
                "service": service_charge,
                "total": total,
                "status": "Pending"
            }

            print("Order placed successfully!")
            print("Your Order ID:", order_id)

    
    elif choice == "3":
        order_id = input("Enter Order ID: ")

        if order_id in orders:
            print("Order ID:", order_id)
            print("Status:", orders[order_id]["status"])

            for item in orders[order_id]["items"]:
                print(item)

            print("Total:", orders[order_id]["total"])
        else:
            print("Order not found.")

   
    elif choice == "4":
        for order_id, details in orders.items():
            print("Order ID:", order_id)
            print("Status:", details["status"])
            print("Total:", details["total"])

   
    elif choice == "5":
        order_id = input("Enter Order ID: ")

        if order_id in orders:
            print("1. Pending")
            print("2. Preparing")
            print("3. Completed")
            print("4. Cancelled")

            status = input("Choose status: ")

            if status == "1":
                orders[order_id]["status"] = "Pending"
            elif status == "2":
                orders[order_id]["status"] = "Preparing"
            elif status == "3":
                orders[order_id]["status"] = "Completed"
            elif status == "4":
                orders[order_id]["status"] = "Cancelled"
            else:
                print("Invalid status.")
                continue

            print("Status updated successfully.")
        else:
            print("Order not found.")

    
    elif choice == "6":
        order_id = input("Enter Order ID: ")

        if order_id in orders:
            details = orders[order_id]

            print("\n===== Restaurant Bill =====")

            for item in details["items"]:
                print("Name:", item["name"])
                print("Price:", item["price"])
                print("Quantity:", item["quantity"])
                print("Subtotal:", item["price"] * item["quantity"])

            print("Subtotal:", details["subtotal"])
            print("Service Charge:", details["service"])
            print("Final Total:", details["total"])
        else:
            print("Order not found.")

   
    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
