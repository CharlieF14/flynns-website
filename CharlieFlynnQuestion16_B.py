#Question 16- b)
#Charlie Flynn, Athlone Community College
List1 = [4, 5, 9, 8, 10, 17, 99, 77]
List1.sort()
print (List1)
median = 0
medianL = []

if len(List1) % 2 != 0:
    median = List1[len(List1) // 2]
    print (median)
else:
    medianL.append(List1[(len(List1) // 2) - 1])
    medianL.append(List1[(len(List1) // 2)])
    print (medianL)