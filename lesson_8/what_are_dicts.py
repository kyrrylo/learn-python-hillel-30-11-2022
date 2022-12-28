# dictionary - словарь, хэш-таблица

d = dict()
print(d, type(d))

s = {1, 2}
print(s, type(s))

x = "ключ1"
d = {
    x: "значение1",
    "ключ2": "значение2",
    "ключ2": "значение3",
    "ключ3": "значение3",
    1: 2,
    2: "значение1",
    "ключ4": 5,
    "room": "bathroom",
    True: 4,  # оказывается конвертируется в 1, лучше не использовать
    False: "false",
    # [1, 2, 3]: 5  # такие типы данных как список (и другие динамические типы) как ключ словаря использовать нельзя
    # {1, 2, 3}: 4,
    (1, 2, 3): 3,
}

# keys (ключи) повторяться не могут (они перетирают/перезаписывают друг друга если повторяются)
# values (значения) повторяться запросто могут, с этим никаких проблем
print(d, type(d))

l = [2, 5, 3]
print(l[1])
# print(l[5]) # error - cant access whats not there
# l[5] = 8  # error - cant assign whats not there
l[1] = 8
print(l)

print(d['ключ2'])  #
print(d[1])  # ключ 1 есть и в нём есть значение
# print(d['значение1'])  # Работает только с ключами, имея значения ключ не получишь (билет в один конец)
# в отличие от списка, в словарь можно добавлять новые элементы по ключу
# как в списке, так и в словаре, можно изменять существующие индексы/ключи

d[5] = 'new element'
print(d[5])
print(len(d))

print(d.keys(), list(d.keys()))
for key in d.keys():
    print(key, d[key])

print(d.values(), type(d.values()), list(d.values()), type(list(d.values())))

print(d.items())

d2 = dict(d.items())
d2 = dict([('room', 'bathroom'), ('house', 'cottage')])
print(d2, type(d2))

# два способа создать словарь
# 1. Вручную перечислить пары ключ значения (могут быть переменные)
# 2. Пользуясь dict(), передать туда список кортежей из двух элементов

if 'room' in d2:
    print('room is in d2')
else:
    print('room is not in d2')

if 'bathroom' in d2:
    print('Key bathroom is in d2')
else:
    print('Key bathroom is not in d2')

if '555' in d2:
    print('Key 555 is in d2')
else:
    print('Key 555 is not in d2')

# set, dict - операция поиска "in" очень быстрая и эффективная
# list, tuple - операция поиска "in" неэффективная, прибегать в крайних случаях (или на заведомо маленьких списках/кортежах)


