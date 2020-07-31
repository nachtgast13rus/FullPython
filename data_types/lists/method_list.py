my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# my_list.append(x)     Добавляет в конец списка х
my_list.append(9)
print(my_list)  # return [1, 2, 3, 4, 5, 6, 7, 8, 9]

# del my_list[x]        Удаляет элемент с индексом x
del my_list[4]
print(my_list)  # return [1, 2, 3, 4, 6, 7, 8, 9]

# my_list.pop(x)        Удаляет и ВОЗВРАЩЯЕТ элемент с индексом х
index_2 = my_list.pop(2)
print(index_2)  # return 3
print(my_list)  # return [1, 2, 4, 6, 7, 8, 9]


# my_list.insert(x, y)      Вставляет значение y на индекс х
my_list.insert(2, 3)    # элемент 3 в индекс 2
print(my_list)  # return [1, 2, 3, 4, 6, 7, 8, 9]

# my_list.remove(x)     Удаляет элемент по ЗНАЧЕНИЮ (не по индексу)
my_list.remove(8)   # Удаляем из списка цифру 8
print(my_list)  # return [1, 2, 3, 4, 6, 7, 9]

# my_list.extend(x, y, z)
my_list.extend([10, 11, 12])    # Добавляет множество значений в конец списка
print(my_list)  # return [1, 2, 3, 4, 6, 7, 9, 10, 11, 12]

my_list = [2, 3, 5, 7, 5, 2, 7, 5, 3, 5, 9, 5, 1, 4]
my_list.sort()      # Сортирует и изменяет список
print(my_list)  # return [1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 7, 7, 9]
my_list.reverse()       # Выводит список задом наперед и изменяет его
print(my_list)  # return [9, 7, 7, 5, 5, 5, 5, 5, 4, 3, 3, 2, 2, 1]
