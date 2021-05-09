class Counter:
    def __init__(self, licz, pth):
        self._licz = licz
        self._pth = pth

    def get_licz(self):
        return self._licz

    def get_pth(self):
        return self._pth

    def set_licz(self, licz):
        self._licz = licz

    def set_pth(self, pth):
        self._pth = pth
