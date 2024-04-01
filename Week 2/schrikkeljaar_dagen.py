def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_in_year(year):
    print(365 + is_leap(year))

year = int(input('Of which year do you wish to know how many days it has? '))
days_in_year(year)