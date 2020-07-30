""" Индексы и нарезка"""

""" Индексы начинаются с 0 если слева направо и с -1 если в обратном направлении"""

string = 'qwertyuiopasdfghjklzxcvbnm'

print(string[0])  # return q
print(string[5])  # return y
print(string[-1])  # return m
print(string[5:])  # return все символы начиная с 5 индекса и до конца
print(string[0: 3])  # return с 0 индекса до 3
print(string[:3])  # return тоже самое
print(string[:: -1])  # наоборот
