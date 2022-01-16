from collections import namedtuple
from recordclass import recordclass
from memory_profiler import memory_usage

def decor(func):
    def wrapper(numbers):
        m1 = memory_usage()
        result = func(numbers)
        m2 = memory_usage()
        mem_dif = m2[0] - m1[0]
        return result, mem_dif
    return wrapper

# Алгоритмы и структуры данных. 5 урок. 1 задание. Скрипт для создания именованного кортежа с прибылью и названием компании.
@decor
def list_of_companies(n):
    company = namedtuple('company', 'name_c profit_c')
    companies = []

    for i in range(n):
        name = input("Введите название предприятия: ")
        profit = input("Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): ")
        company_template = company(
            name_c = name,
            profit_c = profit
        )
        companies.append(company_template)
    return companies

number = int(input("Введите количество предприятий для расчета прибыли: "))
res, mem_diff = list_of_companies(number)
print("Исходный скрипт: ")
print(f"Выполнение заняло {mem_diff} Mib")

# Оптимизация
@decor
def list_of_companies_new(n):
    company = recordclass('company', 'name_c profit_c')
    companies = []

    for i in range(n):
        name = input("Введите название предприятия: ")
        profit = input("Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): ")
        company_template = company(
            name_c = name,
            profit_c = profit
        )
        companies.append(company_template)
    return companies

res_new, mem_diff_new = list_of_companies_new(number)
print("Оптимизированный скрипт: ")
print(f"Выполнение заняло {mem_diff_new} Mib")

# Вывод: Оптимизировали за счет recordclass. Добились:
"""
Исходный скрипт: 
Выполнение заняло 0.0078125 Mib
Оптимизированный скрипт: 
Выполнение заняло 0.00390625 Mib
"""