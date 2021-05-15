import itertools
def arrays(arr):
    dicts = {}
    sorted_arr = []
    for x in arr:
            dicts[str(x)] = set(int(''.join(x)) for x in itertools.permutations(str(x), len(str(x))) if (float(''.join(x))**(1/2) - int(int(''.join(x))**(1/2))) == 0)
            dicts[str(x)] = len(dicts[str(x)])
    sorted_arr = [[dicts[x],int(x)] for x in dicts]
    sorted_arr.sort(reverse=True)
    print(sorted_arr)
    for z in range(len(sorted_arr)):
        for x in range(len(sorted_arr)-1):
            if sorted_arr[x][0] == sorted_arr[x+1][0]:
                if sorted_arr[x][1] > sorted_arr[x+1][1]:
                    t = sorted_arr[x][1]
                    sorted_arr[x][1] = sorted_arr[x+1][1]
                    sorted_arr[x+1][1] = t
    sorted_arr = [int(x[1]) for x in sorted_arr]


    return sorted_arr





print(arrays([715, 112, 136, 169, 144]))