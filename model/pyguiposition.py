class ClickPositions:
    def __init__(self, pos1x, pos1y, pos2x, pos2y):
        self._pos1x = pos1x
        self._pos1y = pos1y
        self._pos2x = pos2x
        self._pos2y = pos2y

    def get_pos1x(self):
        return self._pos1x

    def get_pos1y(self):
        return self._pos1y

    def get_pos2x(self):
        return self._pos2x

    def get_pos2y(self):
        return self._pos2y

    def set_pos1x(self, pos1x):
        self._pos1x = pos1x

    def set_pos1y(self, pos1y):
        self._pos1y = pos1y

    def set_pos2x(self, pos2x):
        self._pos2x = pos2x

    def set_pos2y(self, pos2y):
        self._pos2y = pos2y
