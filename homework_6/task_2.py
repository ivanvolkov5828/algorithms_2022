from memory_profiler import profile


def memory(func):
    @profile
    def wrapper(*args):
        return func(args)
    return wrapper


@memory
def sum_recursion_decorator(num, lst=[0, 0]):
    lst[0 if (num % 10) % 2 == 0 else 1] += 1
    if num < 10:
        return lst
    return sum_recursion(num // 10, lst)

def sum_recursion(num, lst=[0, 0]):
    lst[0 if (num % 10) % 2 == 0 else 1] += 1
    if num < 10:
        return lst
    return sum_recursion(num // 10, lst)


@profile
def foo():
    print(f'Количество четных и нечетных цифр в числе равно: {sum_recursion(int(input("Введите число:")))}')

if __name__ == '__main__':
    foo()
    print(f'Количество четных и нечетных цифр в числе равно: {sum_recursion_decorator(int(input("Введите число:")))}')

"""
Проблема в том, что декоратор вызывается для каждого вызова декорируемой функции
Решение: обернуть вызывающий код в функцию.
Можно не использовать декоратор, использовать например memory_usage
Можно декорировать функцию wrapper в декораторе. 
"""
