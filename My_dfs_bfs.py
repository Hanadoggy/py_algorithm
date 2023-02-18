# algorithm - DFS, BFS
# 문제 유형 대부분 BFS 풀이

from collections import deque


def question_1697():
    subin, sister = input().split()
    subin = int(subin)
    sister = int(sister)
    ruler = [100000 for i in range(100101)]
    xq = deque()
    xq.append(subin)
    ruler[subin] = 0
    while len(xq) > 0:
        tx = xq.popleft()
        if tx > 0 and ruler[tx - 1] > ruler[tx] + 1:
            xq.append(tx - 1)
            ruler[tx - 1] = ruler[tx] + 1

        if tx < 50020 and ruler[2 * tx] > ruler[tx] + 1:
            xq.append(2 * tx)
            ruler[2 * tx] = ruler[tx] + 1

        if tx < 100040 and ruler[tx + 1] > ruler[tx] + 1:
            xq.append(tx + 1)
            ruler[tx + 1] = ruler[tx] + 1

    print(ruler[sister])


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
