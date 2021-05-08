class Counter:
    def __init__(self, licz, pth, x1, y1, x2, y2):
        self._licz = licz
        self._pth = pth
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def get_licz(self):
        return self._licz

    def get_pth(self):
        return self._pth

    def get_x1(self):
        return self._x1

    def get_y1(self):
        return self._y1

    def get_x2(self):
        return self._x2

    def get_y2(self):
        return self._y2

    def set_licz(self, licz):
        self._licz = licz

    def set_pth(self, pth):
        self._pth = pth

    def set_x1(self, x1):
        self._x1 = x1

    def set_y1(self, y1):
        self._y1 = y1

    def set_x2(self, x2):
        self._x2 = x2

    def set_y2(self, y2):
        self._y2 = y2
