# baekjoon problem solving - python

import math
import sys


#                                                           구현

# 종이가 차지 하는 부분을 좌표로 잡고 큰 점이라 생각 해서 넓이 구하기
def question_2563():
    result = [[0 for col in range(110)] for row in range(110)]
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
    result = [[0 for col in range(9)] for row in range(9)]
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
    total = input()
    result = list(map(int, input().split()))
    x = int(input())
    print(result.count(x))


#                                                    집합

def question_1269():
    temp = input()
    alpha = set()
    beta = set()
    alpha.update(input().split())
    beta.update(input().split())
    print(len(alpha) + len(beta) - (2 * len(alpha.intersection(beta))))


def question_1620():
    x, y = input().split()
    pokemon = dict()
    pokemons = list()
    for i in range(int(x)):
        temp = sys.stdin.readline().rstrip()
        pokemon[temp] = i + 1
        pokemons.append(temp)

    for i in range(int(y)):
        temp = sys.stdin.readline().rstrip()
        if temp.isdigit():
            print(pokemons[int(temp) - 1])
        else:
            print(pokemon[temp])


def question_1764():
    x, y = input().split()
    alpha_names = set()
    beta_names = set()
    for i in range(0, int(x)):
        alpha_names.add(input())

    for i in range(0, int(y)):
        beta_names.add(input())

    common_names = list(alpha_names.intersection(beta_names))
    common_names.sort(reverse=True)
    print(len(common_names))
    for i in range(0, len(common_names)):
        print(common_names.pop())


#                                                   정렬

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


#                                                   재귀

def question_25501():
    total = input()


#                                               Dynamic Programming

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


#                                                   메인 함수

if __name__ == '__main__':
    question_1620()
