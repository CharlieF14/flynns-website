#Revision Exercise 4

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def choice():
    
    print("1) Make a code")
    print("2) Decode a message")
    print("3) Quit")
    choice = int(input("Enter your selection: "))

    if choice == 1:
        encode(alp)
    elif choice == 2:
        decode(alp)
    elif choice == 4:
        print("Ending program")
    else:
        print("Invalid Input")
        choice()
        
def encode(alp):
    message = input("Please enter a message to be encoded: ")
    message = message.lower()
    
    key = int(input("Enter the number key: "))
    while key > 25:
        key = int(input("Enter the number key <= 25: "))
    key2 = key
    
    encoded = []
    msg = list(message)
    
    for i in msg:
        if i not in alp:
            encoded.append(i)
        else:
            pos = alp.index(i)
            if (key2 + pos) > 25:
                key2 = key2 - 26
            encoded.append(alp[pos + key2])
    
    print("This is the encoded message", encoded)
    choice()

def decode(alp):
    message = input("Please enter a message to be decoded: ")
    message = message.lower()
    
    key = int(input("Enter the number key: "))
    while key > 25:
        key = int(input("Enter the number key <= 25: "))
    key2 = key
    
    decoded = []
    msg = list(message)
    
    for i in msg:
        if i not in alp:
            decoded.append(i)
        else:
            pos = alp.index(i)
            while (key2 - pos) > 25:
                key2 = (key2 - pos) - 25
            decoded.append(alp[pos - key2])
            
    print("This is the decoded message", decoded)
    choice()

choice()