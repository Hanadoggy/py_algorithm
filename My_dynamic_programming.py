# algorithm - Dynamic Programming

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
