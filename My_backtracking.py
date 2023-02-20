# algorithm - Backtracking


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
