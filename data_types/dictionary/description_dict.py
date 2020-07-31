"""
Словари изменяемые неупорядоченный последовательности по типу ключь: значение
"""

my_dict = {'name': 'dimon', 'age': 35, 'color': 'blue'}  # создаем словарь
my_dict['aka'] = 'nachtgast'    # добавляем новое ключь-значение
print(my_dict)
print(my_dict['color'])


#  еще варианты создания
mywife_dict = dict(name='Katya', age=35, color='green', aka='muchmuch')
print(mywife_dict)
myson_dict = dict(zip(['name', 'age', 'color', 'aka'],
                      ['danila', 14, 'red', 'mitkoon']))
print(myson_dict)

# словарь в словаре
my_family = {'my_name': {'first': 'dmitry', 'last': 'tygushev'},
             'wife_name': {'first': 'ekaterina', 'last': 'tygusheva'},
             'son_name': {'first': 'daniil', 'last': 'tygushev'},
             'daughter_name': {'first': 'alisa', 'last': 'tygusheva'}}
print(my_family)
print(my_family['son_name']['first'])
my_family['son_name']