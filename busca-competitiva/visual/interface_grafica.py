"""
Interface gráfica para o jogo de damas usando Pygame.

Este módulo implementa a renderização visual do tabuleiro, peças e interface
de usuário para o jogo de damas.
"""

import pygame
import sys
from typing import Tuple, Optional, List
from jogo_damas import Tabuleiro, CorPeca, Movimento


class InterfaceGrafica:
    """
    Classe responsável pela renderização gráfica do jogo de damas.
    
    Utiliza Pygame para desenhar o tabuleiro, peças e interface de usuário,
    permitindo interação através do mouse.
    """
    
    # Cores
    COR_CASA_CLARA = (240, 217, 181)      # Bege claro
    COR_CASA_ESCURA = (181, 136, 99)      # Marrom
    COR_PECA_BRANCA = (255, 255, 255)     # Branco
    COR_PECA_PRETA = (0, 0, 0)            # Preto
    COR_BORDA_PECA = (100, 100, 100)      # Cinza escuro
    COR_DESTAQUE = (255, 255, 0)          # Amarelo
    COR_MOVIMENTO_POSSIVEL = (0, 255, 0)  # Verde
    COR_CAPTURA = (255, 0, 0)             # Vermelho
    COR_FUNDO = (50, 50, 50)              # Cinza escuro
    COR_TEXTO = (255, 255, 255)           # Branco
    
    def __init__(self, largura: int = 800, altura: int = 900):
        """
        Inicializa a interface gráfica.
        
        Args:
            largura (int): Largura da janela
            altura (int): Altura da janela
        """
        pygame.init()
        
        self.largura = largura
        self.altura = altura
        
        # Aumentar espaço para informações e botões
        self.espaco_info_topo = 120  # Espaço para informações no topo
        self.espaco_botoes_base = 60  # Espaço para botões na base
        
        # Calcular tamanho do tabuleiro considerando os espaços reservados
        espaco_disponivel = min(largura, altura - self.espaco_info_topo - self.espaco_botoes_base)
        self.tamanho_casa = espaco_disponivel // 8
        
        # Centralizar tabuleiro
        self.offset_x = (largura - self.tamanho_casa * 8) // 2
        self.offset_y = self.espaco_info_topo
        
        # Configurar janela
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Jogo de Damas - Busca Competitiva")
        
        # Fonte para texto
        self.fonte = pygame.font.Font(None, 36)
        self.fonte_pequena = pygame.font.Font(None, 24)
        self.fonte_media = pygame.font.Font(None, 28)
        
        # Estado da interface
        self.posicao_selecionada: Optional[Tuple[int, int]] = None
        self.movimentos_possiveis: List[Movimento] = []
        
        # Clock para controlar FPS
        self.clock = pygame.time.Clock()
    
    def posicao_para_coordenadas(self, linha: int, coluna: int) -> Tuple[int, int]:
        """
        Converte posição do tabuleiro para coordenadas da tela.
        
        Args:
            linha (int): Linha no tabuleiro (0-7)
            coluna (int): Coluna no tabuleiro (0-7)
            
        Returns:
            Tuple[int, int]: Coordenadas (x, y) na tela
        """
        x = self.offset_x + coluna * self.tamanho_casa
        y = self.offset_y + linha * self.tamanho_casa
        return x, y
    
    def coordenadas_para_posicao(self, x: int, y: int) -> Optional[Tuple[int, int]]:
        """
        Converte coordenadas da tela para posição do tabuleiro.
        
        Args:
            x (int): Coordenada x na tela
            y (int): Coordenada y na tela
            
        Returns:
            Optional[Tuple[int, int]]: Posição (linha, coluna) ou None se inválida
        """
        if (x < self.offset_x or x >= self.offset_x + 8 * self.tamanho_casa or
            y < self.offset_y or y >= self.offset_y + 8 * self.tamanho_casa):
            return None
        
        coluna = (x - self.offset_x) // self.tamanho_casa
        linha = (y - self.offset_y) // self.tamanho_casa
        
        if 0 <= linha < 8 and 0 <= coluna < 8:
            return (linha, coluna)
        return None
    
    def desenhar_tabuleiro(self):
        """Desenha o tabuleiro de damas."""
        for linha in range(8):
            for coluna in range(8):
                x, y = self.posicao_para_coordenadas(linha, coluna)
                
                # Escolher cor da casa
                if (linha + coluna) % 2 == 0:
                    cor = self.COR_CASA_CLARA
                else:
                    cor = self.COR_CASA_ESCURA
                
                # Destacar posição selecionada
                if self.posicao_selecionada == (linha, coluna):
                    cor = self.COR_DESTAQUE
                
                # Desenhar casa
                pygame.draw.rect(self.tela, cor, 
                               (x, y, self.tamanho_casa, self.tamanho_casa))
                
                # Desenhar borda
                pygame.draw.rect(self.tela, (0, 0, 0), 
                               (x, y, self.tamanho_casa, self.tamanho_casa), 1)
    
    def desenhar_movimentos_possiveis(self):
        """Desenha indicadores para movimentos possíveis."""
        for movimento in self.movimentos_possiveis:
            linha, coluna = movimento.destino
            x, y = self.posicao_para_coordenadas(linha, coluna)
            
            # Cor baseada no tipo de movimento
            if movimento.e_captura:
                cor = self.COR_CAPTURA
            else:
                cor = self.COR_MOVIMENTO_POSSIVEL
            
            # Desenhar círculo no centro da casa
            centro_x = x + self.tamanho_casa // 2
            centro_y = y + self.tamanho_casa // 2
            pygame.draw.circle(self.tela, cor, (centro_x, centro_y), 10)
    
    def desenhar_peca(self, linha: int, coluna: int, tabuleiro: Tabuleiro):
        """
        Desenha uma peça na posição especificada.
        
        Args:
            linha (int): Linha da peça
            coluna (int): Coluna da peça
            tabuleiro (Tabuleiro): Tabuleiro atual
        """
        peca = tabuleiro.get_peca((linha, coluna))
        if not peca:
            return
        
        x, y = self.posicao_para_coordenadas(linha, coluna)
        centro_x = x + self.tamanho_casa // 2
        centro_y = y + self.tamanho_casa // 2
        raio = self.tamanho_casa // 3
        
        # Cor da peça
        if peca.cor == CorPeca.BRANCA:
            cor_peca = self.COR_PECA_BRANCA
        else:
            cor_peca = self.COR_PECA_PRETA
        
        # Desenhar peça
        pygame.draw.circle(self.tela, cor_peca, (centro_x, centro_y), raio)
        pygame.draw.circle(self.tela, self.COR_BORDA_PECA, (centro_x, centro_y), raio, 3)
        
        # Indicar dama com círculo menor interno
        if peca.e_dama():
            pygame.draw.circle(self.tela, self.COR_BORDA_PECA, 
                             (centro_x, centro_y), raio // 2, 2)
    
    def desenhar_pecas(self, tabuleiro: Tabuleiro):
        """
        Desenha todas as peças do tabuleiro.
        
        Args:
            tabuleiro (Tabuleiro): Tabuleiro atual
        """
        for linha in range(8):
            for coluna in range(8):
                self.desenhar_peca(linha, coluna, tabuleiro)
    
    def desenhar_informacoes(self, tabuleiro: Tabuleiro, info_adicional: str = ""):
        """
        Desenha informações do jogo na parte superior.
        
        Args:
            tabuleiro (Tabuleiro): Tabuleiro atual
            info_adicional (str): Informação adicional para exibir
        """
        # Limpar área de informações
        pygame.draw.rect(self.tela, self.COR_FUNDO, (0, 0, self.largura, self.espaco_info_topo))
        
        # Linha 1: Título do jogo
        titulo = "JOGO DE DAMAS - BUSCA COMPETITIVA"
        titulo_surface = self.fonte_media.render(titulo, True, self.COR_TEXTO)
        titulo_x = (self.largura - titulo_surface.get_width()) // 2
        self.tela.blit(titulo_surface, (titulo_x, 10))
        
        # Linha 2: Turno atual (destaque visual)
        turno_texto = f"Turno: {tabuleiro.turno_atual.value.upper()}"
        if tabuleiro.turno_atual.value == "branca":
            cor_turno = self.COR_PECA_BRANCA
        else:
            cor_turno = (200, 200, 200)  # Cinza claro para pretas
        
        turno_surface = self.fonte.render(turno_texto, True, cor_turno)
        self.tela.blit(turno_surface, (10, 40))
        
        # Linha 2: Contagem de peças (direita)
        brancas = tabuleiro.contar_pecas(CorPeca.BRANCA)
        pretas = tabuleiro.contar_pecas(CorPeca.PRETA)
        pecas_texto = f"Peças - Brancas: {brancas} | Pretas: {pretas}"
        pecas_surface = self.fonte_pequena.render(pecas_texto, True, self.COR_TEXTO)
        pecas_x = self.largura - pecas_surface.get_width() - 10
        self.tela.blit(pecas_surface, (pecas_x, 45))
        
        # Linha 3: Informação adicional (centralizada)
        if info_adicional:
            # Quebrar texto se for muito longo
            max_largura = self.largura - 20
            palavras = info_adicional.split()
            linhas = []
            linha_atual = ""
            
            for palavra in palavras:
                teste_linha = linha_atual + (" " if linha_atual else "") + palavra
                teste_surface = self.fonte_pequena.render(teste_linha, True, self.COR_TEXTO)
                
                if teste_surface.get_width() <= max_largura:
                    linha_atual = teste_linha
                else:
                    if linha_atual:
                        linhas.append(linha_atual)
                    linha_atual = palavra
            
            if linha_atual:
                linhas.append(linha_atual)
            
            # Desenhar linhas centralizadas
            y_start = 75
            for i, linha in enumerate(linhas[:2]):  # Máximo 2 linhas
                info_surface = self.fonte_pequena.render(linha, True, (255, 255, 100))  # Amarelo suave
                info_x = (self.largura - info_surface.get_width()) // 2
                self.tela.blit(info_surface, (info_x, y_start + i * 20))
        
        # Linha de separação
        pygame.draw.line(self.tela, (100, 100, 100), 
                        (10, self.espaco_info_topo - 5), 
                        (self.largura - 10, self.espaco_info_topo - 5), 2)
    
    def desenhar_botoes(self):
        """Desenha botões de controle na parte inferior."""
        # Área dos botões
        y_inicio_botoes = self.altura - self.espaco_botoes_base
        
        # Limpar área dos botões
        pygame.draw.rect(self.tela, self.COR_FUNDO, 
                        (0, y_inicio_botoes, self.largura, self.espaco_botoes_base))
        
        # Linha de separação
        pygame.draw.line(self.tela, (100, 100, 100), 
                        (10, y_inicio_botoes + 5), 
                        (self.largura - 10, y_inicio_botoes + 5), 2)
        
        y_botoes = y_inicio_botoes + 15
        
        # Lista de botões com suas descrições
        botoes = [
            ("R", "Reiniciar"),
            ("H", "Ajuda"),
            ("ESC", "Sair")
        ]
        
        # Calcular espaçamento
        espaco_total = self.largura - 40  # Margens
        espaco_por_botao = espaco_total // len(botoes)
        
        for i, (tecla, descricao) in enumerate(botoes):
            x_base = 20 + i * espaco_por_botao
            
            # Desenhar tecla em destaque
            tecla_surface = self.fonte_pequena.render(f"[{tecla}]", True, (255, 255, 100))
            self.tela.blit(tecla_surface, (x_base, y_botoes))
            
            # Desenhar descrição
            desc_surface = self.fonte_pequena.render(descricao, True, self.COR_TEXTO)
            desc_x = x_base + tecla_surface.get_width() + 5
            self.tela.blit(desc_surface, (desc_x, y_botoes))
            
        # Adicionar informação de controles do mouse no centro
        mouse_info = "🖱️ Clique nas peças para jogar"
        mouse_surface = self.fonte_pequena.render(mouse_info, True, (200, 200, 255))
        mouse_x = (self.largura - mouse_surface.get_width()) // 2
        self.tela.blit(mouse_surface, (mouse_x, y_botoes + 25))
    
    def renderizar(self, tabuleiro: Tabuleiro, info_adicional: str = ""):
        """
        Renderiza o estado completo do jogo.
        
        Args:
            tabuleiro (Tabuleiro): Tabuleiro atual
            info_adicional (str): Informação adicional para exibir
        """
        # Limpar tela
        self.tela.fill(self.COR_FUNDO)
        
        # Desenhar componentes
        self.desenhar_informacoes(tabuleiro, info_adicional)
        self.desenhar_tabuleiro()
        self.desenhar_movimentos_possiveis()
        self.desenhar_pecas(tabuleiro)
        self.desenhar_botoes()
        
        # Atualizar tela
        pygame.display.flip()
        self.clock.tick(60)  # 60 FPS
    
    def processar_eventos(self) -> List[str]:
        """
        Processa eventos do Pygame.
        
        Returns:
            List[str]: Lista de eventos processados
        """
        eventos = []
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                eventos.append("quit")
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Clique esquerdo
                    posicao = self.coordenadas_para_posicao(evento.pos[0], evento.pos[1])
                    if posicao:
                        eventos.append(f"click:{posicao[0]}:{posicao[1]}")
            
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    eventos.append("reset")
                elif evento.key == pygame.K_h:
                    eventos.append("help")
                elif evento.key == pygame.K_ESCAPE:
                    eventos.append("quit")
        
        return eventos
    
    def selecionar_posicao(self, posicao: Tuple[int, int], tabuleiro: Tabuleiro):
        """
        Seleciona uma posição no tabuleiro.
        
        Args:
            posicao (Tuple[int, int]): Posição a selecionar
            tabuleiro (Tabuleiro): Tabuleiro atual
        """
        self.posicao_selecionada = posicao
        
        # Obter movimentos possíveis para a peça selecionada
        peca = tabuleiro.get_peca(posicao)
        if peca and peca.cor == tabuleiro.turno_atual:
            todos_movimentos = tabuleiro.obter_movimentos_possiveis(tabuleiro.turno_atual)
            self.movimentos_possiveis = [mov for mov in todos_movimentos 
                                       if mov.origem == posicao]
        else:
            self.movimentos_possiveis = []
    
    def desselecionar(self):
        """Remove seleção atual."""
        self.posicao_selecionada = None
        self.movimentos_possiveis = []
    
    def encontrar_movimento(self, origem: Tuple[int, int], 
                          destino: Tuple[int, int], 
                          tabuleiro: Tabuleiro) -> Optional[Movimento]:
        """
        Encontra um movimento específico na lista de movimentos possíveis.
        
        Args:
            origem (Tuple[int, int]): Posição de origem
            destino (Tuple[int, int]): Posição de destino
            tabuleiro (Tabuleiro): Tabuleiro atual
            
        Returns:
            Optional[Movimento]: Movimento encontrado ou None
        """
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(tabuleiro.turno_atual)
        
        for movimento in movimentos_possiveis:
            if movimento.origem == origem and movimento.destino == destino:
                return movimento
        
        return None
    
    def mostrar_mensagem(self, mensagem: str, cor: Tuple[int, int, int] = None):
        """
        Mostra uma mensagem temporária na tela.
        
        Args:
            mensagem (str): Mensagem a exibir
            cor (Tuple[int, int, int]): Cor do texto (padrão: branco)
        """
        if cor is None:
            cor = self.COR_TEXTO
        
        # Dividir mensagem em linhas
        linhas = mensagem.split('\n')
        
        # Criar superfícies para cada linha
        superficies_texto = []
        altura_total = 0
        largura_maxima = 0
        
        for linha in linhas:
            if linha.strip():  # Pular linhas vazias
                superficie = self.fonte.render(linha.strip(), True, cor)
                superficies_texto.append(superficie)
                altura_total += superficie.get_height() + 10
                largura_maxima = max(largura_maxima, superficie.get_width())
        
        # Criar fundo da mensagem
        padding = 30
        fundo_largura = largura_maxima + padding * 2
        fundo_altura = altura_total + padding * 2
        
        # Desenhar fundo semi-transparente para toda a tela
        overlay = pygame.Surface((self.largura, self.altura))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.tela.blit(overlay, (0, 0))
        
        # Desenhar caixa da mensagem
        fundo_x = (self.largura - fundo_largura) // 2
        fundo_y = (self.altura - fundo_altura) // 2
        
        # Fundo da caixa
        caixa_fundo = pygame.Surface((fundo_largura, fundo_altura))
        caixa_fundo.fill((40, 40, 40))
        
        # Borda da caixa
        pygame.draw.rect(caixa_fundo, (100, 100, 100), 
                        (0, 0, fundo_largura, fundo_altura), 3)
        
        self.tela.blit(caixa_fundo, (fundo_x, fundo_y))
        
        # Desenhar texto centralizado
        y_atual = fundo_y + padding
        for superficie in superficies_texto:
            x_texto = fundo_x + (fundo_largura - superficie.get_width()) // 2
            self.tela.blit(superficie, (x_texto, y_atual))
            y_atual += superficie.get_height() + 10
        
        pygame.display.flip()
        
        # Aguardar um tempo ou clique
        pygame.time.wait(2000)
    
    def fechar(self):
        """Fecha a interface gráfica."""
        pygame.quit() 