menu_cafe = [
    {
        "name": "Американо",
        "price": 30
    },
    {
        "name": "Раф",
        "price": 40
    },
    {
        "name": 'Чай "Альпийские луга"',
        "price": 25
    },
    {
        "name": "Чай облепиховый",
        "price": 30
    },
    {
        "name": "Печеньки",
        "price": 5
    },
    {
        "name": "Круассан",
        "price": 25
    },
    {
        "name": "Пончики",
        "price": 20
    }
]


def display_menu():
    print('Меню')
    for i, element in enumerate(menu_cafe):
        print(f'  {i + 1}. {element["name"]:25}{element["price"]:5.2f} UAH ')
    print(f'  {len(menu_cafe) + 1}. Выход')


def purchase_from_menu():
    global pocket_size
    display_menu()
    exit_index = len(menu_cafe) + 1
    print(f'У вас есть {pocket_size:6.2f} UAH. Что будете заказывать?')
    menu_index = get_int_from_user('> ', lower_bound=1, upper_bound=exit_index)
    if menu_index == exit_index:
        print(f'Приходите еще, будем рады вас видеть!')
        exit(0)
    menu_item = menu_cafe[menu_index - 1]
    pocket_size -= menu_item["price"]
    print(f'Сейчас вам будет подано {menu_item["name"]}, пожалуйста ожидайте. Желаете что-нибудь еще?')


def get_int_from_user(comment: str, lower_bound: int = -9999999, upper_bound: int = 9999999) -> int:
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


if __name__ == '__main__':
    pocket_size = 100
    while True:
        purchase_from_menu()
