from calendar import isleap
while(True):
    year = input('Of which year do you want to know if it\'s a leap year? (type exit to end program) ')
    #print(isleap(int(year)))
    if year == 'exit':
        exit()
    elif isleap(int(year)) == True:
        print(year, 'is a leap year\n')
    else:
        print(year, 'is not a leap year\n')