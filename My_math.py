# algorithm - 수학


import sys


def question_2981():
    total = int(input())
    arr = [int(sys.stdin.readline().rstrip()) for _ in range(total)]
    arr.sort()
    count = list()
    for i in range(total - 1, 0, -1):
        count.append(arr[i] - arr[i - 1])

    answer = count[0]
    for i in range(1, len(count)):
        answer = calc_2981(answer, count[i])

    result = set()
    for i in range(2, int(answer ** 0.5) + 1):
        if answer % i == 0:
            result.add(i)
            result.add(answer // i)

    result.add(answer)
    result = list(result)
    result.sort(reverse=True)
    while len(result) > 0:
        print(result.pop(), end=' ')


def calc_2981(m, n):
    if n == 0:
        return m
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return calc_2981(m, n)
    else:
        return n
