# Создание и заполнение списка
my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)  #return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list comprepfension
my_list_1 = [i for i in range(10)]
print(my_list_1)    # return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Четные числа от 0 до 100
my_list_2 = [i for i in range(101) if i % 2 == 0]
print(my_list_2)