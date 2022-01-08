# создадим словарь для хранилища
storage = {
    "Toyota": 278,
    "Amazon": 280.5,
    "Walmart": 524,
    "BP": 278.4,
    "Volkswagen": 275.2
}

# алгоритм № 1 O(n log n)
f = lambda x: x[1] # O(1)
j = 0 # O(1)
dct_1 = {} # O(1)
for key, value in sorted(storage.items(), key = f, reverse=True): # O(n + n log n)
    if j == 3: # O(1)
        break
    else:
        dct_1.setdefault(key, value) # O(1)
        j += 1 # O(1)
print(dct_1)

# алгоритм № 2 O(n^2)
my_list = sorted(storage.values(), reverse=True)  # O(n log n)
max_1 = my_list[0:3]  # O(1)
dct = {} # O(1)
for i in range(len(max_1)):  # O(n)
    for key, value in storage.items():  # O(n)
        if value == max_1[i]: # O(1)
            dct[key] = value  # O(1)
print(dct)

# Вывод: Эффективнее будет первый алгоритм, так как линейно-логарифмическая сложность лучше, чем квадратичная.


