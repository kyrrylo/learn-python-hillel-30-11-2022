def f(n: int):
    for i in range(n):
        print(i)


def f_recursive(n: int):
    # базовый случай (тривиальный)
    print(n)
    # рекурсивный случай
    if n > 1:
        f_recursive(n - 1)


if __name__ == '__main__':
    # f(5)
    f_recursive(5)
    # из каждой рекурсии можно сделать цикл
    # но не из каждого цикла можно сделать рекурсию

    # В пайтоне рекурсии лучше избегать!
    # Реализованы неэффективно
