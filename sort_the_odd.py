def sorting_odd(lising_values):
    new_listing_values = list()
    for x in range(len(lising_values)):
        for z in range(x+1,len(lising_values)):
            print(lising_values[x], lising_values[z])
            print(lising_values)
            if lising_values[x] % 2 == 1 and lising_values[z] % 2 == 1 and lising_values[x] > lising_values[z]:
                lising_values[x], lising_values[z] = lising_values[z], lising_values[x]
    return lising_values



print(sorting_odd([5, 3, 2, 8, 1, 4]))