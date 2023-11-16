''' LCCS Algorithms '''
#Linear Search
linearSearch = [15, 4, 41, 13, 24, 14, 12, 21]
''' Target = 14 '''
#1) Non-Recursive
j = 0
for i in linearSearch:
    if i == 14:
        print('Match Found',j)
        break
    else:
        print('Not Found, Continuing Search')
        j = j + 1
#2) Recursive
        
#Binary Search
binarySearch = [23, 4, 56, 7, 8, 9, 14, 10, 17, 19, 2, 25, 48, 28, 33, 37]
binarySearch.sort()
''' Target = 28 '''
#1) Non-Recursive
l = 100
low = binarySearch[0]
high = binarySearch[-1]
mid = (high + low) // 2
while low <= high:
    if mid == 28:
        print('Match Found' , binarySearch.index(28))
        break
    elif mid < 28:
        low = mid + 1
        mid = (high + low) // 2
    elif mid > 28:
        high = mid - 1
        mid = (high + low) // 2
#2)
        
#Simple Sort
#1) Non-Recursive
simpleSearchUnsorted = [9, 6, 10, 4, 8, 5, 7]
simpleSearchSorted = []
minimum = simpleSearchUnsorted[0]
l = 0
g = len(simpleSearchUnsorted)
while g != 0:
    for i in simpleSearchUnsorted:
        if i > minimum:
            continue
        elif i < minimum:
            minimum = i
    simpleSearchSorted.append(minimum)
    simpleSearchUnsorted.remove(minimum)
    g = len(simpleSearchUnsorted)
    l = l + 1
    if g != 0:
        minimum = simpleSearchUnsorted[0]
print(simpleSearchSorted)
    
#Simple Selection Sort
selection = [9, 6, 10, 4, 8, 5, 7]
minimum = 0
marker = 0
for i in selection:
    marker = i
    if marker > minimum:
        continue
    elif marker < minimum:
        minimum = marker
        
        
#Quicksort
qS = [88, 46, 25, 11, 18, 12, 22]
def quicksort(qS):
    left_list = []
    middle_list = []
    right_list = []
    sorted_list=[]
    pivot = qS[-1]
    for i in qS:
        if i < pivot:
            left_list.append(i)    
        elif i == pivot:
            middle_list.append(i)
        elif i > pivot:
            right_list.append(i)
    print(left_list)
    print(right_list)
    print(middle_list)
    quicksort(qS)
quicksort(qS)