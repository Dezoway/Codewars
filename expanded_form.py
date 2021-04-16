def expanded(num):
    discharge = list()
    z = str(num)
    for x in range(len(z)):
        digit = z[x]+'0'*(len(z)-x-1)
        if digit.count('0') == len(digit):
            continue
        discharge.append(digit)
    return ' + '.join(discharge)




print(expanded(4))