def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year = input("Введите год в формате ГГГГ: ")
yv = int(year)
print('Год ' + str(yv) + ' : ')
print(is_year_leap(yv))
