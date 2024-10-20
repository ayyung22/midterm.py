#CIS 103 Midterm Assignment: Programming Fundamentals and Problem Solving
#Author: Annie Yung
#Date: 10/20/2024

import re

print("Customer Information Management System")
#function to validate email pattern and will return customer to enter a valid email format
def validate_email():
    #email validation pattern
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    while True:
        email = input("Please enter your email: ").strip()
        if re.match(email_pattern, email):
            print("Email is valid.")
            return email
        else:
            print("Invalid email format. Please try again.")

#function to validate phone number format and will return customer to enter a valid phone number format
def validate_phone():
    #phone number validation patter
    phone_pattern = r'^\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    while True:
        phone = input("Please enter your phone number: ").strip()
        if re.match(phone_pattern, phone):
            print("Phone number is valid.")
            return phone
        else:
            print("Invalid phone number format. Please try again.")


# function to gather customer's information (name, email, and phone number)
def get_customer_info():
    print()
    print("Welcome! Please provide your contact details.")
    name = input("Please enter your name: ")
    email = validate_email()  # Validate email
    phone = validate_phone()  # Validate phone number

    # return customer's information
    return name, email, phone


#main program
name, email, phone = get_customer_info()
print(f"Customer's Name: {name}")
print(f"Customer's Email: {email}")
print(f"Customer's Phone: {phone}")

print()
print()

print("Product Ordering System, Applying Discounts, and Final Calculations")
#creating list of 5 predefined list items for customer's to choose from
products = [
    {"id": 1, "name": "Sweaters", "price": 20.00},
    {"id": 2, "name": "Shoes", "price": 40.00},
    {"id": 3, "name": "Jacket", "price": 150.00},
    {"id": 4, "name": "Cardigan", "price": 35.00},
    {"id": 5, "name": "Jeans", "price": 37.00}
    ]

#defining function that displays the list items by product ID, name, and price
def display_products():
    print("Available Products:")
    for product in products:
        print(f"ID: {product['id']} - {product['name']} - ${product['price']:.2f}")


#defining function that allows customer's to input product ID number and the quantity
def select_products():
    selected_items = []
    while True:
        display_products()
        try:
            product_id = int(input("\nEnter the product ID to select it (or 0 to finish): "))
            if product_id == 0:
                break  # exits the loop if the user enters 0

            # finding the product based on the ID
            product = next((p for p in products if p["id"] == product_id), None)
            if product:
                #asking the customer for the quantity of the product that was selected
                while True:
                    try:
                        quantity = int(input(f"How many {product['name']} would you like to buy? "))
                        if quantity > 0:
                            selected_items.append({"product": product, "quantity": quantity})
                            print(f"You selected {quantity} {product['name']}(s) - ${product['price'] * quantity:.2f}")
                            break
                        else:
                            print("Quantity must be a positive number. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number for quantity.")
            else:
                print("Invalid product ID. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return selected_items


#function that displays the cart, total price, apply discount (if eligible), and tax
def display_cart(selected_items, discount_threshold=100, discount_rate=0.10, tax_rate=0.0825):
    if selected_items:
        print("\nYour cart:")
        total_price = 0
        for item in selected_items:
            product = item["product"]
            quantity = item["quantity"]
            total_price += product["price"] * quantity
            print(f"{product['name']} - {quantity} x ${product['price']:.2f} = ${product['price'] * quantity:.2f}")

        #checking if discount applies
        if total_price > discount_threshold:
            discount = total_price * discount_rate
        else:
            discount = 0

        #applies discount to the total price
        total_price_after_discount = total_price - discount

        # applies tax to the price after discount, if applicable
        tax = total_price_after_discount * tax_rate
        final_price = total_price_after_discount + tax

        #print the details
        print(f"\nSubtotal: ${total_price:.2f}")
        if discount > 0:
            print(f"Discount ({discount_rate * 100}%): -${discount:.2f}")
        print(f"Total after discount: ${total_price_after_discount:.2f}")
        print(f"Tax ({tax_rate * 100}%): +${tax:.2f}")
        print(f"Final Total: ${final_price:.2f}")
    else:
        print("No products selected.")


#main Program
selected_items = select_products()
display_cart(selected_items)