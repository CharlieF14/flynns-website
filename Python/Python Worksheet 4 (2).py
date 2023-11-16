'''Python Worksheet 4: Caesar Cipher'''
#Part 1a
'''
a - D
b - E
c - F
d - G
e - H
f - I
g - J
h - K
i - L
j - M
k - N
l - O
m - P
n - Q
o - R
p - S
q - T
r - U
s - V
t - W
u - X
v - Y
w - Z
x - A
y - B
z - C
'''

#Part 1b
'''Dwkoqh Frppxqlwb Froohjh'''

#Part 1c
'''25 keys'''

#Part 1d
'''What Do You Get When You Cross A Snowman With A Vampire? Frostbite'''

#Part 2
msg =  input("Enter the message to be encoded: ")
msg = msg.lower()
code = input("Do you wish to encode or decode: ")
code = code.lower()
i = 0
keyNum = int(input("Enter the key number: "))
if (keyNum > 25):
    keyNum = keyNum % 26
elif (keyNum < 1):
    keyNum = abs(keyNum)
    if (keyNum > 25):
        keyNum = keyNum % 26
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while(i<len(msg)):
    if (code == 'encode'):
        if (msg[i] == ' '):
            i = i + 1
        else:
            msg = msg.replace(msg[i], (alphabet[alphabet.index(msg[i]) + keyNum]), 1)
            print(msg[i])
            i = i + 1
    elif (code == 'decode'):
        if (msg[i] == ' '):
            i = i + 1
        else:
            msg = msg.replace(msg[i], (alphabet[alphabet.index(msg[i]) - keyNum]), 1)
            i = i + 1
print (msg)
    
