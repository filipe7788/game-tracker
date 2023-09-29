import pygame
import sys
import csv
import os
# Função para exibir o trajeto selecionado com um círculo percorrendo-o
def exibir_trajeto_selecionado_tela(estado_da_tela, tela, trajeto_selecionado):
    arquivo_selecionado = trajeto_selecionado
    # Cores
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    vermelho = (255, 0, 0)
    # Carregue os pontos do trajeto selecionado
    trajeto_selecionado = []
    with open(os.path.join("trajetos", arquivo_selecionado), mode='r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        next(reader)  # Pule a primeira linha (cabeçalho)
        for linha in reader:
            trajeto_selecionado.append((int(linha[0]), int(linha[1])))

    # Variáveis para rastrear a posição do círculo
    posicao_circulo = 0
    velocidade_circulo = 2  # Ajuste a velocidade conforme necessário
    contador_frames = 0  # Contador de frames para controlar a velocidade

    while estado_da_tela == "trajeto_selecionado":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                estado_da_tela = "percursos"

        # Preencha a tela com branco
        tela.fill(branco)

        # Desenhe o trajeto selecionado
        for i in range(len(trajeto_selecionado) - 1):
            pygame.draw.line(tela, vermelho, trajeto_selecionado[i], trajeto_selecionado[i + 1], 5)

        # Atualize a posição do círculo com base na velocidade
        if contador_frames % velocidade_circulo == 0:
            posicao_circulo += 1

        # Verifique se o círculo chegou ao final do trajeto
        if posicao_circulo >= len(trajeto_selecionado):
            posicao_circulo = 0

        # Desenhe o círculo vermelho na posição atual
        pygame.draw.circle(tela, vermelho, trajeto_selecionado[posicao_circulo], 10)

        # Atualize a tela
        pygame.display.flip()

        contador_frames += 1