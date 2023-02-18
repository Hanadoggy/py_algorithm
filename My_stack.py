# algorithm - 스택

import sys


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
