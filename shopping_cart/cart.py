"""
Shopping Cart
--------------
Lets the user add products with their price to the cart until
they type 'done'. Shows a summary of the purchase and applies a
10% discount if the total exceeds €100.
"""

cart = []

# Collect products and prices until the user decides to finish
while True:
    product = input("Enter the product name (or 'done' to finish): ")
    if product.lower() == "done":
        break
    price = float(input(f"Enter the price of {product}: "))
    cart.append({"name": product, "price": price})

# Calculate the total and show the purchase summary
total_price = sum(item['price'] for item in cart)
print("\nShopping cart summary:")
for item in cart:
    print(f"- {item['name']}: {item['price']:.2f}€")

# Apply a 10% discount if the purchase exceeds €100
if total_price > 100:
    print("You got a 10% discount for spending over €100!")
    discount_applied = total_price * 0.10
    total_price -= discount_applied
    print(f"Discount applied: {discount_applied:.2f}€")

print(f"Total to pay: {total_price:.2f}€")