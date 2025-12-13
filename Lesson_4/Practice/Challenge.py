cart = ['Mouse', 'Keyboard', 'Headset']

deleted_item = input("Enter the item you want to delete from the cart: ")
if deleted_item in cart:
    cart.remove(deleted_item)
    print(f"{deleted_item} has been removed from your cart.")
    print("Current items in your cart:")
    for item in cart:
        print(f"- {item}")
else:
    print(f"{deleted_item} is not found in your cart.")
    