import math


def square(side):
    try:
        side = float(side)
        side = math.ceil(side)
        return side * side
    except ValueError:
        return "Ошибка: введите корректное число"


side_input = input("Введите длину стороны квадрата: ")
print(square(side_input))
