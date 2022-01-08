from random import randint
def game(number, attempts=1):
    param = int(input(f'Попытка: {attempts}. Введите число: '))

    if attempts == 10:
        return f"Вы были близки, загаданное число это {number}"
    elif param == number:
        return f"Поздравляю, вы угадали!"

    if param < number:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")

    return game(number, attempts + 1)

print(game(randint(0, 100)))
