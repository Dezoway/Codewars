class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj
def rev(count,lst):
    if(count == len(lst)-1):
        return ListObject(lst[count],None)
    return ListObject(lst[count],rev(count+1,lst))
txt = '''1. Первые шаги в ООП
1.1 Как правильно проходить этот курс
1.2 Концепция ООП простыми словами
1.3 Классы и объекты. Атрибуты классов и объектов
1.4 Методы классов. Параметр self
1.5 Инициализатор init и финализатор del
1.6 Магический метод new. Пример паттерна Singleton
1.7 Методы класса (classmethod) и статические методы (staticmethod)'''
lst_in = [x for x in txt.split('\n')]
head_obj = ListObject(lst_in[0],rev(1,lst_in))