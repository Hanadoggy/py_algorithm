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


# 너무 난잡한데 코드를 깔끔하게 할 방법은?? 모르겠다 배열이 너무 많음
def question_15683():
    row, col = list(map(int, input().split()))
    room = list()
    cctv = list()
    index = list()
    count = 0
    angle = [[[0], [1], [2], [3]],
             [[0, 2], [1, 3]],
             [[0, 1], [1, 2], [2, 3], [3, 0]],
             [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
             [[0, 1, 2, 3]]]
    # cctv, cctv 가 현재 보는 방향, cctv 방향의 경우의 수 3-6-9-12시 방향
    for i in range(row):
        room.append(list(map(int, input().split())))
    for r in range(row):
        for c in range(col):
            if room[r][c] == 0:
                count += 1
            elif room[r][c] < 6:
                cctv.append([r, c, room[r][c] - 1])
                index.append(0)
    minus = 0
    if len(index) > 0:
        while index[0] != 4:
            check = [item[:] for item in room]
            temp = 0
            for i in range(len(cctv)):
                temp += calc_15683(row, col, cctv, index, angle, check, i)
            minus = max(minus, temp)
            index[-1] += 1
            for i in range(len(index) - 1, 0, -1):
                if index[i] == 4:
                    index[i] = 0
                    index[i - 1] += 1
    print(count - minus)


def calc_15683(row, col, cctv, index, angle, check, n):
    count = 0
    for i in range(len(angle[cctv[n][2]][(index[n] % len(angle[cctv[n][2]]))])):
        if angle[cctv[n][2]][(index[n] % len(angle[cctv[n][2]]))][i] == 0:
            for x in range(cctv[n][1] + 1, col):
                if check[cctv[n][0]][x] == 0:
                    check[cctv[n][0]][x] = 7
                    count += 1
                elif check[cctv[n][0]][x] == 6:
                    break
        elif angle[cctv[n][2]][(index[n] % len(angle[cctv[n][2]]))][i] == 1:
            for y in range(cctv[n][0] + 1, row):
                if check[y][cctv[n][1]] == 0:
                    check[y][cctv[n][1]] = 7
                    count += 1
                elif check[y][cctv[n][1]] == 6:
                    break
        elif angle[cctv[n][2]][(index[n] % len(angle[cctv[n][2]]))][i] == 2:
            for x in range(cctv[n][1] - 1, -1, -1):
                if check[cctv[n][0]][x] == 0:
                    check[cctv[n][0]][x] = 7
                    count += 1
                elif check[cctv[n][0]][x] == 6:
                    break
        else:
            for y in range(cctv[n][0] - 1, -1, -1):
                if check[y][cctv[n][1]] == 0:
                    check[y][cctv[n][1]] = 7
                    count += 1
                elif check[y][cctv[n][1]] == 6:
                    break
    return count


arr = list()
stickers = list()


def question_18808():
    global stickers, arr
    row, col, total = list(map(int, input().split()))
    arr = [[0] * col] * row
    for _ in range(total):
        r, c = list(map(int, input().split()))
        temp = list()
        for _ in range(r):
            temp.append(list(map(int, input().split())))
        stickers.append(temp)
    for i in range(total):
        for case in range(4):
            if turn_18808(row, col, i, case) == 1:
                break
    count = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                count += 1
    print(row * col - count)


def turn_18808(row, col, i, case):
    global stickers, arr
    if case != 0:
        sticker = [[0 for _ in range(len(stickers[i]))] for _ in range(len(stickers[i][0]))]
        for y in range(len(stickers[i][0])):
            for x in range(len(stickers[i])):
                sticker[y][len(stickers[i]) - x - 1] = stickers[i][x][y]
        stickers[i] = [item[:] for item in sticker]
    for y in range(row):
        for x in range(col):
            if x + len(stickers[i][0]) <= col and y + len(stickers[i]) <= row and paste_18808(y, x, i) == 1:
                return 1
    return 0


def paste_18808(row, col, n):
    global stickers, arr
    temp = [item[:] for item in arr]
    for i in range(len(stickers[n])):
        for j in range(len(stickers[n][i])):
            if arr[row + i][col + j] != 0 and stickers[n][i][j] == 1:
                return 0
            elif arr[row + i][col + j] == 0 and stickers[n][i][j] == 1:
                temp[row + i][col + j] = 1
    arr = [item[:] for item in temp]
    return 1
