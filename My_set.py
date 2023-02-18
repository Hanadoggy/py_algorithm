# algorithm - 집합

import sys


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
