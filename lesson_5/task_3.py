from collections import deque
from timeit import timeit

lst_obj = [1, 2, 3, 4, 5]
deq_obj = deque(lst_obj)
elem = 1
elem_1 = [7, 7, 7]


# 1 часть задания
# добавление в список
def add_to_the_list(lst, el):
    lst.append(el)
    return lst


# удаление из списка
def remove_from_the_list(lst):
    lst.pop()
    return lst


# добавление extend
def extend_lst(lst, el):
    lst.extend(el)
    return lst


# добавление в дек
def add_to_deque(d, el):
    d.append(el)
    return d


# удаление из дека
def remove_from_the_deque(d):
    d.pop()
    return d


# добавление extend
def extend_deque(d, el):
    d.extend(el)
    return d

print("Часть 1")
print("append для списка: ", timeit("add_to_the_list(lst_obj, elem)", globals=globals()))
print("append для дека: ", timeit("add_to_deque(deq_obj, elem)", globals=globals()))
print("pop для списка: ", timeit("remove_from_the_list(lst_obj)", globals=globals()))
print("pop для дека: ", timeit("remove_from_the_deque(deq_obj)", globals=globals()))
print("extend для списка: ", timeit("extend_lst(lst_obj, elem_1)", globals=globals()))
print("extend для дека: ", timeit("extend_deque(deq_obj, elem_1)", globals=globals()))


# Вывод: Одинаковые операции(append и append, pop и pop, extend и extend) у списка и дека происходят примерно за одно и
# то же время.

# Часть 2.

# appendleft у дека
def appendleft_deque(d):
    d.appendleft(1)
    return d

# popleft у дека
def popleft_deque(d):
    d.popleft()
    return d

# extendleft у дека
def extendleft_deque(d, el):
    d.extendleft(el)
    return d

# у списка
def ins_lst(lst):
    lst.insert(0, 'asd')
    return lst

def pop_lst(lst):
    lst.pop(0)
    return lst

def extend_lst(lst, el):
    for i in el:
        lst.insert(0, i)
    return lst

print()
print("Часть 2")
print("appendleft у дека: ", timeit("appendleft_deque(deq_obj)", globals = globals(), number=2000))
print("аналогичная операция у списка: ", timeit("ins_lst(lst_obj)", globals = globals(), number=2000))
print("popleft у дека: ", timeit("popleft_deque(deq_obj)", globals = globals(), number=2000))
print("аналогичная операция у списка: ", timeit("pop_lst(lst_obj)", globals = globals(), number=2000))
print("extendleft у дека: ", timeit("extendleft_deque(deq_obj, elem_1)", globals = globals(), number=2000))
print("аналогичная операция у списка: ", timeit("extend_lst(lst_obj, elem_1)", globals = globals(), number=2000))

# Вывод: Операции у дека выполняются существенно быстрее, чем у списка

# Часть 3.

# получение элемента из списка
def getting_a_list_item(lst, i):
    return lst[i]

# получение элемента из словаря
def getting_an_element_from_deque(d, i):
    return d[i]

print()
print("Часть 3")
print("получение элемента из списка: ", timeit("getting_a_list_item(lst_obj, 2)", globals = globals()))
print("получение элемента из дека: ", timeit("getting_an_element_from_deque(deq_obj, 2)", globals = globals()))

# Вывод: Получение по индексу в списке быстрее чем в деке
