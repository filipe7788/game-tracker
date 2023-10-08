import time
import sys
import pygame

class TelaExibirPercurso:
    def __init__(self, trajeto):
        pygame.init()

        self.largura, self.altura = 1920, 1080
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Exibir Percurso Selecionado')

        self.cor_fundo = (255, 255, 255)
        self.cor_bola = (255, 0, 0)

        self.trajeto = trajeto
        
        self.posicao_atual = (self.trajeto["trajeto"][0][0], self.trajeto["trajeto"][0][1])
        self.tempo_inicial = pygame.time.get_ticks()
        self.tempo_ultimo_ponto = 0
        self.parada = False
        self.em_pausa = True
        self.indice_ponto_atual = 0  # Índice do ponto atual na lista de pontos
        self.fonte = pygame.font.Font(None, 36)
                # Posicionamento dos botões
        self.botao_play_rect = pygame.Rect(self.largura // 2 - 120, self.altura - 100, 100, 40)
        self.botao_diagnostico_rect = pygame.Rect(self.largura // 2 + 20, self.altura - 100, 150, 40)
        self.cor_botao = pygame.Color('dodgerblue2')

        self.posicao_atual = self.trajeto["trajeto"][0]
        self.posicao_destino = self.trajeto["trajeto"][1]
        self.em_movimento = False
        # "nome_trajeto": nome_trajeto,
        # "tempo medio": tempo1,
        # "tempo stay": tempo2,
        # "trajeto": trajeto
    def desenhar_trajeto(self):
        # Desenhar pontos
        for i in range(len(self.trajeto["trajeto"])):
            centerX = self.trajeto["trajeto"][i][0]
            centerY = self.trajeto["trajeto"][i][1]
            pygame.draw.circle(self.tela, self.cor_bola, (centerX, centerY), 5)

        # # Desenhar linhas entre os pontos
        for i in range(len(self.trajeto["trajeto"]) - 1):
            ponto_inicial = (int(self.trajeto["trajeto"][i][0]), int(self.trajeto["trajeto"][i][1]))


            ponto_final = (int(self.trajeto["trajeto"][i + 1][0]), int(self.trajeto["trajeto"][i + 1][1]))
            pygame.draw.line(self.tela, self.cor_bola, ponto_inicial, ponto_final, 2)
    
    def desenhar_bola(self):
        pygame.draw.circle(self.tela, self.cor_bola, (int(self.posicao_atual[0]), int(self.posicao_atual[1])), 10)

    def desenhar_botao_play(self):
        pygame.draw.rect(self.tela, self.cor_botao, self.botao_play_rect)
        pygame.draw.rect(self.tela, (0, 0, 0), self.botao_play_rect, 2)
        texto_play = self.fonte.render("Play", True, (0, 0, 0))
        retangulo_play_pos = texto_play.get_rect(center=self.botao_play_rect.center)
        self.tela.blit(texto_play, retangulo_play_pos)

    def desenhar_botao_diagnostico(self):
        pygame.draw.rect(self.tela, self.cor_botao, self.botao_diagnostico_rect)
        pygame.draw.rect(self.tela, (0, 0, 0), self.botao_diagnostico_rect, 2)
        texto_diagnostico = self.fonte.render("Diagnóstico", True, (0, 0, 0))
        retangulo_diagnostico_pos = texto_diagnostico.get_rect(center=self.botao_diagnostico_rect.center)
        self.tela.blit(texto_diagnostico, retangulo_diagnostico_pos)
    
    def atualizar_posicao_bola(self):
        tempo_medio = int(self.trajeto["tempo_medio"])

        deslocamento = (
            (self.posicao_destino[0] - self.posicao_atual[0]),
            (self.posicao_destino[1] - self.posicao_atual[1])
        )

        # Calcular a distância entre os pontos
        distancia = (deslocamento[0] ** 2 + deslocamento[1] ** 2) ** 0.5

        # Normalizar a direção para obter um vetor unitário
        direcao = (deslocamento[0] / distancia, deslocamento[1] / distancia)

        # Calcular o deslocamento com base na velocidade
        deslocamento_velocidade = (direcao[0] * tempo_medio, direcao[1] * tempo_medio)

        # Atualizar a posição da bola
        self.posicao_atual = (
            self.posicao_atual[0] + deslocamento_velocidade[0],
            self.posicao_atual[1] + deslocamento_velocidade[1]
        )

        # Verificar se a bola atingiu o ponto de destino
        if distancia <= tempo_medio / 60:  # Ajuste conforme necessário
            self.em_movimento = False
     

    def verificar_clique_botao_play(self, pos_mouse):
        # Verificar se o clique do mouse está sobre o botão de play (ajuste as coordenadas conforme necessário)
        return 150 <= pos_mouse[0] <= 250 and 500 <= pos_mouse[1] <= 550

    def atualiza(self):

        if self.em_movimento is True:
            for i in range(0, len(self.trajeto["trajeto"])-1):
                # pygame.time.delay(int((self.trajeto["tempo_stay"]))*1000)
                ponto_atual = self.trajeto["trajeto"][i]
                proximo_ponto = self.trajeto["trajeto"][i+1]
                self.posicao_atual = ponto_atual
                self.posicao_destino = proximo_ponto

                self.atualizar_posicao_bola()
            self.em_movimento = False

    def executar(self):
        clock = pygame.time.Clock()

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.em_pausa:
                        self.em_pausa = False
                        self.tempo_pausa = pygame.time.get_ticks() - self.tempo_inicial
                    elif self.botao_play_rect.collidepoint(evento.pos):
                        self.em_movimento = True
                        

            self.tela.fill(self.cor_fundo)

            self.desenhar_trajeto()
            self.desenhar_bola()
            self.desenhar_botao_play()
            self.desenhar_botao_diagnostico()
            self.atualiza()

            pygame.display.flip()
            clock.tick(60)
