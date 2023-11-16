'''Python Worksheet 3'''

#Exercise 14
runningTotal = 0
price1 = 12
runningTotal = runningTotal + price1
price2 = 24
runningTotal = runningTotal + price2
price3 = 36
runninTotal = runningTotal + price3
price4 = 48
runninTotal = runningTotal + price4
print(runningTotal)

#Exercise 15
file = open("daffodils.txt")
for line in file:
    print(line.strip())
file.close() 

#Exercise 16
runningTotal2 = 0
file = open("daffodils.txt")
for line2 in file:
    line2.strip()
    runningTotal2 = runningTotal2 + 1
file.close() 

#Exercise 17
lineCount = 0
runningTotal3 = 0
file = open("num_calc_1.txt")
for line3 in file:
    line3 = line3.strip()
    if(line3.isdigit()):
        runningTotal3 = runningTotal3 + int(line3)
        lineCount = lineCount + 1
print(runningTotal3 / lineCount)
file.close()

lineCount2 = 0
runningTotal4 = 0
file = open("num_calc_2.txt")
for line4 in file:
    line4 = line4.strip()
    if(line4.isdigit()):
        runningTotal4 = runningTotal4 + int(line4)
        lineCount2 = lineCount2 + 1
print(runningTotal4 / lineCount2)
file.close()

#Exercise 18
n1 = int(input("Input a number: "))
n2 = int(input("Input a number: "))
n3 = int(input("Input a number: "))
n4 = int(input("Input a number: "))
n5 = int(input("Input a number: "))
n6 = int(input("Input a number: "))
n7 = int(input("Input a number: "))
n8 = int(input("Input a number: "))
n9 = int(input("Input a number: "))
n10 = int(input("Input a number: "))
n11 = int(input("Input a number: "))
n12 = int(input("Input a number: "))
n13 = int(input("Input a number: "))
n14 = int(input("Input a number: "))
n15 = int(input("Input a number: "))
n16 = int(input("Input a number: "))
n17 = int(input("Input a number: "))
n18 = int(input("Input a number: "))
n19 = int(input("Input a number: "))
n20 = int(input("Input a number: "))
mean = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12 + n13 + n14 + n15 + n16 + n17 + n18 + n19 + n20
mean = mean / 20
print(mean)

#Exercise 19
count = 0
runningTotal5 = 0
lineCount5 = 0
fil = open("average.txt", 'w')
while(count < 10):
    n = (input("Input a number: "))
    fil.write(n)
    fil.write("\n")
    n = 0
    count = count + 1
fil.close()
fil = open("average.txt")
for line in fil:
    line = line.strip()
    if(line.isdigit()):
        runningTotal5 = runningTotal5 + int(line)
        lineCount5 = lineCount5 + 1
print(runningTotal5 / lineCount5)
fil.close() 
    