def dig_pow(n,k):   # This function receives 2 numbers as input
    # The first number will be decomposed into digits,the 2 number is the initial power
    # from the first digit in the first number.
    # Then the degree will be incremented with each iteration.
    z = str(n)    # Here an integer variable is converted to a string type for iteration in a loop
    x1 = 0    # Initializing an integer variable that will assign itself a value from the loop
    for x in z:  # A string consisting of digits is iterated over
        x1 += int(x)**k   # This is where each character of the string (a digit of a number) is converted to an integer
        # type. And thus each digit is raised to a power that is incremented with each iteration.
        k += 1
    m = x1 // n  # Here the integer remainder of the division is assigned to the variable
    if n * m == x1: # If the original number multiplied by the remainder is x1 then return the remainder.Otherwise
        # return -1
        return m
    else:
        return -1








print(dig_pow(89,1))
print(dig_pow(695,2))
print(dig_pow(92,1))
print(dig_pow(46288,3))