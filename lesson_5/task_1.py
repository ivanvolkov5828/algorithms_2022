from collections import namedtuple

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

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def average_profit(lst, n, func):
    sum = 0
    ans_1 = ''
    ans_2 = ''

    for el in lst:
        sum += func(list(map(int, el.profit_c.split(" "))))
    average = sum/n

    for el in lst:
        param = list(map(int, el.profit_c.split(" ")))
        sum_param = func(param)
        if sum_param > average:
            ans_1 += el.name_c + ", "
        else:
            ans_2 += el.name_c + ", "


    return f"Средняя годовая прибыль всех предприятий: {average}", f"Предприятия, с прибылью выше среднего значения: {ans_1}", f"Предприятия, с прибылью ниже среднего значения: {ans_2}"



number = int(input("Введите количество предприятий для расчета прибыли: "))
companies = list_of_companies(number)
print(average_profit(companies, number, sum_numbers))