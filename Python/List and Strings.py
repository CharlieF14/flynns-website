'''Strings and Lists'''
egg = "hello"
yolk = ["hello", "there"]
scrambled = 0
boiled = 0

#Strings
scrambled = egg[3]
print(scrambled)

scrambled = egg[-1]
print(scrambled)

scrambled = egg[1:3]
print(scrambled)

scrambled = egg.upper()
print(scrambled)

scrambled = egg.lower()
print(scrambled)

scrambled = egg.count("l")
print(scrambled)

scrambled = egg.find("l")
print(scrambled)

scrambled = egg.replace("l", "o")
print(scrambled)

scrambled = egg.islower()
print(scrambled)

scrambled = egg.isupper()
print(scrambled)

scrambled = egg.isalnum()
print(scrambled)

scrambled = egg.isalpha()
print(scrambled)

scrambled = egg.isdigit()
print(scrambled)

scrambled = egg.index("el")
print(scrambled)

scrambled = egg.strip("lo")
print(scrambled)

#Lists
yolk[1] = 5
yolk[1]
yolk[-1]
yolk[0:1]
yolk[1:]
del yolk[1]

boiled = yolk.append(32)
print(boiled)

boiled = yolk.extend(yolk)
print(boiled)

boiled = yolk.insert(3, "yahoo")
print(boiled)

boiled = yolk.remove(32)
print(boiled)

boiled = yolk.pop(2)
print(boiled)

boiled = yolk.index("hello")
print(boiled)

boiled = yolk.count("there")
print(boiled)

boiled = yolk.sort()    #Only works if the list has only one data type
print(boiled)

boiled = sorted(yolk)   #Only works if the list has only one data type
print(boiled)

boiled = yolk.reverse()
print(boiled)

boiled = yolk.clear()
print(boiled)

boiled = yolk.copy()
print(boiled)

