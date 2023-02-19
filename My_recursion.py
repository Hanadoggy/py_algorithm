# algorithm - 재귀


def question_1074():
    n, row, col = input().split()
    n = int(n)
    row = int(row)
    col = int(col)
    print(recur_1074(n, row, col))


def recur_1074(n, r, c):
    if n == 0:
        return 0

    x = 2 ** (n - 1)
    if x > r and x > c:
        return recur_1074(n - 1, r, c)
    elif r < x <= c:
        return x ** 2 + recur_1074(n - 1, r, c - x)
    elif r >= x > c:
        return 2 * x ** 2 + recur_1074(n - 1, r - x, c)
    else:
        return 3 * x ** 2 + recur_1074(n - 1, r - x, c - x)


def question_1629():
    x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    print(recur_1629(x, y, z))


def recur_1629(x, y, z):
    if y == 1:
        return x % z

    result = recur_1629(x, y // 2, z)
    result = result * result % z
    if y % 2 == 0:
        return result

    return result * x % z


def question_25501():
    total = input()
    for i in range(int(total)):
        temp = input()
        count = recur_25501(temp, 0, len(temp) - 1, 0)
        print(count[0], count[1])


def recur_25501(s, x, y, count):
    count += 1
    if x >= y:
        return [1, count]
    elif s[x] != s[y]:
        return [0, count]
    else:
        return recur_25501(s, x + 1, y - 1, count)
