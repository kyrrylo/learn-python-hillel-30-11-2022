# ветвление - процесс производный от условных выражений

x = 5
y = 6

print(type(x / y))

print(type(x > y))
# bool - да или нет, правда или не правда, True or False
print(type(True))
print(type(False))

# примеры сравнения чисел (конвертирования их у тип булеан или флаг)
print('Int or float')
print(type(x < y))
print(type(x == y))
print(type(x != y))
print(type(x <= y))
print(type(x >= y))

print('Strings')
print(type('a' in 'Ukraine'))
print(type('Ukraine' in 'I live in Ukraine'))
# is - "является ли" ответ - да/нет True/False
print(type('Ukraine'.islower()))
print(type('Ukraine'.isupper()))
print(type('Ukraine'.isspace()))

if 5:
    print('Пять так пять :)')
else:
    print('Ну, не пять :(')
# при проверке значений проверяется не-пустота
print(bool(20))
print(bool(-0.0000001))
print(bool(0))
print(bool(''))
print(bool('a'))

s = 'Python'
s = ''
if s:
    print(s[-1])
else:
    print('String s is empty')
