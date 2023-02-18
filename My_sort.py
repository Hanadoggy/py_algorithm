# algorithm - 정렬

import math


def question_2587():
    result = list()
    x = 0
    for i in range(0, 5):
        result.append(int(input()))
        x += result[i]

    result.sort()
    print(math.trunc(x / 5))
    print(result[2])


def question_25305():
    x, y = input().split()
    result = list(map(int, input().split()))
    result.sort()
    print(result[int(x) - int(y)])
