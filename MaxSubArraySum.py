def max_sum(array):
    max_array = [0, ]
    for x in array:
        tmp = max_array[-1] + x
        if tmp < 0:
            tmp = 0
        max_array.append(tmp)
    return max(max_array)


print(max_sum([]))