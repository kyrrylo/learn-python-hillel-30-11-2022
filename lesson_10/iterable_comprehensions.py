import os

l = list()
l.append(5)
l = [3, 4, 5, 7]

# range с 1 параметром - ДО чего (строго до, исключаем последний элемент)
print(list(range(10)))

# range с 2 параметрами - ОТ чего (включительно) и ДО чего (исключительно)
print(list(range(5, 10)))

# range с 3 параметром - ОТ чего (включительно), ДО чего (исключительно) и с каким шагом
print(list(range(5, 22, 2)))
# так же можно шаг указывать отрицательный
print(list(range(50, 19, -5)))

l = list()
for el in range(10):
    if el > 2:
        l.append(el ** 2)
print(l)

# List comprehension - [
#                           <конечный элемент списка>
#                           for <объявленная переменная>
#                           in <iterable из которого извлекаются значения>
#                           if <условие чтобы переменная попала в список> (фильтр)
#                      ]
l_comprehension = [x for x in range(10) if x > 2]
print(type(l_comprehension), l_comprehension)
# list(range(10)) - если мы в list comprehension не делаем никаких преобразований
l_comprehension = [x ** 2 for x in range(10)]
print(type(l_comprehension), l_comprehension)

with open(os.path.join('..', 'lesson_9', 'cafe_menu.txt')) as f:
    clear_lines = [line.strip() for line in f.readlines()]
    print(clear_lines)
    for line in clear_lines:
        print(line)

d = {
    'one': 1,
    'two': 2,
    'three': 3
}

# dict comprehension
d = {line: 0 for line in clear_lines}
print(type(d), d)

# set comprehension
s = {x for x in [5, 2, 2, 2, 1]}
print(type(s), s)

comprehension = (x ** 2 for x in range(10))
print(type(comprehension), comprehension)

for x in comprehension:
    print(x)
    break
print(comprehension)

for x in comprehension:
    print(x)
    break
print(comprehension)

for x in comprehension:
    print(x)
    break
print(comprehension)
