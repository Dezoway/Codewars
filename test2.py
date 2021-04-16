def count_the_digit(n,d):
    counts = 0
    for x in range(n+1):
        counts += str(x**2).count(str(d))
    return counts




print(count_the_digit(5750,0))