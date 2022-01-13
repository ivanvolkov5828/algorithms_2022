from collections import OrderedDict
from timeit import timeit

my_dict = {}
my_ordered_dict = OrderedDict()

# добавление элемента
def adding_to_the_dictionary():
    my_dict[1] = 1
    my_dict[2] = 2
    return my_dict

def adding_to_an_ordered_dictionary():
    my_ordered_dict[1] = 1
    my_ordered_dict[2] = 2
    return my_ordered_dict

# удаление элемента
def deleting_from_the_dictionary():
    for i in range(100):
        my_dict[i] = i
        my_dict.popitem()

def deleting_from_an_ordered_dictionary():
    for i in range(100):
        my_ordered_dict[i] = i
        my_ordered_dict.popitem()


print("Добавление элемента в обычный словарь: ", timeit("adding_to_the_dictionary()", globals = globals(), number = 2000))
print("Добавление элемента в упорядоченный словарь: ", timeit("adding_to_an_ordered_dictionary()", globals = globals(), number = 2000))
print("Удаление элемента из обычного словаря: ", timeit("deleting_from_the_dictionary()", globals = globals(), number = 2000))
print("Удаление элемента из упорядоченного словаря: ", timeit("deleting_from_an_ordered_dictionary()", globals = globals(), number = 2000))

"""
Вывод:  Стандартный dict быстрее.
        OrderedDict можно использовать, если важен порядок элементов. 
        Также в нем легко контролировать порядок (move_to_end(), popitem()).
        Можно сравнивать полную эквивалентность словарей.
"""