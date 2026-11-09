# ## Medium Level

# ### Problem 3: Inventory Management System

# **Scenario:**

# You work at a small supermarket. Your manager wants you to build a simple inventory management system to track products and stock quantities.

# **Requirements:**

# 1. Store product information using a dictionary.
# 2. Each product must have:
#    - Product ID
#    - Product Name
#    - Price
#    - Stock Quantity
# 3. Allow users to add new products.
# 4. Allow users to update product prices.
# 5. Allow users to increase or decrease stock quantities.
# 6. Prevent users from selling more products than the available stock.
# 7. Display all products with their current stock quantities.
# 8. Display products that have fewer than 5 items in stock.
# 9. Search for products by Product ID.
# 10. Allow users to continue managing inventory until they choose to exit.

# **Expected Features:**
# - Add Product
# - Update Product
# - Stock In
# - Stock Out
# - View Inventory
# - Low Stock Alert
# - Search Product
# - Exit

# ---
products = {
    "001":{"name":"Apple","price":2000,"quality":50},
    "002":{"name":"Banana","price":1500,"quality":30},
    "003":{"name":"Orange","price":1200,"quality":40},
}
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Stock In")
    print("4. Stock Out")
    print("5. View Inventory")
    print("6. Low Stock Alert")
    print("7. Search Product")
    print("8. Exit")
    
    choice = input("Enter your choice:")
    if choice =="1":
        product_id=input("Enter new product id:")
        if product_id in products:
            print("Product already exists.")
        else:
            product_name=input("Enter product name:")
            product_price=int(input("Enter product price:"))
            product_quality=int(input("Enter product quality:"))
            products[product_id]={
                "name":product_name,
                "price":product_price,
                "quality":product_quality 
            }
            print("Product added successfully.")
            
    elif choice == "2":
        product_id=input("Enter product id to update:")
        if product_id in products:
            new_price=int(input("Enter new price:"))
            products[product_id]["price"]=new_price
            print("Product price updated successfully.")
        else:
            print("Product not found.")
        
    elif choice == "3":
        product_id=input("Enter product id to stock in:")
        if product_id in products:
            stock_in=int(input("Enter quantity to add:"))
            products[product_id]["quality"]+=stock_in
            print("Stock updated successfully.")
        else:
            print("Product not found.")
            
    elif choice == "4":
        product_id=input("Enter product id to stock out:")
        if product_id in products:
            stock_out=int(input("Enter quantity to remove:"))
            if stock_out <= products[product_id]["quality"]:
                products[product_id]["quality"]-=stock_out
                print("Stock updated successfully.")
            else:
                print("Error! Not enough stock.")
        else:
            print("Product not found.")
            
    elif choice =="5":
        print("\n--- Current Inventory ---")
        for product_id, details in products.items():
            print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['quality']}")
            
    elif choice =="6":
        print("\n--- Low Stock Products ---")
        low_stock_found = False
        for product_id, details in products.items():
            if details["quality"] < 5:
                print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['quality']}")
                low_stock_found = True
        if not low_stock_found:
            print("No products with low stock.")
            
    elif choice =="7":
        product_id=input("Enter product id to search:")
        if product_id in products:
            details=products[product_id]
            print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['quality']}")
        else:
            print("Product not found.")
            
    elif choice =="8":
        print("Exiting the Inventory Management System.")
        break
    
    else:
        print("Invalid choice. Please choose a number between 1 and 8.")
    