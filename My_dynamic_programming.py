# algorithm - Dynamic Programming

from bisect import bisect_left


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


def question_1463():
    n = int(input())
    count = [0] * (n + 1)
    for i in range(2, n + 1):
        count[i] = count[i - 1] + 1
        if i % 2 == 0:
            count[i] = min(count[i], count[i // 2] + 1)

        if i % 3 == 0:
            count[i] = min(count[i], count[i // 3] + 1)

    print(count[n])


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


def question_2156():
    total = int(input())
    arr = [int(input()) for _ in range(total)]
    arr.append(0)
    count = [[0] * 2 for _ in range(total + 2)]
    count[1][0] = count[1][1] = arr[0]
    count[2][0] = arr[0] + arr[1]
    count[2][1] = arr[1]
    for i in range(3, total + 1):
        count[i][0] = count[i - 1][1] + arr[i - 1]
        count[i][1] = max(count[i - 2][0], count[i - 2][1], count[i - 3][0], count[i - 3][1]) + arr[i - 1]

    print(max(count[total][0], count[total][1], count[total - 1][0]))


def question_2565():
    total = int(input())
    arr = dict()
    for i in range(total):
        x, y = list(map(int, input().split()))
        arr[x] = y

    lc = list(arr.keys())
    lc.sort()
    count = [1] * total
    for i in range(total):
        for j in range(0, i + 1):
            if arr[lc[i]] > arr[lc[j]] and count[i] <= count[j]:
                count[i] = count[j] + 1

    print(count)
    print(total - max(count))


def question_2579():
    total = int(input())
    arr = [int(input()) for _ in range(total)]
    count = [[0] * 2 for _ in range(total + 1)]
    count[1][0] = count[1][1] = arr[0]
    for i in range(2, total + 1):
        count[i][0] = count[i - 1][1] + arr[i - 1]
        count[i][1] = max(count[i - 2][0], count[i - 2][1]) + arr[i - 1]

    print(max(count[total][0], count[total][1]))


def question_9184():
    arr = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
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


# 미해결

def question_9251():
    cap = list(input())
    com = list(input())
    count = [0] * 2
    arr = [-1]
    if len(com) > len(cap):
        for i in range(len(cap)):
            for j in range(len(com)):
                if cap[i] == com[j] and j > arr[-1] and count[-1] >= count[-2]:
                    arr.append(j)
                    count.append(count[-1] + 1)

    else:
        for i in range(len(com)):
            for j in range(len(cap)):
                if com[i] == cap[j] and j > arr[-1] and count[-1] >= count[-2]:
                    arr.append(j)
                    count.append(count[-1] + 1)

    print(cap, com, count, arr)
    print(max(count))


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


def question_10844():
    arr = [[0] * 11 for _ in range(101)]
    for i in range(0, 10):
        arr[1][i] = 1

    for i in range(2, 101):
        for j in range(0, 10):
            arr[i][j] = (arr[i - 1][j + 1] + arr[i - 1][j - 1]) % 1000000000

    result = 0
    n = int(input())
    for i in range(1, 10):
        result += arr[n][i]

    print(result % 1000000000)


def question_11053():
    total = int(input())
    arr = list(map(int, input().split()))
    count = [0]
    for i in range(total):
        x = bisect_left(count, arr[i])
        if count[-1] < arr[i]:
            count.append(arr[i])
        else:
            count[x] = arr[i]

    print(len(count) - 1)


def question_11054():
    total = int(input())
    arr = list(map(int, input().split()))
    count = [0]
    reverse = [0]
    idx = [[0] * 2]
    comp = 0
    for i in range(total):
        j = bisect_left(count, arr[i])
        if count[-1] < arr[i]:
            count.append(arr[i])
            idx.append([i, len(count) - 1])
        else:
            count[j] = arr[i]

    for x in range(len(idx)):
        for i in range(total - 1, idx[x][0] - 1, -1):
            j = bisect_left(reverse, arr[i])
            if reverse[-1] < arr[i]:
                reverse.append(arr[i])
            else:
                reverse[j] = arr[i]

        comp = max(comp, idx[x][1] + len(reverse) - 2)
        reverse = [0]

    count = [0]
    reverse = [0]
    comp2 = 0
    idx = [[0] * 2]
    for i in range(total - 1, -1, -1):
        j = bisect_left(count, arr[i])
        if count[-1] < arr[i]:
            count.append(arr[i])
            idx.append([i, len(count) - 1])
        else:
            count[j] = arr[i]

    for x in range(len(idx)):
        for i in range(0, idx[x][0] + 1):
            j = bisect_left(reverse, arr[i])
            if reverse[-1] < arr[i]:
                reverse.append(arr[i])
            else:
                reverse[j] = arr[i]

        comp2 = max(comp2, idx[x][1] + len(reverse) - 2)
        reverse = [0]

    print(max(comp, comp2))


def question_24416():
    x = int(input())
    arr = [1 for _ in range(3)]
    for i in range(3, x + 1):
        arr.append(arr[i - 1] + arr[i - 2])

    print(arr[x], x - 2)
