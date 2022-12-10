import time


def say_hi():
    print('hi')
    print('hi')


i = 0
# пока условие не перестанет быть правдой
while i < 10:
    # i = i + 1
    i += 1
    print(i)
# наконец-то (то что после цикла)
# infinite loop - вечный цикл. Ситуация, когда условие в цикле никогда не перестаёт быть правдой
# из него можно выйти, некорректно завершив работу программы:
# - кнопка СТОП в пайчарм
# - Закрыть пайчарм
# - если в консоли/терминале (не пайчарм), то Ctrl+C прерывает работу программы
while False:
    print('*')

text = """в
# наконец-то (то что после цикла)
# infinite loop - вечный цикл. Ситуация, когда условие в цикле никогда не перестаёт быть правдой
# из него можно выйти, некорректно завершив работу программы:
# - кнопка СТОП в пайчарм
# - Закрыть пайчарм
# - если в консоли/терминале (не пайчарм), то Ctrl+C прерывает работу программы
"""
search_query = 'в'
print(f'Searching in text for all "{search_query}"')
# while
print('Решение используя break')
search_index = 0
while True:
    search_index = text.find(search_query, search_index)
    say_hi()
    if search_index == -1:
        break
    print(f'{search_query} was found at position {search_index}')
    search_index += 1
    # time.sleep(2)
else:
    print('Из цикла НЕ вышли через break')

print('Решение без break')
# без использованя break, а использует условие в while
search_index = text.find(search_query)
while search_index != -1:
    print(f'{search_query} was found at position {search_index}')
    search_index += 1
    search_index = text.find(search_query, search_index)
else:
    print('Цикл выполнился 0 раз или он закончился без break :)')

#
# step over - переступить
# step into - вступить в функцию (в конце функции вернёмся где были)
# step into my code - вступать только в мои функции (а не библиотечные/служебный/встроенные)
# step out - находясь внутри функции, выйти из неё сразу на уровень выше
# run to cursor - выполнять до курсора
