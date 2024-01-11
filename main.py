#config iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores RGB
preta = (0, 0, 0)
roxa = (255, 0, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

#parametros da cobrinha
tamanho_quadrado = 10
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobrinha(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, roxa, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 15)
    texto = fonte.render(f"PONTINHOS: {pontuacao}", True, vermelha)
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

    tamanho_cobrinha = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        #desenhar_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        #encerrar jogo se bater nas laterais
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # atualizar posiçao da cobrinha
        x += velocidade_x
        y += velocidade_y

        #desenhar_cobrinha
        pixels.append([x, y])
        if len(pixels) > tamanho_cobrinha:
            del pixels[0]

        #se a cobrinha bateu no corpinho (menos na cabeça)
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobrinha(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_cobrinha - 1)

        #atualizaçao da tela
        pygame.display.update()

        #criar uma nova comidinha
        if x == comida_x and y == comida_y:
            tamanho_cobrinha += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

rodar_jogo()