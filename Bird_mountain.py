from pprint import pprint
from copy import deepcopy


def step2_3(mountains):
    mountain1 = deepcopy(mountains)
    count = 1
    max = 0
    flag = True
    while flag:
        flag = False
        mountain = deepcopy(mountain1)
        for x in range(len(mountain) - 1):
            if x == 0:
                continue
            for i in range(len(mountain[x]) - 1):
                if mountain[x][i] == ' ':
                    continue
                if (mountain[x][i] == mountain[x + 1][i]
                        and mountain[x][i] == mountain[x][i + 1]
                        and mountain[x][i] == mountain[x - 1][i]
                        and mountain[x][i] == mountain[x][i - 1]):
                    mountain1[x][i] = str(count)
                    max = count
                    flag = True

        count += 1
    mountain2 = [''.join([x for x in mountain1[i]]) for i in range(len(mountain1))]
    return mountain1


def peak_height(mountain):
    mountain1 = [['1' if x == '^' else ' ' for x in mountain[i]] for i in range(len(mountain))]
    max = 0
    j = step2_3(mountain1)
    for x in range(len(j)):
        for i in j[x]:
            if i.isdigit():
                if int(i) > max:
                    max = int(i)
    return max

mountain = ['^^'
]
pprint(peak_height(mountain))
