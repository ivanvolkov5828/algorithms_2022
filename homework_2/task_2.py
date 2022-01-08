def even_odd_numbers(number, k, j):
    if len(str(number)) == 0:
        return f"Четных чисел: {k}\nНечетных чисел: {j}"
    else:
        if int(str(number)[0]) % 2 == 0:
            k += 1
        else:
            j += 1
        return even_odd_numbers(str(number)[1:], k, j)

print(even_odd_numbers(123456, 0, 0))
