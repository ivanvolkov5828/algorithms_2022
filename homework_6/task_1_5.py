from memory_profiler import memory_usage

def memory(func):
    def wrapper(*args):
        m1 = memory_usage()
        result = func(*args)
        m2 = memory_usage()
        mem_dif = m2[0] - m1[0]
        return result, mem_dif
    return wrapper

# Алгоритмы и структуры данных. 4 урок. 1 задание. Скрипт, который позволяет сохранить в
# массиве индексы четных элементов другого массива

# Исходный код:
@memory
def func_1(nums):
    arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return arr

res, mem_diff = func_1(list(range(5000000)))
print("Исходный скрипт: ")
print(f"Выполнение заняло {mem_diff} Mib")

# Оптимизированный код:
@memory
def func_2(nums):
    arr = filter(lambda x: x % 2 == 0, nums)
    return arr

res_new, mem_diff_new = func_2(list(range(5000000)))
print("Оптимизированный скрипт: ")
print(f"Выполнение заняло {mem_diff_new} Mib")

# Вывод: Оптимизировали за счет функции filter(). Добились:
"""
Исходный скрипт: 
Выполнение заняло 97.3046875 Mib
Оптимизированный скрипт: 
Выполнение заняло 0.0 Mib
"""