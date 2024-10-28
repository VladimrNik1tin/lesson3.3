# 1. Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()  # Вывод значений параметров
print('--------------------------------')

# Вызываем функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(2, 'столбец', False)
print_params(3, 'None')
print_params(a='один', b='два', c='три')
print_params(a='один', b='два')
print_params(b='два', c='три')
print_params(a='один', c='три')
print_params(a='один')
print_params(b='два')
print_params(c='три')
print_params()  # Вывод функции без аргументов
print('--------------------------------')

# Проверяем, работают ли вызовы print_params(b = 25) и print_params(c = [1,2,3])
print_params(b=25)
print_params(c=[1, 2, 3])
print('--------------------------------')

# 2. Распаковка параметров:
values_list = [1, 'строка', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)
print('--------------------------------')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)