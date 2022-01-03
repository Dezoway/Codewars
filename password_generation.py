import random
exc = ['l', 'I', '1', 'o', 'O', '0']
k = [x for x in range(48, 58)]+[x for x in range(65, 91)]+[x for x in range(97, 123)]


def generate_password(length):
    '''Вспомогательная функция, генерирует пароли по определённому правилу в задании'''
    password = ''
    while len(password) != length:
        t = chr(k[random.randrange(0, len(k))])
        if t not in exc:
            if len(password) == 0:
                t = chr(random.randint(48, 57))
                if t not in exc: password += t
            elif len(password) == 1:
                t = chr(random.randint(65, 90))
                if t not in exc:password += t
            elif len(password) == 2:
                t = chr(random.randint(97, 122))
                if t not in exc:password += t
            else:
                password += t
    return password

def generate_passwords(count,length):
    '''Функция-генератор паролей, на вход получает количсетво паролей и их длину, через цикл вывзывает вспомогательную
    функцию.'''
    passwords = []
    for x in range(count):
        passwords.append(generate_password(length))
    return passwords


print(*generate_passwords(int(input(),int(input()))), sep='\n')