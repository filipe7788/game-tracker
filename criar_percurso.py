import pygame
import sys
import os
import csv 


# Lista para armazenar os pontos desenhados


# Função para exibir a tela de criação de percurso
def exibir_criar_percurso_tela(tela, estado_da_tela, voltar_ao_menu, ir_para_salvar):
    pontos_desenhados = []

    botao_salvar_clicado = False  # Inicializa a variável botao_salvar_clicado como False
    # Variável para rastrear se o mouse está pressionado
    mouse_pressionado = False

    espaco_entre_botoes = 60

    # Cores
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    vermelho = (255, 0, 0)

    fonte = pygame.font.Font(None, 36)
    largura, altura = 1920, 1080
    area_desenho = pygame.Rect(0, 0, largura, altura - 200)  # Área acima do botão "Salvar"


    # Área do botão "Salvar"
    largura_botao_salvar = 200
    altura_botao_salvar = 80
    x_botao_salvar = ((largura - largura_botao_salvar) // 2) + 120  # Centralizado na largura da tela
    y_botao_salvar = altura - altura_botao_salvar - 60  # 60 pixels da margem inferior

    # Área do botão "Voltar"
    largura_botao_voltar = 200
    altura_botao_voltar = 80
    x_botao_voltar = x_botao_salvar - largura_botao_voltar - espaco_entre_botoes  # Separados por 60 pixels
    y_botao_voltar = y_botao_salvar
    linhas = []

    while estado_da_tela == "criar_percurso":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and area_desenho.collidepoint(evento.pos):
                # Inicia o desenho ao pressionar o botão esquerdo do mouse dentro da área de desenho
                mouse_pressionado = True
            elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                # Finaliza o desenho ao soltar o botão esquerdo do mouse
                mouse_pressionado = False
                # Verifique se o clique foi no botão "Salvar"
                if pygame.Rect(x_botao_salvar, y_botao_salvar, largura_botao_salvar, altura_botao_salvar).collidepoint(evento.pos):
                    botao_salvar_clicado = True  # Ativar o efeito de clique
                    estado_da_tela = "salvar_percurso_tela"
                    ir_para_salvar(pontos_desenhados)
                # Verifique se o clique foi no botão "Voltar"
                elif pygame.Rect(x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar).collidepoint(evento.pos):
                    estado_da_tela = "menu"  # Retorna à tela anterior (menu)
                    voltar_ao_menu()

        # Desenhar o percurso enquanto o mouse está pressionado
        if mouse_pressionado:
            pos_mouse = pygame.mouse.get_pos()
            if area_desenho.collidepoint(pos_mouse):
                pontos_desenhados.append(pos_mouse)
                if len(pontos_desenhados)>= 2:
                    linhas.append((pontos_desenhados[-1], pontos_desenhados[-2]))

        # Preencha a área de desenho com branco
        tela.fill(branco, area_desenho)

        # Desenhe os pontos em vermelho
        for ponto in pontos_desenhados:
            pygame.draw.circle(tela, vermelho, ponto, 5)            

        for i in linhas:
            pygame.draw.line(tela, vermelho, i[-2], i[-1], 4)            

        # Botão "Salvar" na parte inferior da tela
        cor_botao_salvar = preto if botao_salvar_clicado else (100, 100, 100)  # Cor mais escura quando clicado
        pygame.draw.rect(tela, cor_botao_salvar, (x_botao_salvar, y_botao_salvar, largura_botao_salvar, altura_botao_salvar), border_radius=20)
        texto_salvar = fonte.render("Salvar", True, branco)
        texto_salvar_rect = texto_salvar.get_rect(center=(x_botao_salvar + largura_botao_salvar // 2, y_botao_salvar + altura_botao_salvar // 2))
        tela.blit(texto_salvar, texto_salvar_rect)

        # Botão "Voltar" ao lado do botão "Salvar"
        pygame.draw.rect(tela, preto, (x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar), border_radius=20)
        texto_voltar = fonte.render("Voltar", True, branco)
        texto_voltar_rect = texto_voltar.get_rect(center=(x_botao_voltar + largura_botao_voltar // 2, y_botao_voltar + altura_botao_voltar // 2))
        tela.blit(texto_voltar, texto_voltar_rect)

        # Atualize a tela
        pygame.display.flip()
