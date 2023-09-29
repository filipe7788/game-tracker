import pygame
import os
import sys

# Função para exibir a tela de percursos
def exibir_lista_de_percursos(tela, estado_da_tela, selecionar_percurso, voltar_ao_menu):
       # Cores
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    vermelho = (255, 0, 0)

    fonte = pygame.font.Font(None, 36)
    largura, altura = 1920, 1080
    area_desenho = pygame.Rect(0, 0, largura, altura - 100)  # Área acima do botão "Salvar"

    # Verifique e liste os arquivos na pasta "trajetos"
    if not os.path.exists("trajetos"):
        os.mkdir("trajetos")  # Crie a pasta "trajetos" se não existir

    lista_de_percursos = []  # Lista para armazenar os percursos disponíveis
    lista_retangulos_percursos = []  # Lista de retângulos clicáveis dos percursos
    percurso_selecionado = None  # Armazena o percurso selecionado

    for arquivo in os.listdir("trajetos"):
        if arquivo.endswith(".csv"):
            lista_de_percursos.append(arquivo)


    # Preencha a tela com branco
    tela.fill(branco)
    largura_botao_voltar = 200
    altura_botao_voltar = 80
    x_botao_voltar = (largura - largura_botao_voltar) // 2  # Centralizado na largura da tela
    y_botao_voltar = altura - altura_botao_voltar - 60  # 60 pixels da margem inferior

    while estado_da_tela == "percursos":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if percurso_selecionado is None:
                    # Verifique se algum trajeto foi selecionado
                    for i, retangulo in enumerate(lista_retangulos_percursos):
                        if retangulo.collidepoint(evento.pos):
                            percurso_selecionado = i
                            estado_da_tela = "trajeto_selecionado"  # Mude para a tela de trajeto selecionado
                            selecionar_percurso(lista_de_percursos[i])

                            break
                    if pygame.Rect(x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar).collidepoint(evento.pos):
                        estado_da_tela = "menu"  # Retorna à tela anterior (menu)
                        voltar_ao_menu()

        # Lista os percursos disponíveis
        texto_titulo = fonte.render("Percursos Disponíveis", True, preto)
        tela.blit(texto_titulo, (40, 40))
        pygame.draw.rect(tela, preto, (x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar), border_radius=20)
        texto_voltar = fonte.render("Voltar", True, branco)
        texto_voltar_rect = texto_voltar.get_rect(center=(x_botao_voltar + largura_botao_voltar // 2, y_botao_voltar + altura_botao_voltar // 2))
        tela.blit(texto_voltar, texto_voltar_rect)
        for i, arquivo in enumerate(lista_de_percursos):
            # Retângulo clicável do percurso
            retangulo = pygame.Rect(40, 100 + i * 60, largura - 80, 50)
            lista_retangulos_percursos.append(retangulo)

            # Preencha os retângulos dos percursos
            pygame.draw.rect(tela, preto, retangulo, border_radius=20)

            # Nome do arquivo (sem a extensão .csv)
            nome_arquivo = os.path.splitext(arquivo)[0]
            texto_percurso = fonte.render(nome_arquivo, True, branco)
            tela.blit(texto_percurso, (50, 115 + i * 60))

        # Atualize a tela
        pygame.display.flip()
