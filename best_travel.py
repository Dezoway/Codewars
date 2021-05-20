import itertools


def chose_best_sum(t, k, ls):
    best_values = list()
    for x in list(itertools.combinations(ls, k)):
        if sum(x) <= t:
            best_values.append(sum(x))
    if len(best_values) == 0:
        return None
    elif t in best_values:
        return t
    else:
        m = 0
        for x in best_values:
            if x > m:
                m = x
        return m





xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(chose_best_sum(430, 8, xs))