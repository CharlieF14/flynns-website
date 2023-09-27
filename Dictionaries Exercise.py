''' Dictionaries Exercise '''
#Question 1
'''
sentence = input("Enter a sentence: ")
chars = {}
vowels = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0
consonantCount = 0
for char in sentence:
    print(char)
    if char in vowels:
        chars[char] = chars.get(char, 0) + 1
        vowelCount = vowelCount + 1
    else:
        consonantCount = consonantCount + 1
print(chars)
print('vowels:', vowelCount, 'consonants:', consonantCount)
from collections import Counter
c = Counter(chars)
max_pair = c.most_common()[0]
print("%s occurs most often %d times" %(max_pair[0], max_pair[1]))
'''
'''
a) The programm counts the amount of times that a letter appears in the sentence
b) Get the individual letters on there own in order to count how often they occur
c) A Dictionary
d) Keys = The separate letters in the sentence
   Values = How often they occur
e) It runs the same
f) It gets a value of a specified key
'''
#i)
'''sentence = input("Enter a sentence: ")
sent_list = sentence.split()
words = {}
for word in sent_list:
    if word in words:
    words[word] = words[word] + 1
    else:
        words[word] = 1
print(words)'''
'''
j) Finds which letter occurs most and how many times it occurs
b) Displays which letter occurs most often first
k) '''

#Question 2

#sentence = input("Enter a sentence: ")
#sent_list = sentence.split()
file = open('dictionary.txt', 'r')
punct = ["!", ".", "?"]
words = {}
avg = 0
count = 0
for line in file:
    line_list = line.split()
    for word in line_list:
        word = word.lower()
        count = count + 1
        if word[-1] in punct:
            word = word.strip(word[-1])
        if len(word) <= 3:
            words[word] = words.get(word, 0) + 1
            avg = avg + len(word)
        else:
            avg = avg + len(word)
avg = avg / count
print(words)
print(avg)
'''
a) Have:1 a:2 very:3 merry:2 Christmas:1 and:1 New:1 Year:1
   happy:2 birthday:2 dear:1 Mary:1 to:1 you:1
   ho:2 ho!:1
b) Since python is a case sensitive language words that have different capital letter will be counted as separate words
c) Leading and trailing characters could be removed and all words could be converted to lowercase or uppercase to keep them the same
'''