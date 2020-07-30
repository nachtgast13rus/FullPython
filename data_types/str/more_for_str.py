""" Строки неизменяемы!
но можно изменить строку с помощью списка"""

string = 'Hello World'
# string[0] = 'P' # return error
string_list = list(string) # Преобразуем строку в список
string_list[0] = 'P' # Меняем нужный элемент
string_1 = ''.join(string_list) # Преобразуем список в строку
print(string, string_1, sep='\n')

# Or
new_string = bytearray(b'Evgen')
new_string.extend(b' is foggot')
new_string = new_string.decode()
print(new_string)

# вместо экранирования символов в пути к файлу
with open('C:\\dataset.txt') as text:
    print(text.read())
# можно сделать так
with open(r'C:\dataset.txt') as text:
    print(text.read())