from collections import defaultdict

num_1 = 'A2'
num_2 = 'C4F'
my_dict = defaultdict(list)

def full_dict(num):
    for el in num:
        my_dict[num].append(el)

def get_sum(a, b):
    result = hex(int(a, 16) + int(b, 16))[2:].upper()
    if result not in my_dict:
        for i in result:
            my_dict[result].append(i)
    return result

def get_mul(a, b):
    result = hex(int(a, 16) * int(b, 16))[2:].upper()
    if result not in my_dict:
        for i in result:
            my_dict[result].append(i)
    return result

full_dict(num_1)
full_dict(num_2)
print(get_sum(num_1, num_2))
print(get_mul(num_1, num_2))
print(my_dict)
