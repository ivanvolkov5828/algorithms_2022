import time

# декоратор для измерения времени для пункта А
def time_measurement_1(func):
    def timer(*n):
        start_time = time.perf_counter()
        func(*n)
        res = time.perf_counter() - start_time
        return res
    return timer

# функция для добавления элементов в список
@time_measurement_1
def add_to_the_list(*args):
    my_list = list()
    for el in args: # O(n)
        my_list.append(el) # O(1)
    return my_list

# функция для добавления элементов в словарь
@time_measurement_1
def add_to_dictionary(*args):
    my_dict = dict()
    for el in args: # O(n)
        my_dict[el] = el # O(1)
    return my_dict

print("Пункт А: ")
print(add_to_the_list(1, 2, 3, 4))
print(add_to_dictionary(1, 2, 3, 4))

# Вывод: Заполнение списка происходит быстрее, так как для ключей словаря вычисляется хеш

# декоратор для измерения времени для пункта Б
def time_measurement_2(func):
    def timer(arg, pos):
        start_time = time.perf_counter()
        func(arg, pos)
        res = time.perf_counter() - start_time
        return res
    return timer

# функция для изменения элемента списка
@time_measurement_2
def changing_a_list_item(my_list, position):
    my_list[position] = 3 # O(1)
    return my_list

# функция для удаления элемента списка
@time_measurement_2
def deleting_a_list_item(my_list, position):
    del my_list[position] # O(n)
    return my_list

# функция для получения элемента списка
@time_measurement_2
def getting_a_list_item(my_list, position):
    return my_list[position] # O(1)

# функция для изменения элемента словаря
@time_measurement_2
def changing_a_dictionary_element(my_dict, key):
    my_dict[key] = 4 # O(1)
    return my_dict

# функция для удаления элемента словаря
@time_measurement_2
def deleting_a_dictionary_element(my_dict, key):
    del my_dict[key] # O(1)
    return dict

# функция для получения элемента словаря
@time_measurement_2
def getting_a_dictionary_element(my_dict, key):
    return my_dict[key] # O(1)

el_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
el_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
position_lst = 2
key_dct = 4

print("Пункт Б: ")
print(changing_a_list_item(el_list, position_lst))
print(deleting_a_list_item(el_list, position_lst))
print(getting_a_list_item(el_list, position_lst))
print(changing_a_dictionary_element(el_dict, key_dct))
print(deleting_a_dictionary_element(el_dict, key_dct))
key_dct = 5
print(getting_a_dictionary_element(el_dict, key_dct ))

# Вывод: Операции словаря быстрее по причине константной сложности
