import pygame
import random
from Cores import *

pygame.init()# inicializar o pygame
pygame.display.set_caption("Snake Python")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores
preta =  (0, 0, 0)
branca = (255, 255, 255)
svermelha = (255, 0, 0)
verde = (0, 255, 0)

#parametros cobrinha
tamanho_quadrado = 10
velocidade_atualizacao = 15

def gerar_comida():#gerar posição das comidas
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
    comida_y = round(random.randrange(0, altura- tamanho_quadrado)/ tamanho_quadrado) * tamanho_quadrado
    return comida_x, comida_y

def desenha_comida(tamanho, comida_x, comida_y): #desenhar comidas na tela
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def rodar_jogo():
    fim_jogo = False

    x = largura / 2 
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixel = []

    comida_x , comida_y = gerar_comida()
    

    while not fim_jogo:

        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
                
        # desenha comida
        desenha_comida(tamanho_quadrado, comida_x, comida_y)

        #atualização da tela
        pygame.display.update()
        relogio.tick(velocidade_atualizacao)

rodar_jogo()