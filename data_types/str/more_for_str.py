""" Строки неизменяемы!
но можно изменить строку с помощью списка"""

string = 'Hello World'
# string[0] = 'P' # return error
string_list = list(string) # Преобразуем строку в список
string_list[0] = 'P' # Меняем нужный элемент
string = ''.join(string_list) # Преобразуем список в строку
print(string)