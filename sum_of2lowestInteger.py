def smallest_integer(array):
    i1=min(array)
    array.remove(i1)
    i2=min(array)
    return i1+i2




print(smallest_integer([5,8,12,18,22]))
print(smallest_integer([7,15,12,18,22]))