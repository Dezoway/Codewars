import pandas as pd # Импортирование библиотеки Pandas и замена имени на более короткое
import math # Импортирование библиотеки math

# Тест 1

def get_status(content):        # Функция получения статуса
    #Функия возращает старое и новое значения статуса
    if content.split().in
    start_status = ''
    finish_status = ''
    return 'start_status = <<'+start_status+'>>, '+'finish_status = <<'+finish_status+'>>'  #Вернуть значения статуса

print(get_status(input('Вход: ')))  # В выводе сразу вызываем функцию в которую передаётся строка введенная пользователем по умолчанию тип ввода-str.

# Тест 2
'''
def unfun(x):           # Функция вычисления
    y = math.pow(x,3) * math.exp(math.sin(x/2))     # Используем exp и sin из библиотеки math
    return y        # Возвращаем готовый результат

print('Выход: y=',unfun(float(input('Вход: x=')))) # В выводе вызываем сразу функцию в которую передаётся ввод пользователя, входные данные сразу преобразованы в тип float.


def get_df(start_x, finish_x, n_points):
   Функция возвращающая значения от заданной математической функции в табличном формате Data Frame.
    Так как в условии задания начальное значение меньше конечного то итерации будут проходить в положительную сторону.
    counter = len(range(start_x,finish_x))/n_points     # Устанавливаем градацию от одного числа к другому расстояние между двумя точками / количество точек.
    table = {'x':[], 'y':[]}        # Создаем словарь с ключами x, y, у каждого ключа список для значений.
    pd.set_option('display.max_rows',None)      # Задаём в функции развёрнутую таблицу, т.к по умолчанию pandas сворачивает таблицу.
    while start_x < finish_x:      # Продолжать цикл пока начальное значение меньше конечного значения.
        table['x'].append(round(start_x,2)) #Добавляем в список словаря по ключу округленное до 2 знаков после запятой значение x.
        table['y'].append(round(math.pow(start_x,2)*math.exp(math.sin(start_x/3)),3))   #   Добавляем в список словаря по ключу округленное до 3 знаков после запятой значение заданной функции
        start_x += counter          #   С каждой итерацией происходит градация начального значения на counter.

    return pd.DataFrame(data=table, index=range(1,n_points+2))  # Возвращаем готовое значение в табличном формате. В параметре data передаём готовый словарь. В парпаметре index передаём нумерацию строк.
    #   Так как нумерация индексов начинается с 0 и функция range итерирует в диапазоне [0;n) то выставим условие от 1 до n_points+2.
print('Вход')
start_x = int(input('start_x='))    # Входные данные от пользователя, у каждой переменной задан тип integer
finish_x = int(input('finish_x='))
n_points = int(input('n_points='))
print(get_df(start_x, finish_x, n_points))  # В выводе вызываем функцию в которую сразу передаём значения.
'''