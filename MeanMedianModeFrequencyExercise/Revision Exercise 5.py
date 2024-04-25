#Revision Exercise 5
def menu():
    f = open('1000 random numbers - corrupted 1.txt', 'r')
    f2 = open('1000 random numbers for frequency.txt', 'r')
    
    print('1) Calculate Mean')
    print('2) Calculate Median')
    print('3) Calculate Mode')
    print('4) Calculate Frequency')
    print('5) Quit')
    
    choice = int(input("Make your choice: "))
    
    if choice == 1:
        mean(f)
    elif choice == 2:
        median(f)
    elif choice == 3:
        mode(f)
    elif choice == 4:
        frequency(f2)
    elif choice == 5:
        print("Thank you.")
    else:
        print("Invalid Choice. Please enter again.")
        menu()
 
 
def mean(f):
    count = 0
    total = 0
    for line in f:
        line_split = line.split(' ')
        for num in line_split:
            if num.isdigit() == True:
                num = int(num)
                count = count + 1
                total = total + num
    avg = total // count
    
    print('Mean is', avg)
    print('\n')
    
    f.close
    menu()

def median(f):
    medianList = []
    for line in f:
        line_split = line.split(' ')
        for num in line_split:
            if num.isdigit() == True:
                num = int(num)
                medianList.append(num)
    medianList = sorted(medianList)
    if len(medianList) % 2 == 0:
        mid = (len(medianList)) // 2
        avgMedian = medianList[mid]
        
        print("Median is", avgMedian)
        
    else:
        median1 = (len(medianList) - 1) // 2
        median2 = (len(medianList)) // 2
        
        avgMedian = medianList[median1] + medianList[median2]
        avgMedian = avgMedian // 2
        
        print(len(medianList))
        
        print("Median is", avgMedian)
        
    f.close
    menu()

def mode(f):
    modeList = []
    modeDict = {}
    modes = []
    counter = 1
    for line in f:
        line_split = line.split(' ')
        for num in line_split:
            if num.isdigit() == True:
                num = int(num)
                if num not in modeList:
                    modeList.append(num)
                    modeDict[num] = modeDict.get(num, 0) + 1
                else:
                    counter = modeDict[num] + 1
                    modeDict.update({num: counter})
                    counter = 1
                    
    placehold = 0
    for key in modeDict:
        if modeDict[key] > placehold:
            modes.clear()
            placehold = modeDict[key]
            modes.append(key)
        elif modeDict[key] == placehold:
            modes.append(key)
    
    print("The mode is", modes)
    
    f.close()
    menu()
    
def frequency(f2):
    frequencyList = []
    frequency = {}
    counter = 1
    for line in f2:
        line_split = line.split(',')
        for num in line_split:
            if num.isdigit() == True:
                num = int(num)
                if num not in frequencyList:
                    frequencyList.append(num)
                    frequency[num] = frequency.get(num, 0) + 1
                else:
                    counter = frequency[num] + 1
                    frequency.update({num: counter})
                    counter = 1
                    
    print("Frequencies of file 2 are:", frequency)
    
    f2.close()
    menu()
    
menu()