from random import randint
from timeit import timeit

# сортировка, которая была на уроке
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj

# более умная сортировка
def my_bubble_sort(lst_obj):
    flag = False
    for i in range(1, len(lst_obj)):
        for j in range(len(lst_obj) - i):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
                flag = True
        if not flag:
            return lst_obj
    return lst_obj

my_list = [randint(-100, 100) for _ in range(10)]
print("Исходный массив: ", my_list)
print("Отсортированный массив: ", bubble_sort(my_list[:]))
print("Более умная сортировка: ", my_bubble_sort(my_list[:]))
print("Замеры времени: ")
print("Первая функция: ", timeit("bubble_sort(my_list[:])", globals=globals(), number = 10000))
print("Вторая функция: ", timeit("my_bubble_sort(my_list[:])", globals=globals(), number = 10000))
"""
Получили:
Исходный массив:  [82, 82, -81, 24, 0, 56, -10, 87, 81, -72]
Отсортированный массив:  [87, 82, 82, 81, 56, 24, 0, -10, -72, -81]
Более умная сортировка:  [87, 82, 82, 81, 56, 24, 0, -10, -72, -81]
Замеры времени: 
Первая функция:  0.006622200000000002
Вторая функция:  0.0015683999999999976
"""
"""
Вывод:
Наша доработка улучшает работу первой функции, а именно, если массив уже отсортирован, то сортировать его не надо. 
Соответственно, чем сложнее перемешан массив, тем больше будут совпадать длительности выполнения сортировки. 
"""