x = input('Input something: ')
print(type(x))
# годятся чтобы проверить является ли строка целым числом больше ноля.
# отрицательное или десятичное число не узнаёт
print(x.isdigit())
print(x.isnumeric())
print(x.isdecimal())


x = ''
# while type(x) != int:
while not isinstance(x, int):
    # пытаемся
    try:
        x = input('Input integer number: ')
        x = int(x)
    # исключаем и обрабатываем ошибку (указываем какая ошибка. В данном случае - все ошибки)
    except Exception:
        print(f'Your input {x} was incorrect, we expected an integer number')
        # в случае без цикла while, когда за исключением следует код,
        # требующий переменных, которые не получилось объявить - делаем exit()
        # exit(0)
    print(type(x))


x = ''
# while type(x) != float:
while not isinstance(x, float):
    # пытаемся
    try:
        x = input('Input float number: ')
        x = float(x)
    # исключаем и обрабатываем ошибку (указываем какая ошибка. В данном случае - все ошибки)
    except Exception:
        print(f'Your input {x} was incorrect, we expected a float number')
    print(type(x))
