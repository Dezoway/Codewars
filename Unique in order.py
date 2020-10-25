def unique_in_order(value):
    iterable = []  # This function cuts off duplicate elements to a different value.If this item
    # is repeated further in the list, it will be added to the new list.
    for i, x in enumerate(value):  # The list generator creates a position\value, and assigns them to two
        # variables in the loop condition
        try:  # This is where the exception check starts,as we will have 2 errors
            if x not in value[i + 1]:
                iterable.append(x)
        except IndexError:  # The value error will be in any case because the index increment occurs, even at the end
            # of the list.
            iterable.append(x)
        except TypeError:  # A type error will occur if the list contains elements of the int type and so on.,
            if x != value[i + 1]:
                iterable.append(x)
    return iterable


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order("ABBCcAD"))
print(unique_in_order([1, 2, 2, 3, 3, 4, 4, 3, 3]))
