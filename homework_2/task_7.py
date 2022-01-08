def formula(number):
    if number == 0:
        return number

    return number + formula(number - 1)

print(formula(5) == (5 * (5 + 1)) / 2 )
