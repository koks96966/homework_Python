def month_to_season(month):
    if not isinstance(month, int) or month < 1 or month > 12:
        return "Ошибка: введите число от 1 до 12"
    if month in [12, 1, 2]:
        return 'зима'
    elif month in [3, 4, 5]:
        return 'весна'
    elif month in [6, 7, 8]:
        return 'лето'
    else:
        return 'осень'


user_input = input("Введите номер месяца (от 1 до 12): ")
try:
    month_number = int(user_input)
    result = month_to_season(month_number)
    print(f"Сезон: {result}")
except ValueError:
    print("Ошибка: нужно ввести целое число!")
