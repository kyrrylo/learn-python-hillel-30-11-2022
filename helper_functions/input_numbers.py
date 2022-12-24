

def get_int_from_user(comment: str, lower_bound: int = float('-inf'), upper_bound: int = float('inf')) -> int:
    """
    Считывает int у пользователя, входящий в заданные рамки от lower_bound до upper_bound
    Считывает до тех пор, пока верное значение не было получено
    :param comment: обращение к пользователю
    :param lower_bound: нижнее допустимое значение
    :param upper_bound: верхнее допустимое значение
    :return: полученное верное integer значение
    """
    while True:
        # пытаемся
        try:
            x = input(f'{comment} ')
            x = int(x)
            if x < lower_bound or x > upper_bound:
                # вызов исключений самостоятельно
                raise ValueError
            # команда return возвращает результат работы функции
            return x
        # исключаем и обрабатываем ошибку (указываем какая ошибка. В данном случае - все ошибки)
        except Exception:
            print(f'Введите корректное значение от {lower_bound} до {upper_bound}')


# При проекте где используется больше одного файла
# во всех файлах НЕ ДОЛЖНО быть кода кроме этих четырех случаев:
# 1. код import'a
# 2. код-объявление переменных-констант (их обычно пишут с большой буквы)
# 3. код в функциях
# 4. код внутри "if __name__ == '__main__':"
if __name__ == '__main__':
    print(f'My file name is {__name__}')
