from collections import Counter
def find(lists):
    a = Counter(lists)
    minimum = list(a.items())[0]
    for x in list(a.items()):
        if minimum[1] > x[1]:
            minimum = x


    return minimum[0]

print(find([1, 1, 1, 2, 1, 1]))