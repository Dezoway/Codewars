def tickets(people):
    TICKET = 25
    array = list(filter(lambda x: x == TICKET, people))
    array2 = list(filter(lambda x: x != TICKET, people))
    if len(array) == 0:
        return "NO"
    for x in range(len(array2)):
        for j in range(len(array)):
            array2[x] -= array[j]
            array[j] -=array[j]
            if array2[x] == 0:
                break
    if sum(array2[:len(array2)]) == 0:
        return "YES"
    else:
        return "NO"




print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100]))
print(tickets([50, 50, 100]))
print(tickets([50, 50, 50, 50, 50]))
print(tickets([25, 25, 25, 25, 25, 25, 25, 25, 50]))
print(tickets([25,25,25,50,100]))
print(tickets([100,100,25,25]))