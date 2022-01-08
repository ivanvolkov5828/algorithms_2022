def calculator():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    sign = input("Введите знак: ")
    number = 0
    try:
        if sign == '0':
            return
        elif sign == '+':
            number = a + b
        elif sign == '-':
            number = a - b
        elif sign == '*':
            number = a * b
        elif opr == '/':
            number = a / b
        else:
            print('Такого знака не существует')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    print(number)
    return calculator()
calculator()