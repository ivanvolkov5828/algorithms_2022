from random import randint
from timeit import timeit

# гномья сортировка
def gnome_sort(lst_obj):
    idx = 1
    i = 0
    n = len(lst_obj)
    while i < n - 1:
        if lst_obj[i] <= lst_obj[i + 1]:
            i, idx = idx, idx + 1
        else:
            lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
            i = i - 1
            if i < 0:
                i, idx = idx, idx + 1
    return lst_obj

def get_median(lst_obj, n):
    gnome_sort(lst_obj)
    return lst_obj[n]

m = 10
lst_10 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("get_median(lst_10[:], m)", globals=globals(), number=1000))

m = 100
lst_100 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("get_median(lst_100[:], m)", globals=globals(), number=1000))

m = 1000
lst_1000 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("get_median(lst_1000[:], m)", globals=globals(), number=30))

"""
Результаты:
0.030328900000000006, при m = 100
3.3495991999999997, при m = 100
10.9054207, при m = 1000
"""
