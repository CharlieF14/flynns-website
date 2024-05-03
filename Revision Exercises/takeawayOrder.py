#1. Read throught the program, then run it to make sure you understand what it is doing.
#2. Ask the user for their name and save it in an appropriately named variable.
#3. Include the user's given name in the print statement where they are thanked for their order.
#4. Write a function to calculate the total value of the order and print this number to the screen
#   with an appropriate description. DO NOT PUT THE PRINT STATEMENT INSIDE THE FUNCTION
#5. Modify your function so the delivery_fee is added to the total price of the order unless the
#   total value of the food is greater than value of free_delivery_price. Print this new value
#   to the screen with appropriate text.


takeaway_menu = ["1. Pad Thai","2. Chicken Tikka Masala","3. Pepperoni Pizza","4. Veggie Burger with Fries","5. Burrito Bowl"]
takeaway_prices = [12.99, 14.50,  9.99,  15.99,  11.50]
delivery_fee = 5.00
free_delivery_price = 30.00

userName = input("What is your name: ")

def totalCost(order, takeaway_prices, x, y):
    total = 0
    for i in order:
        total = total + takeaway_prices[order.index(i)]
        
    if total > y:
        return total
    else:
        total = total + x
        return total

print("Welcome to the takeaway delivery service.")
print("Here's our menu.")
for item in takeaway_menu:
    print(item)

quantity = int(input("How many items would you like to purchase?"))
order = []
for i in range(quantity):
    choice = int(input("Enter the menu number of the item you wish to add to your order: "))
    order.append(choice)
print(f"Thank you {userName} your order is as follows")
for item in order:
    print(takeaway_menu[item-1])

print(f"Total cost: €{totalCost(order, takeaway_prices, delivery_fee, free_delivery_price):.2f}")

