def iq_test(numbers):
    array = numbers.split(" ")
    array = [int(x) for x in array]
    even = odd = 0
    count_even = count_odd = 0
    for x in range(len(array)):
        if array[x] % 2 == 0:
            even=x+1
            count_even+=1
        else:
            odd=x+1
            count_odd+=1
    if count_even > count_odd:
        return odd
    else:
        return even







print(iq_test("2 4 7 8 10"))
print(iq_test("1 4 8 10 12"))
print(iq_test("2 3 5 7 9"))