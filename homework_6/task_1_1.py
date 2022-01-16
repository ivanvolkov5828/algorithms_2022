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
def add_to_the_list(numbers):
    my_list = list()
    for el in numbers:
        my_list.append(el)
    return my_list

res, mem_diff = add_to_the_list([1, 2, 3, 4])
print("Исходный скрипт: ")
print(f"Выполнение заняло {mem_diff} Mib")

# Оптимизация
@decor
def add_to_the_list_new(numbers):
    for el in numbers:
        yield el

my_generator, mem_diff = add_to_the_list_new([1, 2, 3, 4])
#for i in my_generator:
        #print(i)
print("Оптимизированный скрипт: ")
print(f"Выполнение заняло {mem_diff} Mib")

# Вывод: Оптимизировали скрипт за счет ленивых вычислений. Добились:
"""
Исходный скрипт: 
Выполнение заняло 0.01171875 Mib
Оптимизированный скрипт: 
Выполнение заняло 0.0 Mib
"""