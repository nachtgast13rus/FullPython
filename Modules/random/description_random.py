"""Описание функций модуля random"""

import random

# random.random()       генерирует случайное число от 0.0 до 1.0
print(random.random())

# random.randint(min, max)      возвращает случайное целое число в промежутке между  min и max(вкл)
print(random.randint(1, 10))

# random.randrange(start, stop, step)       возвращает случайное целое число из определенного набора чисел
print(random.randrange(10))  # return от 0 до 9
print(random.randrange(5, 10))  # return от 5 до 9
print(random.randrange(5, 100, 3))  # return от 5 до 99 с шагом 3

# random.shuffle        перемешивает список случайным образом
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# random.choice()       возвращает один случайный элемент из списка
print(random.choice(numbers))