# Question 16(a)
# Name and School: Charlie Flynn, Athlone Community College

import random
check = 0
while check <+ 1:
    s_name = input("Enter your surname:      ")    
    f_name = input("Enter your first name:      ")
    age = int(input("Enter your age:      "))
    eircode = input("Enter your eircode:      ")
    vaccines = ['A', 'B', 'C']
    print("Do you agree to enrol in a vaccine trial?")
    trial = input("Type 'YES' or 'NO'        ")
    print("Hello", f_name, s_name, ", you are", age,"years old and your Eircode is", eircode)
    if age > 12 and age < 49:
        print(f_name, "you will recieve the MRNA vaccine")
    elif age >= 50:
        print(f_name, "you will recieve the ADENO vaccine")
    eicode = list(eircode)
    if (int(eircode[-1]) % 2) == 0:
        print("You must attend Eastwood for your vaccine")
    elif (int(eircode[-1]) % 2) != 0:
        print("You must attend Northfield for your vaccine")
    if trial == "YES":
        supVac = random.choice(vaccines)
        print("You are now enrolled in the trial to recieve Super vaccine", supVac)
    elif trial == 'NO':
        print("You are not enrolled in the vaccine trial")

    repeat = input("If you have finished entering people's details type 'END', otherwise press RETURN:      ")
    if repeat == 'END':
        check = 1
    else:
        check = check + 1
