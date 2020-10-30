def find_even_in(array):  # This function defines the middle of the array at the arithmetic level(the sum of elements)
    r=0
    for z,x in enumerate(array):    # This loop iterates through the array elements including the element indexes
        m= sum(array[:z+1]) # The variable is assigned the sum of elements up to the index of the array iteration
        n= sum(array[z:])   # The variable is assigned the sum of elements from the iteration index of the array
        if m == n:    # If the variables are equal then stop the loop and assign the current iteration to the variable r
            r=z
            break
    if m == n:  # Here we compare again because if the loop block contains the if else construction the loop will
        # output only the else option
        return r
    else:
        return -1









