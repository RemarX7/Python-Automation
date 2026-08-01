import math


def square(m2):
    return math.ceil(m2*m2)


m2 = int(input('Введите значения стороны квадрата: '))
print(f'Площадь квадрата = {square(m2)}')
