# создадим список
numbers = [4, -8, 5, 6, 22, 11, -9, 28, 2, -1, 0, 4, -3]

# алгоритм № 1 O(n^2)
min = 0 # O(1)
for i in range(len(numbers)): # O(n)
    min = numbers[i] # O(1)
    for j in range(len(numbers)): # O(n)
        if numbers[j] < min: # O(1)
            min = numbers[j] # O(1)

print(min)

# алгоритм № 2 O(n)
min_1 = numbers[0] # O(1)
for i in range(1, len(numbers)): # O(n)
    if numbers[i] < min_1: # O(1)
        min_1 = numbers[i]  # O(1)

print(min_1)