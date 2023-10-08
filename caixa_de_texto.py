import pygame

class CaixaDeTexto:
    def __init__(self, x, y, largura, altura, fonte, cor_texto, cor_borda):
        self.retangulo = pygame.Rect(x, y, largura, altura)
        self.texto = ""
        self.fonte = fonte
        self.cor_texto = cor_texto
        self.cor_borda = cor_borda

    def renderizar(self, tela):
        pygame.draw.rect(tela, self.cor_borda, self.retangulo, 2)
        texto_renderizado = self.fonte.render(self.texto, True, self.cor_texto)

        # Calcula a posição para alinhar à direita
        pos_x = self.retangulo.x + self.retangulo.width - texto_renderizado.get_width() - 5
        pos_y = self.retangulo.y + 5

        tela.blit(texto_renderizado, (pos_x, pos_y))

    def update(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o mouse está sobre a caixa de texto
            if self.retangulo.collidepoint(evento.pos):
                self.ativa = True
            else:
                self.ativa = False
        elif evento.type == pygame.KEYDOWN and self.ativa:
            if evento.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            elif evento.key == pygame.K_RETURN:
                self.ativa = False  # Desativa a caixa ao pressionar Enter
            elif evento.key in range(32, 127):  # Caracteres imprimíveis ASCII
                if len(self.texto) < 45:
                    self.texto += evento.unicode