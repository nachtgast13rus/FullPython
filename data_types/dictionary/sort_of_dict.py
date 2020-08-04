"""словари являются не сортироваными последовательностями, но их можно отсортировать по ключам"""
my_dict = {'a': 1,
           'b': 2,
           'c': 3,
           'd': 4,
           'e': 5,
           'f': 6,
           'g': 7}
print(my_dict)

# 1 способ
list_key = list(my_dict.keys()) # создаем список ключей
list_key.sort() # сортируем его
for key in list_key:    # идем по списку с ключами
    print(key, '=>', my_dict[key])  # выводим значения из словаря соотв. списку ключей

# or
for key in sorted(my_dict):
    print(key, '=>', my_dict[key])