'''Python Worksheet 2'''

#Exercise 8
#1
MyFloatValue = float(9.82)
print((MyFloatValue))
print(type(MyFloatValue))
MyIntValue = int(MyFloatValue)
print((MyIntValue))
print(type(MyIntValue))
MyStrValue = str(MyFloatValue)
print((MyStrValue))
print(type(MyStrValue))
#2
'''placeholder = "hello"
placeholder = int(placeholder)
print(placeholder)
A Value Error'''

#Exercise 9
#1
'''year = input("Enter the current year")
age = int(input("What age will you be at the end of this year?"))
print("You were born in", year-age)
Type Error
You cannot subtract an int from a string'''
#2
year = input("Enter the current year")
age = int(input("What age will you be at the end of this year?"))
birthyear = int(year) - age
print("You were born in", birthyear)
#3
'''a will give an error as they are separate value types'''

#Exercise 10
mars = 1
coke = 1.5
crisps = .8
tea = 2
bread = 3.5
total = (int(mars) * 5) + (int(coke) * 4) + (int(crisps) * 3) + (int(tea) * 2) + int(bread)
print(float(total))

#Exercise 11
number1 = int(input("Enter first number: "))
number2 = input("Enter second number: ")
number2 = int(number2)
sum = number1 + number2
print(number1, "+", number2, "=", sum)

#Exercise 12
tempf = int(input("Enter the temperature in Fahrenheit: "))
tempc = ((tempf - 32) * (5/9))
print("The temperature in celsius is", tempc)

#Exercise 13
dd = int(input("Enter the day number: "))
mm = int(input("Enter the month number: "))
y = int(input("Enter the last 2 digits of the year: "))
c = int(input("Enter the first 2 digits or the year: "))
if(mm < 3):
    mm = mm + 12
    y = y - 1
x = int((13 * (mm + 1)) // 5)
w = int((dd + x + y + (y//4) + (c//4) - 2*c)%7)
print("The day of the week is", w)