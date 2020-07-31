"""
Функция map(function, iterable) применяет функцию(function) к каждому итерируемому объекту
"""

my_list = [i for i in range(10)] # Создаем список

def plus_5(value: int):     # функция умножает value на 5
    return int(value) * 5

final_list = map(plus_5, my_list)       # применяем функцию к каждому элементу списка
print(list(final_list))     # преобразовываем полученое значение в список и печатаем

# or
my_list_1 = [plus_5(i) for i in my_list]
print(my_list_1)

