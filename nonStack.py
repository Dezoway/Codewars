class StackObj:
    def __init__(self, data):
        self.__next = None
        self.__data = data

    @property
    def next(self):
        return self.__next

    @property
    def data(self):
        return self.__data

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or not next:
            self.__next = next

    @data.setter
    def data(self, data):
        self.__data = data

class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top == None:
            self.top = obj
        else:
            k = self.top
            while k.next:
                k = k.next
            k.next = obj
    def pop(self):
        if not self.top.next:self.top = None
        else:
            k = self.top
            while k.next.next:
                k = k.next
            k.next = None

    def get_data(self):
        k = self.top
        lst = []
        while k:
            lst.append(k.data)
            k = k.next
        return lst
