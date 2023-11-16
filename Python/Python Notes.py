'''Python Notes'''
#Running Total
#Initialise the variable
runningTotal = 0
#Perfrom Calculations
price1 = 10
runningTotal = runningTotal + price1
price2 = 14
runningTotal = runningTotal + price2
price3 = 6
runninTotal = runningTotal + price3

#Display the Output
print(runningTotal)

#Opening a file
file = open("myFile.txt")
print(file)
for line in file: #Line is just a variable
    print(line.strip()) #.Strip removes end line character
    #You cannot run this loop twice as it has gone through the file
file.close() #Closes the file, otherwise it will be locked
#If you close and reopen the file the loop can be performed again