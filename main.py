import pygame
import sys
import csv
import os
from criar_percurso import exibir_criar_percurso_tela
from lista_de_percursos import exibir_lista_de_percursos
from reproducao_de_percurso import exibir_trajeto_selecionado_tela
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

def voltar_ao_menu():
    global estado_da_tela
    estado_da_tela = "menu"

# Função para exibir a tela de criação de percurso
def exibir_criar_percurso():
    global tela, estado_da_tela
    exibir_criar_percurso_tela(tela, estado_da_tela, voltar_ao_menu)


def selecionar_percurso(trajeto_selecionado_lista):
    global trajeto_selecionado, estado_da_tela
    estado_da_tela = "trajeto_selecionado"
    trajeto_selecionado = trajeto_selecionado_lista

# Função para exibir a tela de percursos
def exibir_percursos():
    global estado_da_tela, lista_de_percursos, percurso_selecionado
    exibir_lista_de_percursos(tela, estado_da_tela, selecionar_percurso, voltar_ao_menu)

# Função para exibir o trajeto selecionado com um círculo percorrendo-o
def exibir_trajeto_selecionado():
    global estado_da_tela, trajeto_selecionado
    exibir_trajeto_selecionado_tela(estado_da_tela, tela, trajeto_selecionado)
    
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