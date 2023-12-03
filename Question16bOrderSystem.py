#Question 16 b)
#Charlie Flynn, Athlone Community College

Standard_Postal_List = ['Netherlands', 'Finland', 'Greece', 'Ireland', 'Denmark', 'Romania', 'Spain', 'Poland', 'France', 'Hungary', 'Portugal', 'Germany', 'Sweden']

shippingCountry = input("Where would you like to ship to: ")
if shippingCountry in Standard_Postal_List:
    print("This country uses standard postage and packaging costs")
else:
    print("This country is not on the approved delivery list")
    userAdd = input("Would you like to add this country to the approved Postal List for future deliveries, y/n: ")
    if userAdd == 'y' or 'Y':
        Standard_Postal_List.append(shippingCountry)
        print(shippingCountry, "has been added to the Standard Postal List")
    elif userAdd == 'n' or 'N':
        print(shippingCountry, "has not been added to the Standard Postal List")
    else:
        print("Invalid Operation")
    
Standard_Postal_List.sort()
print(Standard_Postal_List)