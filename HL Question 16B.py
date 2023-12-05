# Question 16(b)
# examination Number: Charlie Flynn

studentNameList = []
studentResultList = []

def studentNames(studentNameList):
    studentName = input("Please enter the student's name and enter 'end' or 'End' when complete: ")
    if studentName == 'end' or studentName == 'End':
        studentResults(studentResultList, studentNameList)
    else:
        studentNameList.append(studentName)
        studentNames(studentNameList)
        
def studentResults(studentResultList, studentNameList):
    studentResult = int(input("Please enter the students result and enter '-1' when complete: "))
    if studentResult == -1:
        print(studentNameList)
        print(studentResultList)
        if len(studentNameList) < len(studentResultList):
            print("ERROR: You have entered more student results than student names")
            print("Compare the entered names and results and add the missing name to the correct index location.")
            print("\n Student results are:", studentResultList)
            print("\n Student names are:", studentNameList)
            forgottenName = input("Please enter the students name that was left out: ")
            forgottenIndex = int(input("What is the index position of the name: "))
            studentNameList.insert(forgottenIndex, forgottenName)
            scores(studentResultList, studentNameList)
        elif len(studentNameList) > len(studentResultList):
            print("ERROR: You have entered more student names than student results")
            print("Compare the entered names and results and add the missing result to the correct index location.")
            print("\n Student results are:", studentResultList)
            print("\n Student names are:", studentNameList)
            forgottenResult = int(input("Please enter the students result that was left out: "))
            forgottenIndex = int(input("What is the index position of the result: "))
            studentResultList.insert(forgottenIndex, forgottenResult)
            scores(studentResultList, studentNameList)
        else:
            scores(studentResultList, studentNameList)
    else:
        studentResultList.append(studentResult)
        studentResults(studentResultList, studentNameList)
        
def scores(studentResultList, studentNameList):
    placehold = 0
    placehold2 = 200
    for i in studentResultList:
        if i > placehold:
            placehold = i
            maxIndex = studentResultList.index(i)
        else:
            continue
    maxResult = float((placehold/ 200) * 100)
    print("Highest Value scored is:", maxResult)
    
    for j in studentResultList:
        if j <= placehold2:
            placehold2 = j
            minIndex = studentResultList.index(j)
        else:
            continue
    minResult = float((placehold2/ 200) * 100)
    print("Lowest value scored is:", minResult)
    
    maxStudent = studentNameList[maxIndex]
    print("The student who scored the highest value is:", maxStudent)
    
    minStudent = studentNameList[minIndex]
    print("The student who scored the lowest value is:", minStudent)
    
    avg = 0
    amount = 0
    
    for k in studentResultList:
        avg += k
        amount += 1
    avgResult = round(float((avg / amount)/200 * 100), 1)
    print("The average value in the class is:", avgResult)
    
    
studentNames(studentNameList)