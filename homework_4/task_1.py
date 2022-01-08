from timeit import timeit

# исходная функция
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# моя функция № 1
def func_2(nums):
    arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return arr

# моя функция № 2
def func_3(nums):
    arr = [i for i in range(0, len(nums), 2)]
    return arr

numbers = [i for i in range(101)]

print("Замер времени для исходной функции: ", timeit("func_1(numbers)", globals=globals(), number=100000))
print("Замер времени для моей функции: ", timeit("func_2(numbers)", globals=globals(), number=100000))
print("Замер времени для моей второй функции: ", timeit("func_3(numbers)", globals=globals(), number=100000))

# Аналитика: Видим, что моя первая функция выполняется быстрее исходной, так как используем lc. В свою очередь
# моя вторая функция выполняется быстрее, чем предыдущие, так как она без условия, а просто с другим шагом в range().
