# algorithm - Dynamic Programming


def question_1003():
    result = [0, 1, 1]
    for i in range(3, 41):
        result.append(result[i - 1] + result[i - 2])

    total = int(input())
    for i in range(0, total):
        x = int(input())
        if x == 0:
            print("1 0")
        elif x == 1:
            print("0 1")
        else:
            print(result[x - 1], result[x])


def question_1149():
    total = int(input())
    arr = [list(map(int, input().split())) for _ in range(total)]
    count = [[0] * 3 for _ in range(total + 1)]
    for i in range(1, total + 1):
        count[i][0] = min(count[i - 1][1], count[i - 1][2]) + arr[i - 1][0]
        count[i][1] = min(count[i - 1][0], count[i - 1][2]) + arr[i - 1][1]
        count[i][2] = min(count[i - 1][0], count[i - 1][1]) + arr[i - 1][2]

    print(min(count[total][0], count[total][1], count[total][2]))


def question_1904():
    arr = list()
    arr.append(0)
    arr.append(1)
    arr.append(2)
    for i in range(3, 1000001):
        arr.append((arr[i-1] + arr[i-2]) % 15746)

    print(arr[int(input())] % 15746)


def question_1912():
    n = int(input())
    tlist = list(map(int, input().split()))
    count = tlist[0]
    comp = tlist[0]
    for i in range(1, n):
        count = max(count + tlist[i], tlist[i])
        comp = max(count, comp)

    print(comp)


def question_1932():
    total = int(input())
    arr = [list(map(int, input().split())) for _ in range(total)]
    count = [[0] * (total + 1) for _ in range(total + 1)]
    for i in range(1, total + 1):
        for j in range(1, i + 1):
            count[i][j] = max(count[i - 1][j - 1], count[i - 1][j]) + arr[i - 1][j - 1]

    print(max(count[total][j] for j in range(1, total + 1)))


def question_9184():
    arr = [[[0 for h in range(21)] for x in range(21)] for y in range(21)]
    arr[0][0][0] = 1
    arr[0][0][1] = 1
    arr[0][1][0] = 1
    arr[1][0][0] = 1
    arr[0][1][1] = 1
    arr[1][0][1] = 1
    arr[1][1][0] = 1
    while True:
        x, y, z = map(int, input().split())
        if x == -1 and y == -1 and z == -1:
            break
        elif x < 1 or y < 1 or z < 1:
            print('w({}, {}, {}) = 1'.format(x, y, z))
        elif x > 20 or y > 20 or z > 20:
            print('w({}, {}, {}) = {}'.format(x, y, z, recur_9184(20, 20, 20, arr)))
        else:
            print('w({}, {}, {}) = {}'.format(x, y, z, recur_9184(x, y, z, arr)))


def recur_9184(a, b, c, arr):
    if arr[a][b][c] != 0:
        return arr[a][b][c]
    elif a < 1 or b < 1 or c < 1:
        arr[a][b][c] = 1
    elif a < b < c:
        arr[a][b][c] = recur_9184(a, b, c-1, arr) + recur_9184(a, b-1, c-1, arr) - recur_9184(a, b-1, c, arr)
    else:
        arr[a][b][c] = recur_9184(a-1, b, c, arr) + recur_9184(a-1, b-1, c, arr)\
                       + recur_9184(a-1, b, c-1, arr) - recur_9184(a-1, b-1, c-1, arr)

    return arr[a][b][c]


def question_9461():
    case = int(input())
    arr = list()
    arr.append(0)
    arr.append(1)
    arr.append(1)
    arr.append(1)
    arr.append(2)
    arr.append(2)
    for i in range(6, 101):
        arr.append(arr[i-1] + arr[i-5])

    for i in range(case):
        print(arr[int(input())])


def question_24416():
    x = int(input())
    arr = [1 for i in range(3)]
    for i in range(3, x + 1):
        arr.append(arr[i - 1] + arr[i - 2])

    print(arr[x], x - 2)
