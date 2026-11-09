# Problem 1: Shopping Cart Management System

# **Scenario:**

# You are building a simple shopping cart system for an online store. Customers can add products to their shopping cart, remove products, and view their cart.

# **Requirements:**

# 1. Store product names and prices using a dictionary.
# 2. Allow customers to add products to their shopping cart.
# 3. Allow customers to remove products from their cart.
# 4. Display all products in the cart.
# 5. Calculate the total price of all products.
# 6. If a customer tries to add a product that does not exist, display an error message.
# 7. If a customer tries to remove a product that is not in the cart, display an error message.
# 8. Allow customers to continue shopping until they choose to exit.

# **Expected Features:**
# - Add Product
# - Remove Product
# - View Cart
# - Calculate Total
# - Exit

# ---

product={
    "book":2000,
    "pencil":700,
    "pen":1200
}
cart=[]
while True:
    print("1.add products to their shopping cart")
    print("2.remove products from their cart")
    print("3.Display all products in the cart.")
    print("4.Calculate the total price of all products.")
    print("5.Exit.")
    
    
    choice = input("Enter your choice")
    
    if choice == "1":
        new_products = input("Enter products")
        if new_products in product:
            cart.append(new_products)
            print("product is added successsfully")
        else:
            print("error! no product")
        
    elif choice == "2":
        remove_products = input("Enter products")
        if remove_products in cart:
            cart.remove(remove_products)
            print("product is removed successsfully")
        else:
            print("error!no product")
        
        
    elif choice == "3":
        if len(cart)==0:
            print("no products in carts")
        else:
            for ptd in cart:
                print(ptd,product[ptd])
           
    elif choice=="4":
        total=0
        for i in cart:
            total+=product[i]
        print(f"total is {total}")
        
    elif choice=="5":
        print("Thank you for Shopping Cart Management System")
        break
    
    else:
        print("Invalid choice. you should choose (1-5)")
        
            
            
    
        
