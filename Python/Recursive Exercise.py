''' Recursive Exercise '''
#Question 1
userList = []
def addList(userList):
    n = 0
    userSum = 0
    userAns = input("Would you like to add to a list? ")
    userAns = userAns.lower()
    if userAns == 'yes':
        userNum = int(input("Enter a number: "))
        userList.append(userNum)
        addList(userList)
    else:
        sumList(userList, n, userSum)
        
def sumList(userList, n, userSum):
    if n == len(userList):
        print(userSum)
    else:
        userSum = userSum + userList[n]
        n = n + 1
        sumList(userList, n, userSum)
        
#Question 2
factorial = 0
def fact(n):
    if n < 0:
        n = n * -1
        fact(n)
    elif(n > 1):
        factorial = n * fact(n - 1)
    elif(n == 1):
        factorial = n * 1
    return factorial

#Question 3
def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n >=3:
        return fibo(n - 1) + fibo(n - 2)

#Question 4
def sumDigi(n):
    g = n % 10
    if n == 0:
        return 0
    else:
        return g + sumDigi(n // 10)
    
#Question 5
def eucl(n):
    