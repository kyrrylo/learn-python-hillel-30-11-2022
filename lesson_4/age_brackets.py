# conditional statements
# условные выражения
"""
тут только только одно из условий будет выполнено (первое правдивое)
if <condition>:
    <body of if>
elif <condition>:
    < body of elif >
elif <condition>:
    < body of elif >
...
elif <condition>:
    < body of elif >
else:
    < body of else>
*to be continued*

тут каждое условие может быть выполнено
if <condition>:
    <body of if>
if <condition>:
    <body of if>
if <condition>:
    <body of if>
if <condition>:
    <body of if>
"""

# 0-6 лет - ребёнок
# 6-18 лет - школьник(ца)
# 18-23 лет - студент(ка)
# 23-30 лет - юноша/девушка
# 30-65 лет - мужчина/женщина
# 65-90 лет - дедушка/бабушка
# 90+ лет - долгожитель

# while - пока
while True:
    try:
        user_input = input('Сколько вам полных лет? (или введите exit чтобы выйти) ')
        if user_input.lower() == 'exit':
            exit(0)
            quit(0)
        age_of_user = int(user_input)
        if age_of_user < 0:
            print('Ваш возраст отрицательный, с вами точно всё в порядке?')
        if 0 <= age_of_user < 6:
            print('Вы ребёнок!')
        if 6 <= age_of_user < 18:
            print('Вы школьник или школьница!')
        if 18 <= age_of_user < 23:
            print('Вы студент или студентка!')
        if 23 <= age_of_user < 30:
            print('Вы юноша или девушка!')
        if 30 <= age_of_user < 65:
            print('Вы взрослый!')
        if 65 <= age_of_user < 90:
            print('Вы дедушка или бабушка!')
        if age_of_user >= 90:
            print('Вы долгожитель!')
    except Exception:
        print('Возраст должен быть числом!')
        # ключевое слово, используется внутри циклов. Означает прервать текущую итерацию и начать всё с начала
        # (переход к первой строке тела цикла)
        continue




if age_of_user < 0:
    print('Ваш возраст отрицательный, с вами точно всё в порядке?')
elif age_of_user < 6:
    print('Вы ребёнок!')
elif age_of_user < 18:
    print('Вы школьник или школьница!')
elif age_of_user < 23:
    print('Вы студент или студентка!')
elif age_of_user < 30:
    print('Вы юноша или девушка!')
elif age_of_user < 65:
    print('Вы взрослый!')
elif age_of_user < 90:
    print('Вы дедушка или бабушка!')
else:
    print('Вы долгожитель!')