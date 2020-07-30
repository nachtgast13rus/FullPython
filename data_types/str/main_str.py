#  переводим строку 'a4b3c2d8' в aaaabbbccdddddddd
string = 'a4b3c2d8'
for i in string:
    if i.isalpha():
        x = i
    elif i.isdecimal:
        print(x * int(i), end='')

"""Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и 
выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких 
слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми."""

line = 'abc a bCd bC AbC BC BCD bcd ABC'
line_1 = line.lower()
new_line = line_1.split(' ')
print(new_line)
print(line_1.count(new_line[0]))

# with open("file.txt", 'r') as f:
#     s = list(map(lambda i: i.strip('.,!?'), f.read().lower().split()))
#     m = max(sorted(s), key = lambda j: s.count(j))
#     print("%s %d" % (m, s.count(m)))