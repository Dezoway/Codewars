def highest_rank(array):  # This function counts how many times a digit is included in the array and outputs the largest value that occurs the most
    z = 0  # The variables Z and j initialize the count of how many times a given number occurs and how large it is
    j = 0
    for x in array:
        if array.count(x) >= z:     # If this number occurs more than the value of z,then z=x,  j is equal to the value itself
            z = array.count(x)
            j = x
            for m in array:         #A nested loop is used here
                if m > j and array.count(m) >= z:   # If m is greater than j and the number of repetitions m is greater than the number of repetitions I then j=m
                    j = m
    return j


print(highest_rank([12, 10, 8, 8, 7, 7, 3, 1, 5]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))
print(highest_rank([10, 10, 10, 12, 12, 12, 4, 3, 1]))
