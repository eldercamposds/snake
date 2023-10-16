class Cores:
    def cores(self, preta, branca, vermelha, verde):
        self._preta = (0, 0, 0)
        self._branca = (255, 255, 255)
        self._vermelha = (255, 0, 0)
        self._verde = (0, 255, 0)

    @property
    def preta(self):
        return self._preta
        