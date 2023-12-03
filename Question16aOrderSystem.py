#Question 16 a)
#Charlie Flynn, Athlone Community College

#This program is a simple ordering system
print("Welcome to the new online ordering system.\n")
user_name = input("Please enter your user name: ")
noOrder = int(input("How many items are the customers order: "))

total_cost = 0
if noOrder <= 0:
    print("Invalid option")
else:
    for i in range(1,noOrder + 1, 1):
        price_of_item = float(input("Enter the price of item {}".format(i)+" : € "))
        total_cost+= price_of_item
        i += 1

    print("You entered", noOrder, "items and the total is €", total_cost)
    balance = float(input("What is the customers current account balance € "))
    balanceTotal = balance - total_cost
    if balanceTotal > 0:
        print("Your remaining balance: €", balanceTotal)
    else:
        owed = balanceTotal * -1
        print("The customer does not have enough credit in their account, they still owe: €", owed)
    print("The member of staff who processed your order was:", user_name)
