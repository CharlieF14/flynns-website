''' Random Exercises '''
import random
#Question 1
q1 = random.randint(1,100)
print(q1)

#Question 2
q2 = ["banana", "orange", "pear", "apple", "tomato"]
q2Ans = random.choice(q2)
print(q2Ans)

#Question 3
q3User = input('Heads or Tails? ')
q3Ans = random.choice("ht")
if q3User == q3Ans:
    print("You win")
else:
    print("Bad Luck")
    
#Question 4
q4Ans = random.randint(1,5)
q4User = int(input("Pick a number between 1 and 5: "))
if q4User == q4Ans:
    print("Well done")
elif q4User > q4Ans:
    print("Too high")
    q4User = int(input("Pick again: "))
    if q4User == q4Ans:
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Too low")
    q4User = int(input("Pick again: "))
    if q4User == q4Ans:
        print("Correct")
    else:
        print("Incorrect")
        
#Question 5
q5 = 