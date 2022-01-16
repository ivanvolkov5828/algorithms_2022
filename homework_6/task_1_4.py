from memory_profiler import memory_usage

def decor(func):
    def wrapper(numbers):
        m1 = memory_usage()
        result = func(numbers)
        m2 = memory_usage()
        mem_dif = m2[0] - m1[0]
        return result, mem_dif
    return wrapper

# Алгоритмы и структуры данных. 3 урок. 1 задание. Скрипт для добавления элементов в список
@decor
def add_to_the_list(lst):
    my_list = list()
    for el in lst:
        my_list.append(el)
    return my_list

res, mem_diff = add_to_the_list(list(range(1000)))
print("Исходный скрипт: ")
print(f"Выполнение заняло {mem_diff} Mib")

# Оптимизация
@decor
def add_to_the_list_new(lst):
    new_list = map(str, lst)
    print(type(new_list))
    print(list(new_list))
    return new_list


res_new, mem_diff_new = add_to_the_list_new(list(range(1000)))
print("Оптимизированный скрипт: ")
print(f"Выполнение заняло {mem_diff_new} Mib")

# Вывод: Оптимизировали за счет функции map(). Добились:
"""
Исходный скрипт: 
Выполнение заняло 0.01171875 Mib
Оптимизированный скрипт: 
Выполнение заняло 0.00390625 Mib
"""