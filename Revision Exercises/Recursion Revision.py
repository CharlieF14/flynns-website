#Recursion Revision

#Question 1
l = [2, 56, 7, 12, 9]

sums = 0
i = 0

def sumOf(i, l):
    if i <= (len(l) - 1):
        return l[i] + sumOf(i+1, l)
    else:
        return 0
    
print(sumOf(i, l))

#print('\n')

#Question 2
number = int(input("Enter a number: "))

def fact(number):
    if number <= 1:
        return 1
    else:
        return number * fact(number - 1)

print(fact(number))

#print('\n')

#Question 3
n = int(input('Enter a non-negative integer: '))
if n < 0:
    n = n * -1
    print('Changing number to positive.')
n = str(n)

i = 0

def digSum(n, i):
    if i <= (len(n) - 1):
        return int(n[i]) + digSum(n, i+1)
    else:
        return 0
    
print(digSum(n, i))

#Question 4
a = int(input("Enter a number: "))
b = int(input("Enter the power value: "))

def power(a, b):
    if b > 1:
        return a * power(a, b-1)
    else:
        return a

print(power(a, b))

#Question 5
string = input("Enter a string: ")
i = 0

def has_digit(string):
    if string == '':
        return 0
    else:
        rest = has_digit(string[1:])
        if string[0] in '0123456789':
            check = 1 + rest
        else:
            check = 0 + rest
            
    if check > 0:
        return True
    else:
        return False

print(has_digit(string))