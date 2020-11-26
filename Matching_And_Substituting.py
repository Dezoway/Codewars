import json
def change(s1=None, prog=None, version=None):
    NAME = 'g964 '
    DATETIME = '2019-01-01 '
    NUMBER = '+1-503-555-0090 '
    counts = 0
    array_s1 = [[x+' ' for x in i.split(' ')] for i in s1.split('\n')]
    array_s1[0][0] = 'Program: '
    array_s1[1][1] = NAME
    array_s1[4][1] = DATETIME
    del array_s1[2], array_s1[5], array_s1[0][1], array_s1[3][2:]
    array_s1[0][1] = prog+' '
    print(array_s1)
    for x in array_s1[2][1]:
        if x.isdigit():
            counts +=1
    if counts < 11:
        return 'ERROR: VERSION or PHONE'
    else:
        array_s1[2][1] = NUMBER
    if version[0] == '.' and array_s1[4][1][0] == '.' or len(version) == 1 and len(array_s1[4][1]) == 1:
        return'ERROR: VERSION or PHONE'
    elif version[0] != '.' and array_s1[4][1][0] == '.' or len(version):
        array_s1[4][1] = version
    elif version[0] == '.' and array_s1[4][1][0] != '.':
        pass
    elif version.count('.') >= 2 and array_s1[4][1].count('.') >= 2:
        return 'ERROR: VERSION or PHONE'
    elif version.count('.') >= 2 and array_s1[4][1].count('.') < 2:
        pass

    else:
        array_s1[4][1] = version

    return (''.join([''.join([x for x in i]) for i in array_s1]).rstrip())
s1 = '''Program title: Hammer\nAuthor: Tolkien\nCorporation: IB\nPhone: +1-503-555-0090\nDate: Tues March 29, 2017\nVersion: 3.0\nLevel: Release'''
print(change(s1,'Honor2s','2'))