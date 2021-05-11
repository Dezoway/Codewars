def fibb(integer):
    '''Данная функция находит произведение двух соседних чисел для заданной последовательнсти
    Если произведение двух соседних чисел равно заданной последовательности то вернуть два числа и True
    Или если произведение двух соседних чисел больше заданной последовательности то вернуть два числа и False'''
    value1 = value2 = 1
    tmp = 0
    array = []
    if integer == 0:
        return [0, 1, True]
    elif integer == 1:
        return [1, 1, True]
    for x in range(integer):
        tmp = value1+value2
        value1 = value2
        value2 = tmp
        print(tmp)
        if value1 * value2 == integer:
            array += value1, value2, True
            break
        elif value1 * value2 > integer:
            array += value1, value2, False
            break
    return array