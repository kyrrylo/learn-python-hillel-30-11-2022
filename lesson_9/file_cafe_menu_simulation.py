import json


def load_menu_json(json_filename: str) -> list:
    """
    Читает меню из json-файла, возвращает меню в формате списка
    :param json_filename: джсон файл с меню
    :return: меню в формате списка словарей
    """
    return json.load(open(json_filename, encoding='utf-8'))


def load_menu(filename: str) -> list:
    """
    Читает меню из файла, возвращает меню в формате списка
    :param filename: файл с меню
    :return: меню в формате списка
    """
    menu_cafe = []
    with open(filename, encoding='utf-8', mode='r') as f:
        for menu_item in f.readlines():
            try:
                name, price = menu_item.strip().split(':')
                price = float(price)
                menu_cafe.append({
                    "name": name,
                    "price": price
                })
            except Exception:
                # парсинг - процесс конвертирования обычной строки в осмысленные и важные для программы значения (бизнес логику)
                print(f'Не удалось распарсить строку меню: {menu_item}')
    return menu_cafe


def display_menu(menu_cafe: list):
    print('Меню')
    for i, element in enumerate(menu_cafe):
        print(f'  {i + 1}. {element["name"]:25}{element["price"]:5.2f} UAH ')
    print(f'  {len(menu_cafe) + 1}. Выход')


def purchase_from_menu(menu_cafe: list):
    global pocket_size
    display_menu(menu_cafe)
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
    # menu = load_menu('cafe_menu.txt')
    menu = load_menu_json('cafe_menu.json')
    while True:
        purchase_from_menu(menu)
