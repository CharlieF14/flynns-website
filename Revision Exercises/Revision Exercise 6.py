#Revision Exercise 6

#Question 1
character = input("Enter the character: ")
asc = ord(character)
print(f'Original value: {character}, ASCII: {asc}')

#Question 2
num = int(input("Enter the ASCII value: "))
uni = chr(num)
print(f'Original value: {num}, Unicode: {uni}')

#Question 3
message = ("abcdefghijklmonopqrstuvwxyz")
lis = []
for i in message:
    asc1 = ord(i)
    asc1 = asc1 + 2
    
    if asc1 > 122:
        asc1 = asc1 - 26
    
    uni1 = chr(asc1)
    lis.append(uni1)
    
decode = ''
for i in lis:
    decode = decode + i
    
print(f'Decoded Message: {decode}')