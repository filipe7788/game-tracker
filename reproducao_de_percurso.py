import pygame
import sys
import csv
import os
from peyetribe import EyeTribe

# Função para exibir o trajeto selecionado com um círculo percorrendo-o
def exibir_trajeto_selecionado_tela(estado_da_tela, tela, trajeto_selecionado, voltar_para_lista, ir_para_diagnostico):
    arquivo_selecionado = trajeto_selecionado
    # Cores
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    vermelho = (255, 0, 0)

    fonte = pygame.font.Font(None, 36)
    largura, altura = 1920, 1080

    # Área do botão "Salvar"
    largura_botao_salvar = 200
    altura_botao_salvar = 80
    x_botao_salvar = ((largura - largura_botao_salvar) // 2) + 120  # Centralizado na largura da tela
    y_botao_salvar = altura - altura_botao_salvar - 60  # 60 pixels da margem inferior

    # Área do botão "Voltar"
    largura_botao_voltar = 200
    altura_botao_voltar = 80
    x_botao_voltar = x_botao_salvar - largura_botao_voltar - 60  # Separados por 60 pixels
    y_botao_voltar = y_botao_salvar

    # Carregue os pontos do trajeto selecionado
    trajeto_selecionado = []
    with open(os.path.join("trajetos", arquivo_selecionado), mode='r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        next(reader)  # Pule a primeira linha (cabeçalho)
        for linha in reader:
            trajeto_selecionado.append((int(linha[0]), int(linha[1])))

    # Variáveis para rastrear a posição do círculo
    posicao_circulo = 0
    velocidade_circulo = 3  # Ajuste a velocidade conforme necessário
    contador_frames = 0  # Contador de frames para controlar a velocidade

    isPlay = False

    tracker = EyeTribe(host="localhost", port=6555)
    tracker.connect()
    n = [tracker.next()]
    tracker.pushmode()


    while estado_da_tela == "trajeto_selecionado":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                if texto_voltar_rect.collidepoint(evento.pos):
                    isPlay = not isPlay  # Ativar o efeito de clique
                elif texto_salvar_rect.collidepoint(evento.pos):
                    estado_da_tela = "diagnostico"
                    ir_para_diagnostico(n)
        # Preencha a tela com branco
        tela.fill(branco)

        # Desenhe o trajeto selecionado
        for i in range(len(trajeto_selecionado) - 1):
            pygame.draw.line(tela, vermelho, trajeto_selecionado[i], trajeto_selecionado[i + 1], 5)  

        if isPlay:
            # Atualize a posição do círculo com base na velocidade
            if contador_frames % velocidade_circulo == 0:
                posicao_circulo += 1
                n.append(tracker.next())

            # Verifique se o círculo chegou ao final do trajeto
            if posicao_circulo >= len(trajeto_selecionado):
                posicao_circulo = 0
                isPlay = False
                tracker.pullmode()
            

        # Desenhe o círculo vermelho na posição atual
        pygame.draw.circle(tela, vermelho, trajeto_selecionado[posicao_circulo], 10)

        contador_frames += 1

        pygame.draw.rect(tela, preto, (x_botao_salvar, y_botao_salvar, largura_botao_salvar, altura_botao_salvar), border_radius=20)
        texto_salvar = fonte.render("Diagnóstico", True, branco)
        texto_salvar_rect = texto_salvar.get_rect(center=(x_botao_salvar + largura_botao_salvar // 2, y_botao_salvar + altura_botao_salvar // 2))
        tela.blit(texto_salvar, texto_salvar_rect)


        # Botão "Voltar" ao lado do botão "Salvar"
        pygame.draw.rect(tela, preto, (x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar), border_radius=20)
        texto_voltar = fonte.render("Play", True, branco)
        texto_voltar_rect = texto_voltar.get_rect(center=(x_botao_voltar + largura_botao_voltar // 2, y_botao_voltar + altura_botao_voltar // 2))
        tela.blit(texto_voltar, texto_voltar_rect)
        pygame.display.flip()