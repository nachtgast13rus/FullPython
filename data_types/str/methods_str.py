""" Методы строк"""

string = 'Evgen is a good man'

# string.find(x)        Поиск индекса первого появления х
print(string.find('o')) # return 12

# string.replace(x, y)      Заменить в string подстроку x на y
string = string.replace('good man', 'foggot')
print(string)