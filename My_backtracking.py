# algorithm - Backtracking


def question_1182():
    count = 0
    # global count
    total, num = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    calc_1182(arr, 0, total, num, 0)
    if num == 0:
        count -= 1
    print(count)


def calc_1182(arr, cur, total, num, x):
    # global count
    # if cur == total:
    #     if num == x:
    #         count += 1
    # else:
    calc_1182(arr, cur + 1, total, num, x)
    calc_1182(arr, cur + 1, total, num, x + arr[cur - 1])


def question_9663():
    size = int(input())
    count = [0]
    lx = [0] * 16
    ly = [0] * 32
    lz = [0] * 32
    recur_9663(size, count, lx, ly, lz, 0)
    print(count[0])


def recur_9663(size, count, lx, ly, lz, c):
    if c == size:
        count[0] += 1
        return

    for i in range(size):
        if lx[i] == 1 or ly[i + c] == 1 or lz[c - i + size - 1] == 1:
            continue

        lx[i] = ly[i + c] = lz[c - i + size - 1] = 1
        recur_9663(size, count, lx, ly, lz, c + 1)
        lx[i] = ly[i + c] = lz[c - i + size - 1] = 0


def question_15649():
    total, n = list(map(int, input().split()))
    arr = [0] * (total + 1)
    check = [0] * (total + 1)
    recur_15649(arr, check, 0, n, total)


def recur_15649(arr, check, x, n, total):
    if x == n:
        for i in range(n):
            print(arr[i], end=' ')

        print()

    for i in range(1, total + 1):
        if check[i] == 0:
            arr[x] = i
            check[i] = 1
            recur_15649(arr, check, x + 1, n, total)
            check[i] = 0


def question_15650():
    total, num = list(map(int, input().split()))
    arr = [0] * total
    check = [0] * (total + 1)
    calc_15650(total, num, 0, check, arr)


def calc_15650(total, num, cur, check, arr):
    if cur == num:
        for i in range(num):
            print(arr[i], end=' ')
        print()

    for i in range(1, total + 1):
        if cur == 0:
            arr[cur] = i
            check[i] = 1
            calc_15650(total, num, cur + 1, check, arr)
            check[i] = 0
        elif check[i] == 0 and arr[cur - 1] < i:
            arr[cur] = i
            check[i] = 1
            calc_15650(total, num, cur + 1, check, arr)
            check[i] = 0


def question_15651():
    total, num = list(map(int, input().split()))
    arr = [0] * total
    calc_15651(total, num, arr, 0)


def calc_15651(total, num, arr, cur):
    if cur == num:
        for i in range(num):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, total + 1):
        arr[cur] = i
        calc_15651(total, num, arr, cur + 1)


def question_15652():
    total, num = list(map(int, input().split()))
    arr = [0] * total
    calc_15652(total, num, arr, 0)


def calc_15652(total, num, arr, cur):
    if cur == num:
        for i in range(num):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, total + 1):
        if cur == 0:
            arr[0] = i
            calc_15652(total, num, arr, cur + 1)
        elif i >= arr[cur - 1]:
            arr[cur] = i
            calc_15652(total, num, arr, cur + 1)


def question_15654():
    total, num = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    idx = [0] * total
    check = [0] * total
    calc_15654(total, num, arr, idx, 0, check)


def calc_15654(total, num, arr, idx, cur, check):
    if cur == num:
        for i in range(num):
            print(arr[idx[i]], end=' ')
        print()
        return

    for i in range(total):
        if check[i] == 0:
            idx[cur] = i
            check[i] = 1
            calc_15654(total, num, arr, idx, cur + 1, check)
            check[i] = 0
