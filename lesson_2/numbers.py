import time

# Как пайчарм показывает статус файлов для гитхаба (система контроля версий)
# зеленый - новый файл будет добавлен
# синий - существующий файл изменен (или его местоположение или содержимое)
# красный - не добавлен в репозиторий, существует только локально
# желтый - файл игнорируется (перечислен в .gitignore)

# print(x) это вызывает ошибку
x = 5
print(x)
print(x + 3)

print(type(x))

# int - это тип данных пятерки

print(type(8))

# float - тип данных для 4.5
print(type(9 / 2))

print(type(100 / 3))

print(type(2.5))

# float - это тип данных для десятичных дробей. "Плавающая точка" - происхождение названия float
# главный определяющий фактор - наличие точки
print(type(5.0))

# int - integer это целые числа без точки
x = 5 + 2
x = 7 + 3
x = 5 - 2
x = 7 - 4
x = 5 * 2
x = 10 * 3
x = 10 / 2
# x = 10 \ 5 это вызывает ошибку
x = 5.99
# функция оборачивания в интежер (целое)
x = int(x)
print(x)
# функция оборачивания во флоат
x = float(x)
print(x)

# функция округления
print(round(5.433637123, 2))
print(round(5.438637123, 2))
print(round(6.438637123))
print(round(6.938637123))

x = 7
y = 9
print('y operations')
# уменьшаем у на один, переменная меняет сама себя
y = y - 1
y -= 1
print(y)

# увеличиваем у на один, переменная меняет сама себя
y = y + 1
y += 1
print(y)

y = y * 2
y *= 2
print(y)

y = y / 2
y /= 2
print(y)

# операция деления нацело
z = 9 // 2
print(z)
# операция получения остатка от деления
z = 9 % 2
print(z)

# сразу делает и деление нацело и нахождение остатка от деления
d, m = divmod(9, 2)
# более сложный (ненужный) и подробный вариант получить значения:
dm = divmod(9, 2)
d = dm[0]
m = dm[1]


# оператор возведения в степень
x = 5
print(x ** 2)

# у операций есть порядок выполнения
x = 25 ** 1 / 2
print(x)
x = 25 ** (1 / 2)
print(x)

# функция pow идентична оператору **
print(pow(25, 2))
print(pow(25, 1 / 2))

x = 10 - 100
print(x)
# функция abs - это математический модуль | |
print(abs(x))


timestamp_1 = time.time()
x = 5 ** 23216
timestamp_2 = time.time()
print(timestamp_2 - timestamp_1)