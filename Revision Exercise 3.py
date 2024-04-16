#Revision Exercise 3

f = open("Revision Exercise 3 IDs.csv")

print("1) Create a new User ID")
print("2) Change a password")
print("3) Display all User IDs")
print("4) Quit")

selection = int(input("Enter Selection: "))


def passwordCheck(userID, f):
    userPassword = input("Please enter a password: ")
    score = 0
    count = 0
    
    for i in userPassword:
        if i.isdigit() == True:
            score = score + 1
            count = count + 1
        elif i.isupper() == True:
            score = score + 1
            count = count + 1
        elif i.islower() == True:
            score = score + 1
            count = count + 1
            
    if count > 8:
        score = score + 1
    if userPassword.isalnum() == True:
        score = score + 1
        
    if score > 4:
        print("You have a strong password.")
        f.write(userID + ' ' + userPassword)
    elif score > 2 and score < 5:
        print("This password could be improved")
        again = int(input("Would you like to try again? 1 for yes and 0 for no: "))
        if again == 1:
            passwordCheck(userID, f)
        else:
            f.write(userID + '' + userPassword)
    else:
        print("This password is weak")
        passwordCheck(userID, f)


def newID(f):
    f = open("Revision Exercise 3 IDs.csv",'a+')
    userID = input("Please enter the new User ID: ")
    for line in f:
        if userID == line:
            userID = input("This User ID already exists. Please enter a different ID: ")
        else:
            continue

    passwordCheck(userID, f)
    


if selection == 1:
    newID(f)
elif selection == 2:
    newID(f)
elif selection == 3:
    newID(f)
elif selection == 4:
    newID(f)
else:
    print("Invalid Input.")

f.close()