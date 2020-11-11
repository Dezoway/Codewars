def tribonacci(signature, n):
    """Returns a list of Fibonacci numbers with the sum of the last 3 numbers"""
    i = 0
    z = 1
    m = 2
    for x in range(n-len(signature)):
        signature.append(signature[i]+signature[z]+signature[m])
        i += 1
        z += 1
        m += 1
    return signature[:n]


print(tribonacci([1, 1, 1], 10))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([300, 200, 100], 0))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([0, 0, 0], 10))
print(tribonacci([0.5, 0.5, 0.5],30))