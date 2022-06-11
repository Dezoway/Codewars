class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None and self.tail is None:
            self.head = obj
            self.tail = obj
            obj.set_next(None)
            obj.set_prev(None)

        else:
            obj.set_next(None)
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj

    def remove_obj(self):
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self):
        lst = []
        k = self.head
        while k :
            lst.append(k.get_data())
            k = k.get_next()
        return lst

class ObjList:
    def __init__(self, data):
        self.__prev = None
        self.__next = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj


    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
