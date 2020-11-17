import time
start_time=time.time()
def count_primes(k, start, end):
    array_primes = list()
    while start <= end:
        if start == 0 or start == 1:
            start += 1
            continue
        j = start
        counts = 2
        counts2 = 0
        while True:
            if j % counts == 0:
                j //= counts
                counts2 += 1
                if j == 1:
                    break
            elif j % counts > 0:
                counts += 1
                continue
        if counts2 == k:
            array_primes.append(start)
        start += 1
    return array_primes

print(count_primes(2, 0, 100))
print(time.time() - start_time)

