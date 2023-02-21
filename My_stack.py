# algorithm - 스택

import sys


def question_2504():
    arr = input()
    stack = list()
    append = list()
    count = 0
    temp = 1
    for i in range(len(arr)):
        if arr[i] == '[':
            stack.append(arr[i])
            temp *= 3
        elif arr[i] == '(':
            stack.append(arr[i])
            temp *= 2
        elif arr[i] == ']':
            if len(stack) == 0 or stack[-1] == '(':
                count = 0
                break

            if arr[i - 1] == '[':
                count += temp
            stack.pop()
            temp //= 3
        else:
            if len(stack) == 0 or stack[-1] == '[':
                count = 0
                break

            if arr[i - 1] == '(':
                count += temp
            stack.pop()
            temp //= 2

    if len(stack) > 0:
        print(0)
    else:
        print(count)


def question_4949():
    stack = list()
    while True:
        valid = 1
        stack.clear()
        given = input()
        if given == ".":
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
    y = ''
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
