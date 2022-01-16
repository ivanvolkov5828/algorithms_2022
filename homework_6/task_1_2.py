from pympler import asizeof
import time

# Основы языка Python. 9 урок. 1 задание. ООП. Создание класса светофор
class TrafficLight:
    __color = 0

    def __init__(self, red, yellow, green):
        self.__color = red
        self.yellow = yellow
        self.green = green

    def running(self):
        if self.__color == "Red":
            print(self.__color, end="")
            time.sleep(7)
            print('\r', end='')
        else:
            print("Ошибка! Должен быть красный цвет")

        if self.yellow == "Yellow":
            print(self.yellow, end="")
            time.sleep(2)
            print('\r', end='')
        else:
            print("Ошибка! Должен быть желтый цвет")

        if self.green == "Green":
            print(self.green, end="")
            time.sleep(3)
            print('\r', end='')
        else:
            print("Ошибка! Должен быть зеленый цвет")

light = TrafficLight("Red", "Yellow", "Green")
# light.running()
print(asizeof.asizeof((light)))

# Оптимизация
class TrafficLight1:
    __slots__ = ['red', 'yellow', 'green', '__color']

    def __init__(self, red, yellow, green, __color):
        self.__color = red
        self.yellow = yellow
        self.green = green

    def running(self):
        if self.__color == "Red":
            print(self.__color, end="")
            time.sleep(7)
            print('\r', end='')
        else:
            print("Ошибка! Должен быть красный цвет")

        if self.yellow == "Yellow":
            print(self.yellow, end="")
            time.sleep(2)
            print('\r', end='')
        else:
            print("Ошибка! Должен быть желтый цвет")

        if self.green == "Green":
            print(self.green, end="")
            time.sleep(3)
            print('\r', end='')
        else:
            print("Ошибка! Должен быть зеленый цвет")

light_1 = TrafficLight1("Red", "Yellow", "Green", 0)
# light.running()
print(asizeof.asizeof((light_1)))

# Вывод: Оптимизировали за счет слотов. Добились:
"""
504
232
Уменьшения в 2 раза
"""