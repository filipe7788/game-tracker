import pygame
import sys
import csv
import os
from criar_percurso import exibir_criar_percurso_tela
from lista_de_percursos import exibir_lista_de_percursos
from reproducao_de_percurso import exibir_trajeto_selecionado_tela
from diagnostico import exibir_diagnostico_tela
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
track_geral = None
# Variável para rastrear a tela de percursos
lista_de_percursos = []  # Lista para armazenar os percursos salvos
percurso_selecionado = None  # Armazena o percurso selecionado

# Variável para armazenar o trajeto selecionado
trajeto_selecionado = []

def voltar_para_lista():
    global estado_da_tela
    estado_da_tela = "percursos"

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

def ir_para_diagnostico(track):
    global estado_da_tela, track_geral
    estado_da_tela = "diagnostico"
    track_geral = track

# Função para exibir a tela de percursos
def exibir_percursos():
    global estado_da_tela, lista_de_percursos, percurso_selecionado
    exibir_lista_de_percursos(tela, estado_da_tela, selecionar_percurso, voltar_ao_menu)

# Função para exibir o trajeto selecionado com um círculo percorrendo-o
def exibir_trajeto_selecionado():
    global tela, estado_da_tela, trajeto_selecionado
    exibir_trajeto_selecionado_tela(estado_da_tela, tela, trajeto_selecionado, voltar_para_lista, ir_para_diagnostico)
    

def exibir_diagnostico(): 
    global tela, estado_da_tela, track_geral
    exibir_diagnostico_tela(estado_da_tela, tela, voltar_ao_menu, track_geral)

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
    elif estado_da_tela == "diagnostico":
        exibir_diagnostico()