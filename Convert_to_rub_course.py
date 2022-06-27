class MoneyR:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):return self.__cb

    @cb.setter
    def cb(self, cb):self.__cb = cb

    @property
    def volume(self):return self.__volume

    @volume.setter
    def volume(self, volume):self.__volume = volume

    def check(self):
        if not self.cb:raise ValueError('Незивестен курс валют.')

    def convertion_to_rub(self):
        self.check()
        return round(self.volume,1)

    def __eq__(self, other):return self.convertion_to_rub() == other.convertion_to_rub()

    def __lt__(self, other):return self.convertion_to_rub() < other.convertion_to_rub()

    def __le__(self, other):return self.convertion_to_rub() <= other.convertion_to_rub()


class MoneyD:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    def check(self):
        if not self.cb:raise ValueError('Незивестен курс валют.')

    @property
    def cb(self):return self.__cb

    @cb.setter
    def cb(self, cb):self.__cb = cb

    @property
    def volume(self):return self.__volume

    @volume.setter
    def volume(self, volume):self.__volume = volume

    def convertion_to_rub(self):
        self.check()
        return round(self.volume * self.cb.rates['rub'],1)

    def __eq__(self, other):return self.convertion_to_rub() == other.convertion_to_rub()

    def __lt__(self, other):return self.convertion_to_rub() < other.convertion_to_rub()

    def __le__(self, other):return self.convertion_to_rub() <= other.convertion_to_rub()


class MoneyE:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def check(self):
        if not self.cb:raise ValueError('Незивестен курс валют.')

    def convertion_to_rub(self,):
        self.check()
        return round(self.volume / self.cb.rates['euro']*self.cb.rates['rub'], 1)

    def __eq__(self, other): return self.convertion_to_rub() == other.convertion_to_rub()

    def __lt__(self, other): return self.convertion_to_rub() < other.convertion_to_rub()

    def __le__(self, other): return self.convertion_to_rub() <= other.convertion_to_rub()


class CentralBank:

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = CentralBank