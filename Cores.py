class Cores():
    def __init__(self, cor):
        self._cor = cor
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, cor):
        if (cor == "preta".strip().split()):
            self._cor = (0,0,0)
        if (cor == "verde"):
            self._cor = (0, 255, 0)

# teste = Cores.cor.setter("verde")

# print(teste)
     
        # self._branca = (255, 255, 255)
        # self._vermelha = (255, 0, 0)
        # self._verde = (0, 255, 0)



