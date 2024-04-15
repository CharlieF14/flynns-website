#Revision Assignment 1

#Question 1
import random
num = random.randint(0,10)
print(num)

#Question 2
num1 = 4
num2 = 5
if num1 == num2:
    print(True)
elif num1 != num2:
    print(False)
    
#Question 3
userNum = int(input("Guess the number: "))
while userNum != num:
    print("That is not the number: ")
    userNum = int(input("Guess the number: "))
print("Congrats")




#Question 4

def palindrome(x):
    userList = list(x)
    backwards = []
    for i in userList:
        backwards.append(i)
    if backwards == userList:
        print("Your word is a palindrome.")
        
def symmetrical(x):
    userList
    
userCheck = 0
while userCheck != -1:
    userString = input("Please enter a string: ")
    palindrome(userString)
    symmetrical(userString)
    userCheck = int(input("Enter -1 to end the loop: "))
    
