
buy_usd = 40.3
sell_usd = 39.8

user_choice = input("""Выберите одно:
1. Продать USD
2. Купить USD
>>""")

user_usd = input("""Сколько USD?
>>""")
user_usd = float(user_usd)
# str - string / строка
print(type(user_choice))
# = оператор присвоения
# == оператор сравнения
if user_choice == '1':
    uah = round(user_usd * sell_usd, 2)
    print(f'Вы продаёте нам {user_usd} USD, вот ваши {uah} UAH')
if user_choice == '2':
    uah = round(user_usd * buy_usd, 2)
    print(f'Вы покупаете у нас {user_usd} USD, за {uah} UAH')