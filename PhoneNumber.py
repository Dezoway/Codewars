def create_phone_number(n):
    string=''.join([str(x) for x in n])
    return '({0}) {1}-{2}'.format(string[:3], string[3:6], string[6:])





print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))