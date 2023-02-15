# None - пустота, неопределённость


def count_to(n: int = None):
    if isinstance(n, type(None)):
        print('Ничего не пришло!')
    else:
        pass


if __name__ == '__main__':
    x = 0
    print(type(None))
    # None - undefined, пустышка, не сравнима ни с одним типом
    if 5 == 5.0:
        print('equal')
    if isinstance(5, type(5.0)):
        print('types equal')


# int, float + - * / // % **
# str + * strip/split/join/find/rfind
# list - сортировки и фиксирования порядка, накопления
# set - хороши для поиска
# tuple - нельзя менять после создания. При этом занимают меньше места, чем list, dict, set
# dict - хороши для поиска, имеют пару
# def -> return, generator -> yield
# классы - объединяет в себе всё
