'''Strings Exercise'''
#Question 1
userName = input("Enter your name: ")
userName = len(userName)
print(userName)

#Question  2
userFirst = input("Enter your first name: ")
userSecond = input("Enter your second name: ")
userName = userFirst + " " + userSecond
print(userName)
length = len(userName)
print(length)

#Question 3
userFirst = userFirst.title()
userSecond = userSecond.title()
userName = userFirst + " " + userSecond
print(userName)

#Question 4
userRhyme = input("Enter the first line of a nursery rhyme: ")
userRhymeLen = len(userRhyme)
print(userRhymeLen)
startNum = int(input("Enter a starting number: "))
endingNum = int(input("Enter a ending number: "))
userRhyme = userRhyme[startNum:endingNum]
print(userRhyme)

#Question 5
userWord = input("Enter a word: ")
userWord = userWord.upper()
print(userWord)

#Question 6
if len(userFirst) < 5:
    userName = userFirst + userSecond
    userName = userName.upper()
    print(userName)
else:
    userFirst = userFirst.lower()
    print(userFirst)
    
#Question 7
normWord = input("Enter a word: ")
vowels = ["a", "e", "i", "o", "u"]
if normWord[0] in vowels:
    pigWord = normWord + "way"
else:
    first = normWord[0]
    normWord = normWord.replace(normWord[0],"",1)
    pigWord = normWord + first + "ay"
    
pigWord = pigWord.lower()
print(pigWord)