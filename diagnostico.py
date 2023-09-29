import pygame
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io

def exibir_diagnostico_tela(estado_da_tela, tela, voltar):
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

    while estado_da_tela == "diagnostico":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar).collidepoint(evento.pos):
                    estado_da_tela = "menu"  # Retorna à tela anterior (menu)
                    voltar()

            # Preencher a tela com a cor branca
        tela.fill(branco)

        # Plotar o gráfico usando matplotlib
        fig = Figure(figsize=(8, 6), dpi=80)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        x = [1,2,3]
        y = [1 ,2 ,3]
        ax.plot(x, y)

        buf = io.BytesIO()
        canvas.print_figure(buf, format='png')
        buf.seek(0)
        graph_surface = pygame.image.load(io.BytesIO(buf.read()))
        
        tela.blit(graph_surface, (400, 400))  # Exibir o gráfico na tela

        # Botão "Voltar" ao lado do botão "Salvar"
        pygame.draw.rect(tela, preto, (x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar), border_radius=20)
        texto_voltar = fonte.render("Voltar", True, branco)
        texto_voltar_rect = texto_voltar.get_rect(center=(x_botao_voltar + largura_botao_voltar // 2, y_botao_voltar + altura_botao_voltar // 2))
        tela.blit(texto_voltar, texto_voltar_rect)
        pygame.display.flip()