# baekjoon problem solving - python

import math
import sys
from collections import deque


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


#                                                           스택

def question_4949():
    stack = list()
    run = True
    while run:
        valid = 1
        stack.clear()
        given = input()
        if given == ".":
            run = False
            break

        for i in range(0, len(given)):
            if given[i] == '(' or given[i] == '[':
                stack.append(given[i])
            elif given[i] == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    valid = 0
            elif given[i] == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    valid = 0

        if valid == 0 or len(stack) != 0:
            print('no')
        else:
            print('yes')


def question_10799():
    count = 0
    word = input()
    stack = list()
    stack.append(word[0])
    for i in range(1, len(word)):
        if word[i] == ')' and word[i - 1] == '(':
            count += len(stack) - 1
            stack.pop()
        elif word[i] == ')':
            stack.pop()
            count += 1
        else:
            stack.append(word[i])

    print(count)


def question_10828():
    total = input()
    stack = list()
    for i in range(int(total)):
        word = sys.stdin.readline().rstrip()
        if word[1] == 'u':
            x, y = word.split()
        else:
            x = word

        if x == 'push':
            stack.append(int(y))
        elif x == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif x == 'size':
            print(len(stack))
        elif x == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])


#                                                           집합

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


def question_11478():
    name = input()
    partition = set()
    count = 0
    for i in range(1, len(name) + 1):
        partition.clear()
        for j in range(0, (len(name) - i + 1)):
            partition.add(name[j:(j + i)])
        count += len(partition)

    print(count)


#                                                       정렬

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


#                                                       재귀

def question_25501():
    total = input()


#                                                       Dynamic Programming

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


#                                                      DFS, BFS

def question_1926():
    x, y = input().split()
    x = int(x)
    y = int(y)
    xq = deque()
    yq = deque()
    maxsize = 0
    number = 0
    canvas = [[0 for col in range(y)] for row in range(x)]
    check = [[0 for col in range(y)] for row in range(x)]
    for i in range(x):
        canvas[i] = list(map(int, input().split()))

    for i in range(x):
        for j in range(y):
            if check[i][j] == 0 and canvas[i][j] == 1:
                xq.append(i)
                yq.append(j)
                count = 0
                while len(xq) > 0 and len(yq) > 0:
                    tx = xq.popleft()
                    ty = yq.popleft()
                    check[tx][ty] = 1
                    count += 1

                    if ty < y - 1 and canvas[tx][ty + 1] == 1 and check[tx][ty + 1] == 0:
                        xq.append(tx)
                        yq.append(ty + 1)
                        check[tx][ty + 1] = 1

                    if tx < x - 1 and canvas[tx + 1][ty] == 1 and check[tx + 1][ty] == 0:
                        xq.append(tx + 1)
                        yq.append(ty)
                        check[tx + 1][ty] = 1

                    if ty > 0 and canvas[tx][ty - 1] == 1 and check[tx][ty - 1] == 0:
                        xq.append(tx)
                        yq.append(ty - 1)
                        check[tx][ty - 1] = 1

                    if tx > 0 and canvas[tx - 1][ty] == 1 and check[tx - 1][ty] == 0:
                        xq.append(tx - 1)
                        yq.append(ty)
                        check[tx - 1][ty] = 1

                if count > maxsize:
                    maxsize = count

                number += 1

    print(number)
    print(maxsize)


def question_2178():
    x, y = input().split()
    x = int(x)
    y = int(y)
    xq = deque()
    yq = deque()
    canvas = [[0 for col in range(y)] for row in range(x)]
    check = [[(x * y) for col in range(y)] for row in range(x)]
    for i in range(x):
        canvas[i] = list(input())

    xq.append(0)
    yq.append(0)
    check[0][0] = 1
    while len(xq) > 0 and len(yq) > 0:
        tx = xq.popleft()
        ty = yq.popleft()
        if ty < y - 1 and canvas[tx][ty + 1] == '1' and check[tx][ty + 1] > check[tx][ty] + 1:
            xq.append(tx)
            yq.append(ty + 1)
            check[tx][ty + 1] = check[tx][ty] + 1

        if tx < x - 1 and canvas[tx + 1][ty] == '1' and check[tx + 1][ty] > check[tx][ty] + 1:
            xq.append(tx + 1)
            yq.append(ty)
            check[tx + 1][ty] = check[tx][ty] + 1

        if ty > 0 and canvas[tx][ty - 1] == '1' and check[tx][ty - 1] > check[tx][ty] + 1:
            xq.append(tx)
            yq.append(ty - 1)
            check[tx][ty - 1] = check[tx][ty] + 1

        if tx > 0 and canvas[tx - 1][ty] == '1' and check[tx - 1][ty] > check[tx][ty] + 1:
            xq.append(tx - 1)
            yq.append(ty)
            check[tx - 1][ty] = check[tx][ty] + 1

    print(check[x - 1][y - 1])


def question_4179():
    x, y = input().split()
    x = int(x)
    y = int(y)
    jsx = 0
    jsy = 0
    fsqx = deque()
    fsqy = deque()
    escape = x * y
    xq = deque()
    yq = deque()
    valid = False
    canvas = [[0 for col in range(y)] for row in range(x)]
    check = [[(x * y) for col in range(y)] for row in range(x)]
    fast = [[(x * y) for col in range(y)] for row in range(x)]
    for i in range(x):
        canvas[i] = list(input())
        for j in range(y):
            if canvas[i][j] == 'J':
                jsx = i
                jsy = j
            elif canvas[i][j] == 'F':
                fsqx.append(i)
                fsqy.append(j)

    while len(fsqx) > 0:
        xq.append(fsqx.popleft())
        yq.append(fsqy.popleft())
        check[xq[0]][yq[0]] = 0
        while len(xq) > 0:
            tx = xq.popleft()
            ty = yq.popleft()
            if ty < y - 1 and canvas[tx][ty + 1] != '#' and check[tx][ty + 1] > check[tx][ty] + 1:
                xq.append(tx)
                yq.append(ty + 1)
                check[tx][ty + 1] = check[tx][ty] + 1

            if tx < x - 1 and canvas[tx + 1][ty] != '#' and check[tx + 1][ty] > check[tx][ty] + 1:
                xq.append(tx + 1)
                yq.append(ty)
                check[tx + 1][ty] = check[tx][ty] + 1

            if ty > 0 and canvas[tx][ty - 1] != '#' and check[tx][ty - 1] > check[tx][ty] + 1:
                xq.append(tx)
                yq.append(ty - 1)
                check[tx][ty - 1] = check[tx][ty] + 1

            if tx > 0 and canvas[tx - 1][ty] != '#' and check[tx - 1][ty] > check[tx][ty] + 1:
                xq.append(tx - 1)
                yq.append(ty)
                check[tx - 1][ty] = check[tx][ty] + 1

    xq.append(jsx)
    yq.append(jsy)
    fast[jsx][jsy] = 0
    while len(xq) > 0:
        tx = xq.popleft()
        ty = yq.popleft()
        if tx == x - 1 or ty == y - 1 or tx == 0 or ty == 0:
            if fast[tx][ty] < escape and check[tx][ty] > fast[tx][ty]:
                valid = True
                escape = fast[tx][ty] + 1

        if ty < y - 1 and canvas[tx][ty + 1] != '#' and check[tx][ty + 1] > fast[tx][ty] and fast[tx][ty + 1] > fast[tx][ty] + 1:
            xq.append(tx)
            yq.append(ty + 1)
            fast[tx][ty + 1] = fast[tx][ty] + 1

        if tx < x - 1 and canvas[tx + 1][ty] != '#' and check[tx + 1][ty] > fast[tx][ty] and fast[tx + 1][ty] > fast[tx][ty] + 1:
            xq.append(tx + 1)
            yq.append(ty)
            fast[tx + 1][ty] = fast[tx][ty] + 1

        if ty > 0 and canvas[tx][ty - 1] != '#' and check[tx][ty - 1] > fast[tx][ty] and fast[tx][ty - 1] > fast[tx][ty] + 1:
            xq.append(tx)
            yq.append(ty - 1)
            fast[tx][ty - 1] = fast[tx][ty] + 1

        if tx > 0 and canvas[tx - 1][ty] != '#' and check[tx - 1][ty] > fast[tx][ty] and fast[tx - 1][ty] > fast[tx][ty] + 1:
            xq.append(tx - 1)
            yq.append(ty)
            fast[tx - 1][ty] = fast[tx][ty] + 1

    if valid:
        print(escape)
    else:
        print('IMPOSSIBLE')


def question_7576():
    y, x = input().split()
    x = int(x)
    y = int(y)
    xq = deque()
    yq = deque()
    txq = deque()
    tyq = deque()
    day = 0
    container = [[0 for col in range(y)] for row in range(x)]
    for i in range(x):
        container[i] = list(map(int, input().split()))
        for j in range(y):
            if container[i][j] == 1:
                xq.append(i)
                yq.append(j)

    while len(xq) > 0 or len(txq) > 0:
        if len(xq) == 0:
            day += 1
            xq = txq.copy()
            yq = tyq.copy()
            txq.clear()
            tyq.clear()

        tx = xq.popleft()
        ty = yq.popleft()
        if ty < y - 1 and container[tx][ty + 1] == 0:
            txq.append(tx)
            tyq.append(ty + 1)
            container[tx][ty + 1] = 1

        if tx < x - 1 and container[tx + 1][ty] == 0:
            txq.append(tx + 1)
            tyq.append(ty)
            container[tx + 1][ty] = 1

        if ty > 0 and container[tx][ty - 1] == 0:
            txq.append(tx)
            tyq.append(ty - 1)
            container[tx][ty - 1] = 1

        if tx > 0 and container[tx - 1][ty] == 0:
            txq.append(tx - 1)
            tyq.append(ty)
            container[tx - 1][ty] = 1

    for i in range(x):
        for j in range(y):
            if container[i][j] == 0:
                day = -1
                break

    print(day)


#                                                        메인 함수

#   백준 대신 알고리즘 강의 따라가는 중...

if __name__ == '__main__':
    question_4179()
