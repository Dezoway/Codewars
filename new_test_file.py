from tkinter import *
from tkinter import messagebox
import random, time, os


def var1():
    window1 = Tk()
    window1.geometry('400x400')
    window1.title('Переворот строки 1.0')
    text_var1 = Label(window1, text='Добро пожаловать в программу переворт строки 1.0', font='Times 12')
    text_var1.place(x=1, y=1)
    text_var1_2 = Label(window1, text='Введите строку которую хотите перевернуть:', font='Times 12')
    text_var1_2.place(x=1, y=25)
    user_enter = Entry(window1)
    user_enter.place(x=1, y=50)

    def text1():
        strings = user_enter.get()
        if strings.lower() == strings.lower()[::-1]:
            messagebox.showinfo('Готово!', 'Перевёрнутая строка:' + strings[::-1] + '\nВау!Да это же строка па'
                                                                                    'линдром')
        else:
            messagebox.showinfo('Готово!', 'Перевёрнутая строка:' + strings[::-1])

    user_button = Button(window1, text='Клик', command=text)
    user_button.place(x=150, y=50)




def var2():
    zero = 0
    full = 100
    computer = random.randrange(zero, full)

    def allis():
        global_text = Label(window, text='Вы загадали:' + str(computer) + '?')
        global_text.place(x=0, y=50)
        ranges = full - zero
        print(ranges)

    def b():
        nonlocal computer, zero, full
        zero = computer
        computer = int(random.randrange(zero, full))
        allis()

    def s():
        nonlocal computer, zero, full
        full = computer
        computer = int(random.randrange(zero, full))
        allis()

    def choice():
        button_var2.destroy()
        button_choice_y = Button(window, text='Да', command=window.destroy)
        button_choice_s = Button(window, text='Больше', command=b)
        button_choice_b = Button(window, text='Меньше', command=s)
        button_choice_y.place(x=0, y=100)
        button_choice_b.place(x=45, y=100)
        button_choice_s.place(x=200, y=100)
        print('as')
        allis()
    window = Tk()
    window.geometry('400x400')
    window.title('Отгадывание числа 1.0')
    text_var2 = Label(window, text='Загадайте число от 0 до 100\nВы готовы?')
    text_var2.place(x=0, y=0)
    button_var2 = Button(window, text='Да', command=choice)
    button_var2.place(x=0, y=50)



def var3():
    window = Tk()
    window.geometry('600x600')
    window.title('База данных пользователей')
    text_window3 = Label(window, text='В данной базе данных хранятся пользователи которые\n использовали данную '
                                      'программу:', font='Times 14')
    text_window3.place(x=1, y=1)


def close():
    new_file.quit()


def clicked(new_file):
    btn1 = Button(new_file, text='Переворот строки', comman=var1)
    btn2 = Button(new_file, text='Отгадывание чисел', command=var2)
    btn3 = Button(new_file, text='База данных', command=var3)
    btn4 = Button(new_file, text='Выйти из программы', command=close)
    btn1.place(x=1, y=50)
    btn2.place(x=1, y=75)
    btn3.place(x=1, y=100)
    btn4.place(x=1, y=125)


def main_window():
    new_file = Tk()
    new_file.title('Программа пользовательский ввод 1.0')
    new_file.geometry('600x600')
    text = Label(new_file, text='Добро пожаловать в мою первую универсальную программу 1.0',
                 font=('Times New Roman 50', 15))
    text.grid(column=0, row=0)
    text2 = Label(new_file, text='Выберите 1 из 3 вариантов исполнения программы:')
    text2.place(x=1, y=30)
    clicked(new_file)
    new_file.mainloop()


entered_name = Tk()
entered_name.title('Инициализация')
entered_name.geometry('300x300')
text = Label(entered_name, text='Пожалуйста введите своё имя:', font=('Arial', 12))
text.place(x=1, y=1)

def user():
    string = enter_user.get()
    if len(string) == 0:
        messagebox.showinfo('Неверное имя', 'Вы задали неверное имя,попробуйте снова')
    else:
        file = open('table.txt', 'a')
        file.writelines(string+'\n')


user_button = Button(entered_name, text='Клик', command = user)
enter_user = Entry(entered_name)
enter_user.place(x=0, y=25)
user_button.place(x=150, y=25)
entered_name.mainloop()
