import pygame
import os, csv, sys
from caixa_de_texto import CaixaDeTexto
import pickle

def salvar_percurso_tela(tela, estado_da_tela, trajeto_selecionado, voltar_ao_menu):


    largura, altura = 1920, 1080
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Caixa de Diálogo')

    cor_fundo = (255, 255, 255)
    cor_texto = (0, 0, 0)
    cor_borda = (0, 0, 0)

    fonte = pygame.font.Font(None, 36)

    textos = ["Digite o nome do trajeto:", "Digite a quantidade de tempo que o indicador deverá se mover entre 2 pontos:", "Digite a quantidade de tempo que o indicador deverá passar em cada ponto:"]
    caixas_de_texto = [CaixaDeTexto(largura // 2 - 300, altura // 2 - 36 - i * 200, 600, 72, fonte, cor_texto, cor_borda) for i in range(3)]
    ativo = 0  # Começa com o primeiro campo ativo
    
    botao_confirmar = pygame.Rect(largura // 2 - 100, altura - 200, 200, 80)
    cor_botao = pygame.Color('dodgerblue2')


    while estado_da_tela == "salvar_percurso_tela":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_confirmar.collidepoint(evento.pos) and ativo < len(textos):
                    if ativo == 0:
                        nome_trajeto = caixas_de_texto[ativo].texto
                    elif ativo == 1:
                        tempo1 = caixas_de_texto[ativo].texto
                    elif ativo == 2:
                        tempo2 = caixas_de_texto[ativo].texto
                        salvar_trajeto(nome_trajeto, tempo1, tempo2, trajeto_selecionado)
                    ativo += 1
                    if ativo == len(textos):
                        estado_da_tela = "menu"  # Retorna à tela anterior (menu)
                        voltar_ao_menu()
            tela.fill(cor_fundo)


            for i, (texto, caixa) in enumerate(zip(textos, caixas_de_texto)):
                retangulo_texto = fonte.render(texto, True, cor_texto)
                # Calcula a posição para alinhar à direita
                pos_x = largura // 2 - retangulo_texto.get_width() // 2
                pos_y = altura // 2 - 90 - i * 200
                tela.blit(retangulo_texto, (pos_x, pos_y))


                caixa.update(evento)
                caixa.renderizar(tela)

            pygame.draw.rect(tela, cor_botao, botao_confirmar)
            pygame.draw.rect(tela, cor_texto, botao_confirmar, 2)

            texto_botao = fonte.render("Confirmar", True, cor_texto)
            retangulo_botao_pos = texto_botao.get_rect(center=botao_confirmar.center)
            tela.blit(texto_botao, retangulo_botao_pos)

            pygame.display.flip()


def salvar_trajeto(nome_trajeto, tempo1, tempo2, trajeto):
    result = [] 
    for i in trajeto: 
        if i not in result: 
            result.append(i) 
            
    objeto_trajeto = {
        "nome_trajeto": nome_trajeto,
        "tempo_medio": tempo1,
        "tempo_stay": tempo2,
        "trajeto": result
    }

    pasta_trajetos = "trajetos"
    if not os.path.exists(pasta_trajetos):
        os.makedirs(pasta_trajetos)

    caminho_arquivo = os.path.join(pasta_trajetos, f"{nome_trajeto}.pkl")
    with open(caminho_arquivo, "wb") as arquivo:
        pickle.dump(objeto_trajeto, arquivo)
