'''Lists Exercise'''
#Question 1
'''sports = ["football", "gaelic"]
userSport = input("Enter a sport: ")
sports.append(userSport)
sports.sort()
print(sports)

#Question 2
subjects = ["Enlgish", "Maths", "Irish", "Science", "History", "Geography"]
0print(subjects)
subjDislike = input("Which of these subjects to you dislike: ")
subjects.remove(subjDislike)
print(subjects)

#Question 3
colours = ["red", "green", "yellow", "blue", "purple", "cyan", "pink", "black", "white", "grey"]
userStart = int(input("Enter a number between 0 and 4: "))
userEnd = int(input("Enter a number between 5 and 9: "))
userColour = colours[userStart : userEnd]
print(userColour)

#Question 4
nums = [123, 456, 789, 312]
usNum = int(input("Enter a 3 digit number: "))
i = 0
while i < len(nums):
    print(nums[i])
    i = i + 1
    if usNum == nums[i]:
        print(nums.index(nums[i]))

#Question 5
l = 0
invs = []
while l < 3:
    invite = input("Who do you want to invite? ")
    invs.append(invite)
    l = l + 1
l = 0
j = 0
quest = input("Do you want to add another? ")
if quest == 'no':
    print(invs)
    print(len(invs))
else:
    while l == 0:
        if invite == 'no':
            print(invs)
            print(len(invs))
            l = -1
        else:
            invite = input("Who do you want to invite? ")
            invs.append(invite)
 
#Question 6
l = 0
invs = []
while l < 3:
    invite = input("Who do you want to invite? ")
    invs.append(invite)
    l = l + 1
l = 0
j = 0
quest = input("Do you want to add another? ")
if quest == 'no':
    print(invs)
    print(len(invs))
else:
    while l == 0:
        if invite == 'no':
            print(invs)
            print(len(invs))
            l = -1
        else:
            invite = input("Who do you want to invite? ")
            invs.append(invite)
unInv = input("Enter a name on the list: ")
print(invs.index(unInv))
response = input("Do you still want this person to come? ")
if response == 'no':
     invs.remove(unInv)
     print(invs)

#Question 7
tv = ["Lost in Space", "Mandolorian", "Gravity Falls", "The Boys"]
g = 0
while g < len(tv):
    print(tv[g])
    g = g + 1
userTv = input("Enter a TV show: ")
posTv = int(input("Enter the position: "))
tv.insert(posTv, userTv)
print(tv)
'''
#Question 8
l = 0
nums = []
while l < 3:
    userNumbor = input("Enter a number: ")
    nums.append(userNumbor)
    l = l + 1
quest = input("Do you want that number added? ")
if quest == 'no':
    nums.pop(-1)
    print(nums)
else:
 print(nums)
 