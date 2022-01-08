from timeit import timeit

def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

def eratosfen(n):
    sieve = list(range(100000))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1[n-1]

print("simple()")
print("10: ", timeit("simple(10)", globals=globals(), number=100))
print("100: ", timeit("simple(100)", globals=globals(), number=100))
print("1000: ", timeit("simple(1000)", globals=globals(), number=100))

print("eratosfen()")
print("10: ", timeit("eratosfen(10)", globals=globals(), number=100))
print("100: ", timeit("eratosfen(100)", globals=globals(), number=100))
print("1000: ", timeit("eratosfen(1000)", globals=globals(), number=100))

"""
simple()
10:  0.003162999999999999
100:  0.2834741
1000:  60.1908114

eratosfen()
10:  3.416387499999999
100:  3.372660599999996
1000:  3.5718075999999996
"""

# Вывод: Чем больше порядковый номер простого числа, тем эффективнее «Решето Эратосфена»,
#  первый алгоритм эффективнее использовать с порядковыми номерами простых чисел до 100.