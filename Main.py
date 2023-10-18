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
vermelha = (255, 0, 0)
verde = (0, 255, 0)

#parametros 
tamanho_quadrado = 10
velocidade_atualizacao = 15

def gerar_comida():#gerar posição das comidas
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura- tamanho_quadrado)/ float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenha_comida(tamanho, comida_x, comida_y): #desenhar comidas na tela
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenha_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho] )

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 10)
    texto = fonte.render(f"Pontos: {pontuacao}", False, vermelha)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0

    return velocidade_x, velocidade_y



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
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

                
        # desenha comida
        desenha_comida(tamanho_quadrado, comida_x, comida_y)

        #atualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        # desenhar cobra
        pixel.append([x, y])
        if len(pixel) > tamanho_cobra:
            del pixel[0]
            
        for pixel in pixel[:-1]: # verificando se a cobra bateu no proprio corpo
            if pixel == [x, y]:
                fim_jogo = True

        desenha_cobra(tamanho_quadrado, pixel)

        desenhar_pontuacao(tamanho_cobra - 1)

        #atualização da tela
        pygame.display.update()

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_y, comida_x = gerar_comida()

        relogio.tick(velocidade_atualizacao)

rodar_jogo()