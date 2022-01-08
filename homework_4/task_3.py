from timeit import timeit
from random import randint

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    enter_num = int("".join(reversed(str(enter_num))))
    return enter_num

number = randint(1000, 10000)
print(f"Исходное число: {number}")

print(f'\nРекурсия: ', revers(number))
print("Время работы:" ,timeit('revers(number)', globals=globals()))

print(f'\nЦикл: ', revers_2(number))
print("Время работы:", timeit('revers_2(number)', globals=globals()))

print(f'\nСрезы: ', revers_3(number))
print("Время работы:", timeit('revers_3(number)', globals=globals()))

print(f'\nМое решение: ', revers_4(number))
print("Время работы:", timeit('revers_4(number)', globals=globals()))

""" Полученные данные: 
Исходное число: 8107

Рекурсия:  7018
Время работы: 1.7177350999999998

Цикл:  7018
Время работы: 1.5571053000000001

Срезы:  7018
Время работы: 0.5992850999999999

Мое решение:  7018
Время работы: 0.9788399999999999
"""

# Аналитика: Быстрее всего работают срезы, так как тут по сути всего одна операция. Хуже всего конечно работает рекурсия,
# из-за наличия арифметических операций. Цикл работает чуть быстрее, но по большему счету функции очень похожи. Просто в
# первой мы используем рекурсии для перебора, а во втором цикл. Мой вариант решения хуже срезов по той причине, что
# помимо функции reversed, используется еще функция join, которая тоже требует времени
