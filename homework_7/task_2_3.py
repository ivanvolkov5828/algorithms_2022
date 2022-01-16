from timeit import timeit
from random import randint
from statistics import median

m = 10
lst_10 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("median(lst_10[:])", globals=globals(), number=1000))

m = 100
lst_100 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("median(lst_100[:])", globals=globals(), number=1000))

m = 1000
lst_1000 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("median(lst_1000[:])", globals=globals(), number=25))

"""
Результаты:
0.0010090999999999989, при m = 10
0.015232300000000004, при m = 100
0.0058724, при m = 1000
"""

"""
Вывод:
Встроенная функция показал себя, как самый лучший вариант.
Хуже всех себя показал способ нахождения медианы через сортировку.
"""