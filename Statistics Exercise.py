''' Statistics Exercise '''

file = open("mean-median-mode-frequency.csv", "r")
frequency = {}
mode = []
avg = 0
count = 0
test = 0
lineNum = 1
median = []
medianCount = 0
for line in file:
    line_split = line.split(',')
    for num in line_split:
        if num == '\n':
            avg = 0
            count = 0
            frequency = {}
            median = []
            test = 1
        else:
            num = int(num)
            count = count + 1
            frequency[num] = frequency.get(num, 0) + 1
            avg = avg + int(num)
            median.append(str(num))
            test = 0
    if test == 0:
        avg = avg / count
        medianCount = int(count / 2)
        placeHold = 0
        for key in frequency:
            if frequency[key] > placeHold:
                placeHold = frequency[key]
                mode.clear()
                mode.append(key)
            elif frequency[key] == placeHold:
                mode.append(key)
        print("Line",lineNum,":")
        print("Mean:", avg)
        print("Frequency:", frequency)
        print("Median:", median[medianCount])
        print("Mode:", mode)
        lineNum = lineNum + 1