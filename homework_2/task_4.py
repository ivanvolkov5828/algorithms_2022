def summer(num, s = 0, halved = 1, count = 0):
    if count == num:
        return f'Количество элементов: {num}\nСумма: {s}'
    count += 1
    return summer(num, s + halved, halved / -2, count)

print(summer(3))


