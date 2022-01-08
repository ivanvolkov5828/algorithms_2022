from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]

def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3():
    return max(set(array), key=array.count)

print("Время работы первой функции: ", timeit(f'func_1()', globals=globals()))
print("Время работы второй функции: ", timeit(f'func_2()', globals=globals()))
print("Время работы третьей функции: ", timeit(f'func_3()', globals=globals()))

"""
Время работы первой функции:  2.0789231999999997
Время работы второй функции:  2.3646753
Время работы третьей функции:  1.1101377000000001
"""

# Быстрее всего работает моя функция, так как используется только max. Медленнее работает первая функция из-за цикла,
# метода count(). И хуже всего вторая функция так как цикл, append(), max(), index(), count(), все это требует время.
# Из замеров можно седлать вывод, что у меня получилось ускорить задачу.

