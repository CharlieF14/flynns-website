#Revision Exercise 5
def menu():
    f = open('1000 random numbers - corrupted 1.txt', 'r')
    
    print('1) Calculate Mean')
    print('2) Calculate Median')
    print('3) Calculate Mode')
    print('4) Calculate Frequency')
    print('5) Quit')
    
    choice = int(input("Make your choice: "))
    
    if choice == 1:
        mean(f)
    elif choice == 2:
        median(f)
    elif choice == 3:
        mode(f)
    elif choice == 4:
        frequency(f)
    elif choice == 5:
        print("Thank you.")
    else:
        print("Invalid Choice. Please enter again.")
        menu()
 
 
def mean(f):
    count = 0
    total = 0
    for line in f:
        line_split = line.split(' ')
        for num in line_split:
            if num.isdigit() == True:
                num = int(num)
                count = count + 1
                total = total + num
    avg = total // count
    
    print('Mean is', avg)
    print('\n')
    
    f.close
    menu()
 
menu()