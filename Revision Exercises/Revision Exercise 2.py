#Revision Exercise 2
import random

colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "clear"]

print(colours)

i = 0
computerList = []
userList = []
def colourPicker(computerList, userList):
    userList = []
    i = 0
    while i < 4:
        computerChoice = random.choice(colours)
        computerList.append(computerChoice)
    
        userChoice = input("Please enter your choice: ")
        userList.append(userChoice)
    
        i = i + 1
    
    print(userList)
    masterMind(userList, computerList)
        
def masterMind(x, y):
    i = 0
    correct = 0
    partial = 0
    while i < 4:
        if x[i] == y[i]:
            correct = correct + 1
            i = i + 1
        elif x[i] in y:
            i = i + 1
            partial = partial + 1
        else:
            i = i + 1
        
    print("Number of correct colours in correct place:", correct)
    print("Number of correct colours in incorrect place:", partial)
    if correct == 4:
        print("ALL CORRECT")
    else:
        colourPicker(computerList, userList)
    
colourPicker(computerList, userList)