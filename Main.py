import pygame
import random
import Cores

pygame.init()# inicializar o pygame
pygame.display.set_caption("Snake Python")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores
black = Cores

#parametros cobrinha
tamanho_quadrado = 10
velocidade_cobra = 15

#loop
def rodar_jogo():
    fim_jogo = False

    while not fim_jogo:

        tela.fill(black)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
        