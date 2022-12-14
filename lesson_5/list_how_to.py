# list - список

x = [3, 4, 5]
print(type(x))
print(x)

x = list((3, 4, 5))
print(type(x))
print(x)

# первый с начала списка (слева)
print(x[0])
print(x[1], x[2])

# когда обращаемся к несуществующему элементу, выдаёт ошибку
# print(x[3])

# первый с конца (справа)
print(x[-1])
print(x[-2], x[-3])

# то же самое - несуществующие элементы недоступны
# print(x[-4])

random_list = [True, 5, 0.3, -905.43, 'I am a programmer', 'Hello', False, 3212]
print(random_list)
print(type(random_list))

s = 'I am a programmer'
# первый и последний элементы строки - такая же индексация
print(s[0], s[-1])

# отобразить список задом наперед
print(x)
print(x[::-1])

# поменять местами элементы списка
z = [7, 4, 98, 3]
y = [86, 23, 54790, 21, 5]

temp_y = y[0]
y[0] = y[-1]
y[-1] = temp_y
print(y)

# присваивание многих элементов в одну строку
y[0], y[3] = y[3], y[0]
print(y)

# slice - диапазон/отрезок
sorted_marks = [100, 98, 93, 85, 70, 60, 30, 25, 5]
# логика slice - [откуда вырезать (включительно): до куда резать (исключительно)]
print(sorted_marks[0:-1])
print(sorted_marks[:])
print(sorted_marks[:3])

# склеивание списков
print(sorted_marks[:3] + sorted_marks[4:])

# фильтр по списку
# задаём новый пустой список, куда попадут все прошедшие проверку оценки
correct_marks = list()
# correct_marks = []  # Так тоже можно задать пустой список
# задаём пороговое значение
threshold_value = 60
# iteration - итерация (пройтись по массиву/списку данных)
print(len(sorted_marks))  # длина списка
i = 0  # итератор - показывает какой элемент мы сейчас рассматриваем
while i < len(sorted_marks):
    if sorted_marks[i] >= threshold_value:
        correct_marks.append(sorted_marks[i])
        print(f'{sorted_marks[i]} больше (или равно) {threshold_value}')
    # увеличиваем итератор чтобы на следующем шаге цикла обрабатывать новую переменную
    i += 1

print(correct_marks)
