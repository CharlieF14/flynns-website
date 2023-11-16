''' Functions exercise '''

#Question 1
def userNum():
    num = int(input('Enter a number: '))
    count(num)
    
def count(num):
    i = 0
    while i < num:
        i = i + 1
        print(i)
        
#Question 2
def randomGenerate():
    highNum = int(input('Pick a high number: '))
    lowNum = int(input('Pick a low number: '))
    import random
    comp_num = random.randint(lowNum, highNum)
    randomGuess(comp_num)
    
def randomGuess(comp_num):
    print('I am thinking of a number: ')
    guess = int(input('Guess what it is: '))
    checkRandom(comp_num, guess)
    
def checkRandom(comp_num, guess):
    if comp_num == guess:
        print('Correct, you win!')
    elif comp_num > guess:
        print('Nuh uh, too low')
        randomGuess(comp_num)
    elif comp_num < guess:
        print('Nuh uh, too high')
        randomGuess(comp_num)
        
#Question 3
def mainMenu():
    print('1) Addition')
    print('2) Subtraction')
    userInput = int(input('Enter 1 or 2: '))
    if userInput == 1:
        addition()
    elif userInput == 2:
        subtraction()
    else:
        print('Error invalid input')
        
def addition():
    import random
    randNum1 = random.randint(5,20)
    randNum2 = random.randint(5,20)
    print(randNum1)
    print(randNum2)
    userAns = int(input("Add these numbers together: "))
    ans = randNum1 + randNum2
    print('This is the answer:', ans)
    print('This was your answer:', userAns)
    answer(userAns, ans)

def subtraction():
    import random
    randNum1 = random.randint(25, 50)
    randNum2 = random.randint(1, 25)
    print(randNum1)
    print(randNum2)
    ans = randNum1 - randNum2
    userAns = int(input("Subtract these numbers: "))
    print('This is the answer:', ans)
    print('This was your answer:', userAns)
    answer(userAns, ans)
        
def answer(userAns, ans):
    if userAns == ans:
        print('Correct')
    else:
        print('Incorrect')
        
#Question 4
nameList = []
def menuMain():
    print('1) Add name to list')
    print('2) Change name in list')
    print('3) Delete name in list')
    print('4) View names in list')
    print('5) End Program')
    userChoice = int(input('Please choose what option you would like: '))
    if userChoice == 1:
        nameAdd(nameList)
    elif userChoice == 2:
        nameChange(nameList)
    elif userChoice == 3:
        nameDelete(nameList)
    elif userChoice == 4:
        nameView(nameList)
    elif userChoice == 5:
        print('Ending program...')
    else:
        print('Invalid input!')
        menuMain(nameList)
        
def nameAdd(nameList):
    userInput = input('Please enter a name to add: ')
    nameList.append(userInput)
    menuMain()

def nameChange(nameList):
    print(nameList)
    userInput = input('Please choose the name to be changed: ')
    userInput2 = input('Please choose a name to add: ')
    nameList[nameList.index(userInput)] = userInput2
    menuMain()

def nameDelete(nameList):
    print(nameList)
    userInput = input('Please enter a name to delete: ')
    nameList.remove(userInput)
    menuMain()
    
def nameView(nameList):
    print('These are the names:', nameList)
    menuMain()
    
#Question 5
file = open('Salaries.csv')
delete = []
def q5Menu():
    print('1) Add to file')
    print('2) View all records')
    print('3) Delete a record')
    print('4) Quit program')
    userChoice = int(input("Enter the number of your selection: "))
    if userChoice == 1:
        fileAdd(file)
    elif userChoice == 2:
        fileView(file)
    elif userChoice == 3:
        fileDelete(file)
    elif userChoice == 4:
        print('Quitting program...')
    else:
        print('Invalid input!')
    
def fileAdd(file):
    file = open('Salaries.csv', 'a')
    userName = input('What name would you like to add: ')
    userSalary = input('What salary would you like to add: ')
    file.write(userName + '' + userSalary)
    file.write('\n')
    file.close()
    q5Menu()
    
def fileView(file):
    file = open("Salaries.csv", 'r')
    for line in file:
        print(line)
    file.close()
    q5Menu()
        
def fileDelete(file):
    file = open('Salaries.csv', 'r')
    for line in file:
        delete.append(line)
    file.close()
    userDel = int(input("Please choose the line to delete: "))
    del delete[userDel - 1]
    file = open('Salaries.csv', 'w')
    for index in delete:
        file.write(index)
    file.close()
    q5Menu()