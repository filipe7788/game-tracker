import pygame
import sys
import csv
import os
import uuid

# Inicialize o Pygame
pygame.init()

# Configurações da tela
largura, altura = 1920, 1080
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("App de Percursos")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Fonte para o texto
fonte = pygame.font.Font(None, 36)

# Variável para rastrear o estado da tela atual
estado_da_tela = "menu"

# Espaçamento entre os botões
espaco_entre_botoes = 60

# Área de desenho do trajeto
area_desenho = pygame.Rect(0, 0, largura, altura - 100)  # Área acima do botão "Salvar"

# Lista para armazenar os pontos desenhados
pontos_desenhados = []

# Variável para rastrear se o mouse está pressionado
mouse_pressionado = False

# Variável para rastrear a tela de percursos
lista_de_percursos = []  # Lista para armazenar os percursos salvos
percurso_selecionado = None  # Armazena o percurso selecionado

# Variável para armazenar o trajeto selecionado
trajeto_selecionado = []

# Função para exibir o menu
def exibir_menu():
    global estado_da_tela
    while estado_da_tela == "menu":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_percursos.collidepoint(evento.pos):
                    estado_da_tela = "percursos"
                elif botao_criar.collidepoint(evento.pos):
                    estado_da_tela = "criar_percurso"

        # Preencha a tela com branco
        tela.fill(branco)

        # Botões do menu
        botao_percursos = pygame.Rect(760, 400, 400, 100)
        pygame.draw.rect(tela, preto, botao_percursos, border_radius=20)
        texto_botao_percursos = fonte.render("Percursos", True, branco)
        texto_botao_percursos_rect = texto_botao_percursos.get_rect(center=botao_percursos.center)
        tela.blit(texto_botao_percursos, texto_botao_percursos_rect)

        botao_criar = pygame.Rect(760, 550, 400, 100)
        pygame.draw.rect(tela, preto, botao_criar, border_radius=20)
        texto_botao_criar = fonte.render("Criar Percurso", True, branco)
        texto_botao_criar_rect = texto_botao_criar.get_rect(center=botao_criar.center)
        tela.blit(texto_botao_criar, texto_botao_criar_rect)

        # Atualize a tela
        pygame.display.flip()

# Função para exibir a tela de criação de percurso
def exibir_criar_percurso():
    global estado_da_tela, pontos_desenhados, mouse_pressionado

    botao_salvar_clicado = False  # Inicializa a variável botao_salvar_clicado como False

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
                # Verifique se o clique foi no botão "Voltar"
                elif pygame.Rect(x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar).collidepoint(evento.pos):
                    estado_da_tela = "menu"  # Retorna à tela anterior (menu)

        # Desenhar o percurso enquanto o mouse está pressionado
        if mouse_pressionado:
            pos_mouse = pygame.mouse.get_pos()
            if area_desenho.collidepoint(pos_mouse):
                pontos_desenhados.append(pos_mouse)

        # Preencha a área de desenho com branco
        tela.fill(branco, area_desenho)

        # Desenhe os pontos em vermelho
        for ponto in pontos_desenhados:
            pygame.draw.circle(tela, vermelho, ponto, 5)

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

        # Lógica para salvar o trajeto quando o botão "Salvar" é clicado
        if botao_salvar_clicado:
            salvar_trajeto(pontos_desenhados)
            pontos_desenhados = []  # Limpa a lista de pontos após salvar
            botao_salvar_clicado = False

# Função para salvar os dados do trajeto em um arquivo CSV
def salvar_trajeto(trajeto):
    # Certifique-se de que a pasta "trajetos" existe ou a crie
    if not os.path.exists("trajetos"):
        os.mkdir("trajetos")

    # Crie um nome de arquivo único usando UUID
    nome_arquivo = os.path.join("trajetos", f"trajectory_{str(uuid.uuid4())[:8]}.csv")

    # Salva os pontos do trajeto no arquivo CSV
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["X", "Y"])  # Cabeçalho do CSV
        for ponto in trajeto:
            writer.writerow([ponto[0], ponto[1]])

# Função para exibir a tela de percursos
def exibir_percursos():
    global estado_da_tela, lista_de_percursos, percurso_selecionado

    # Verifique e liste os arquivos na pasta "trajetos"
    if not os.path.exists("trajetos"):
        os.mkdir("trajetos")  # Crie a pasta "trajetos" se não existir

    lista_de_percursos = []  # Lista para armazenar os percursos disponíveis
    lista_retangulos_percursos = []  # Lista de retângulos clicáveis dos percursos
    
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

                            break
                    if pygame.Rect(x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar).collidepoint(evento.pos):
                        estado_da_tela = "menu"  # Retorna à tela anterior (menu)

                else:
                    # Se um trajeto já foi selecionado, volte ao menu ao clicar em qualquer lugar
                    estado_da_tela = "menu"
                    percurso_selecionado = None


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


# Função para carregar a lista de percursos salvos
def carregar_percursos():
    percursos = []
    if os.path.exists("trajetos"):
        for arquivo in os.listdir("trajetos"):
            if arquivo.endswith(".csv"):
                percurso = {
                    "arquivo": os.path.join("trajetos", arquivo),
                    "botao": None  # O botão será criado dinamicamente ao exibir a lista
                }
                percursos.append(percurso)
    return percursos

# Função para carregar um trajeto de um arquivo CSV
def carregar_trajeto(arquivo):
    trajeto = []
    with open(arquivo, mode='r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        next(reader)  # Ignorar a linha de cabeçalho
        for linha in reader:
            x, y = map(int, linha)
            trajeto.append((x, y))
    return trajeto

# Função para exibir o trajeto selecionado com um círculo percorrendo-o
# Função para exibir o trajeto selecionado com um círculo percorrendo-o
def exibir_trajeto_selecionado():
    global estado_da_tela, trajeto_selecionado

    arquivo_selecionado = lista_de_percursos[percurso_selecionado]

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

# Loop principal
while True:
    if estado_da_tela == "menu":
        exibir_menu()
    elif estado_da_tela == "criar_percurso":
        exibir_criar_percurso()
    elif estado_da_tela == "percursos":
        exibir_percursos()
    elif estado_da_tela == "trajeto_selecionado":
        exibir_trajeto_selecionado()