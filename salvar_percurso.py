import pygame
import os, csv, sys

def salvar_percurso_tela(tela, estado_da_tela, trajeto_selecionado, voltar_ao_menu):


    botao_salvar_clicado = False  # Inicializa a variável botao_salvar_clicado como False
    # Variável para rastrear se o mouse está pressionado
    mouse_pressionado = False

    espaco_entre_botoes = 60

    # Cores
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    vermelho = (255, 0, 0)
    cor_texto = (0, 0, 0)

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


    fonte = pygame.font.Font(None, 36)
    texto = fonte.render('Digite o nome do trajeto:', True, cor_texto)
    retangulo_texto = texto.get_rect(center=(largura // 2, 50))

    input_retangulo = pygame.Rect(50, 100, 300, 40)
    cor_input = pygame.Color('lightskyblue3')
    input_texto = ''

    while estado_da_tela == "salvar_percurso_tela":
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
                # Verifique se o clique foi no botão "Voltar"
                elif pygame.Rect(x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar).collidepoint(evento.pos):
                    estado_da_tela = "menu"  # Retorna à tela anterior (menu)
                    voltar_ao_menu()
                # Botão "Salvar" na parte inferior da tela

        tela.fill(branco, area_desenho)
        pygame.draw.rect(tela, cor_input, input_retangulo)
        tela.blit(texto, retangulo_texto)
        
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


        pygame.display.flip()

                # Lógica para salvar o trajeto quando o botão "Salvar" é clicado
        if botao_salvar_clicado:
            # escolher_nome(pontos_desenhados)

            botao_salvar_clicado = False

def salvar_trajeto(trajeto, nome):
    # Certifique-se de que a pasta "trajetos" existe ou a crie
    if not os.path.exists("trajetos"):
        os.mkdir("trajetos")

    # Crie um nome de arquivo único usando UUID
    nome_arquivo = os.path.join("trajetos", f"trajeto"+nome+ ".csv")

    # Salva os pontos do trajeto no arquivo CSV
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["X", "Y"])  # Cabeçalho do CSV
        for ponto in trajeto:
            writer.writerow([ponto[0], ponto[1]])

def escolher_nome(trajeto):
    # root = tk.Tk()
    # root.withdraw()  # Esconde a janela principal

    # # Pede ao usuário para inserir o nome do trajeto
    # nome_trajeto = simpledialog.askstring("Nome do Trajeto", "Digite o nome do trajeto:")
    # salvar_trajeto(trajeto, nome_trajeto)
    print("a")