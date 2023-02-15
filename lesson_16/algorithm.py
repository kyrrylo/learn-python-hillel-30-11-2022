# Abstract tasks

# lake = ??
# 48 - 100
# 47 - 50
# 46 - 25
# 45 - 12.5

# 100 - 70
# 48 - 100
# 47 - 70
# 46 - 35
# 45 - 17.5
# 1/4 - 25

# 47 - 99
# 46 - 49.5
# 45 -

# 1 worm
# Each 1 second worm splits in half
# 60 seconds -> full glass

# 2 worms?
# Each 1 second worm splits in half
# 59 seconds -> full glass


if __name__ == '__main__':
    with open('text.txt') as f:
        # O(1)
        x = 463623 * 123123
        y = 14123412451515 ** 123

        text = f.read().split()
        # O(n)
        x = 0
        for word in text:
            x += 1
        print(x)

        # O(n * m) - n is all words, m is unique words
        for word in text:
            text.count(word)

        # O(n^2)
        x = 0
        for word in text:
            for letter in word:
                x += 1
        print(x)


        # O(n^3)
        for word in text:
            for letter in word:
                word.count(letter)

        # O(logn) > O(n)    > means better, faster, stronger
        # O(n*logn) > O(n^2)

        # 1 6 9 25 48 90 102
        # 0 1 2 3  4  5  6

    # Итого, варианты сложностей алгоритма
    # O(1)
    # O(n)
    # O(n^2) / O(n^3) / O(n^4) ...
    # O(logn)
    # +Варианты их перемножения между собой, например O(n^2*logn)
