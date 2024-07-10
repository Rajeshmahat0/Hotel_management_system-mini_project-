
# Define the menu of the restaurant
menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
}

# Function to handle ordering
def take_order(menu):
    order_total = 0
    while True:
        item = input("Enter the name of the item you want to order (or 'done' to finish): ").lower()

        if item == 'done':
            break

        if item in menu:
            order_total += menu[item]
            print(f"{item.capitalize()} has been added to your order")
        else:
            print(f"Sorry, {item.capitalize()} is not available in our menu")

    return order_total

if __name__ == "__main__":
    print("Welcome to our Restaurant")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item.capitalize()} : Rs {price}")

    order_total = take_order(menu)

    print(f"Your total order amount is Rs {order_total}")
    print("Thank you for visiting!")

