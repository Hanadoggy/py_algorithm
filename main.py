# baekjoon problem solving - python


def question_10807():
    total = input()
    result = list(map(int, input().split()))
    x = int(input())
    print(result.count(x))


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


if __name__ == '__main__':
    question_5597()