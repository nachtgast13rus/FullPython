"""
полезная библиотека для определения времени выполнения кусков кода
"""

import timeit

def my_list_x():
    my_list = []
    for i in range(999999):
        my_list.append(i)
    return my_list

def my_list_y():
    my_list_1 = [i for i in range(999999)]
    return my_list_1

print(timeit.timeit(my_list_x, number=100)) # result 19.149796969
print(timeit.timeit(my_list_y, number=100)) # result 13.198887718000002
