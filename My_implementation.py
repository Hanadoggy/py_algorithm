# algorithm - 구현

# 종이가 차지 하는 부분을 좌표로 잡고 큰 점이라 생각 해서 넓이 구하기


def question_2563():
    result = [[0 for _ in range(110)] for _ in range(110)]
    total = int(input())
    for n in range(0, total):
        x, y = input().split()
        for i in range(int(x), int(x) + 10):
            for j in range(int(y), int(y) + 10):
                result[i][j] = 1

    count = 0
    for i in range(0, 100):
        for j in range(0, 100):
            if result[i][j] == 1:
                count = count + 1

    print(count)


def question_2566():
    result = [[0 for _ in range(9)] for _ in range(9)]
    mylist = [-1, 0, 0]
    for i in range(0, 9):
        temp = list(map(int, input().split()))
        for j in range(0, 9):
            result[i][j] = temp[j]
            if mylist[0] <= temp[j]:
                mylist[0] = temp[j]
                mylist[1] = i + 1
                mylist[2] = j + 1

    print(mylist[0])
    print(mylist[1], mylist[2])


def question_2738():
    n, m = map(int, input().split())
    result1 = list()
    result2 = list()
    for i in range(0, n):
        result1.append(input())

    for i in range(0, n):
        result2.append(input())

    for i in range(0, n):
        for j in range(0, m):
            print(int(result1[i].split()[j]) + int(result2[i].split()[j]), end=' ')

        print()


def question_5597():
    result = list()
    for i in range(0, 28):
        result.append(int(input()))

    result.sort()
    result.append(0)
    result.append(0)
    for i in range(1, 31):
        if i != result[i - 1]:
            print(i)
            result.insert(i - 1, i)


def question_10807():
    temp = input()
    result = list(map(int, input().split()))
    x = int(input())
    print(result.count(x))
