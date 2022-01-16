from random import randint
from timeit import timeit

def get_median(lst_obj, n):
    for i in range(n):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)


m = 10
lst_10 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("get_median(lst_10[:], m)", globals=globals(), number=1000))

m = 100
lst_100 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("get_median(lst_100[:], m)", globals=globals(), number=1000))

m = 1000
lst_1000 = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("get_median(lst_1000[:], m)", globals=globals(), number=25))

"""
Результаты:
0.0069706, при m = 10
0.38756660000000004, при m = 100
1.1691927, при m = 1000
"""