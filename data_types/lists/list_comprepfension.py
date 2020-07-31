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

# сортировка по символам
string = 'Я узнал что у меня, есть огромная семья!' # создаем строку
my_list_3 = [i for i in string if i not in 'аеуи']  # список символов строки если их нет в 'аеуи"
my_string = ''.join(my_list_3)  # из списка делаем строку
print(my_string)

my_list_4 = [-1, 2, -3, 4, -5, 6]
new_my_list_4 = [i if i > 0 else 0 for i in my_list_4]  # если элемент больше 0 то элемент иначе 0
new_1_my_list_4 = [i for i in new_my_list_4 if i != 0]  # убираем нули
print(new_1_my_list_4)