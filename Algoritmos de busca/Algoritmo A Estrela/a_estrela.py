import pygame
from queue import PriorityQueue

# Implementação do Algoritmo A* usando um visualizador em Pygame. Há exibição do custo f de cada nó e do caminho encontrado.
# Adaptado de: https://www.youtube.com/watch?v=JtiK0DOeI4A&t=724s&ab_channel=TechWithTim

pygame.font.init()

LARGURA_ALTURA = 800
JANELA = pygame.display.set_mode((LARGURA_ALTURA, LARGURA_ALTURA))
pygame.display.set_caption("Algoritmo A*")

VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
ROXO = (128, 0, 128)
LARANJA = (255, 165, 0)
CINZA = (128, 128, 128)
TURQUESA = (64, 224, 208)

class Noh:
    def __init__(self, linha, coluna, largura_altura, qnt_linhas):
        self.linha = linha
        self.coluna = coluna
        self.x = linha * largura_altura
        self.y = coluna * largura_altura
        self.largura_altura = largura_altura # É um quadrado, então largura e altura são iguais
        self.cor = BRANCO
        self.vizinhos = []
        self.qnt_linhas = qnt_linhas
        self.custo_f = 0

    def consultar_posicao(self):
        return self.linha, self.coluna
    
    def consultar_ja_visitado(self):
        return self.cor == VERMELHO
    
    def consultar_esta_na_fronteira(self):
        return self.cor == VERDE
    
    def consultar_eh_obstaculo(self):
        return self.cor == PRETO
    
    def consultar_eh_inicio(self):
        return self.cor == LARANJA
    
    def consultar_eh_fim(self):
        return self.cor == TURQUESA
    
    def redefinir(self):
        self.cor = BRANCO

    def definir_obstaculo(self):
        self.cor = PRETO

    def definir_inicio(self):
        self.cor = LARANJA

    def definir_fim(self):
        self.cor = TURQUESA

    def definir_esta_na_fronteira(self):
        self.cor = VERDE

    def definir_como_ja_visitado(self):
        self.cor = VERMELHO

    def definir_como_caminho(self):
        self.cor = AZUL

    def desenhar(self, janela, fonte):
        pygame.draw.rect(janela, self.cor, (self.x, self.y, self.largura_altura, self.largura_altura))

        if self.custo_f > 0:
            texto = fonte.render(str(self.custo_f), True, PRETO)
            janela.blit(texto, (self.x + 2, self.y + 2))
        
    def atualizar_vizinhos(self, grid):
        self.vizinhos = []

        # Checa se está dentro dos limites do grid e se é obstáculo. Se tudo estiver certo, adiciona à lista de vizinhos!

        if self.linha < self.qnt_linhas - 1 and not grid[self.linha + 1][self.coluna].consultar_eh_obstaculo(): # Cima
            self.vizinhos.append(grid[self.linha + 1][self.coluna])

        if self.linha > 0 and not grid[self.linha - 1][self.coluna].consultar_eh_obstaculo(): # Baixo
            self.vizinhos.append(grid[self.linha - 1][self.coluna])

        if self.coluna < self.qnt_linhas - 1 and not grid[self.linha][self.coluna + 1].consultar_eh_obstaculo(): # Direita
            self.vizinhos.append(grid[self.linha][self.coluna + 1])

        if self.coluna > 0 and not grid[self.linha][self.coluna - 1].consultar_eh_obstaculo(): # Esquerda
            self.vizinhos.append(grid[self.linha][self.coluna - 1])

    def __lt__(self, outro): 
        return False

def heuristica(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    return abs(x1 - x2) + abs(y1 - y2) # Distância de Manhattan

def algoritmo(desenhar, grid, inicio, fim):
    contador = 0

    fila = PriorityQueue()

    # Usamos o contador para desempatar nós tenham a mesma prioridade
    fila.put((0, contador, inicio)) # Coloca o nó inicial na fila
    veio_de = {} # Dicionário para armazenar o caminho

    custo_g = {noh: float("inf") for linha in grid for noh in linha} # Dicionário para armazenar o custo g de cada nó
    custo_g[inicio] = 0 # O custo g do nó inicial é 0

    custo_f = {noh: float("inf") for linha in grid for noh in linha} # Dicionário para armazenar o custo f de cada nó
    custo_f[inicio] = heuristica(inicio.consultar_posicao(), fim.consultar_posicao()) # O custo f do nó inicial é a heurística
    inicio.custo_f = custo_f[inicio] # Atualiza o custo f do nó inicial

    fila_hash = {inicio} # Conjunto para armazenar os nós que estão na fila

    while not fila.empty():
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()

        noh_atual = fila.get()[2] # Pega o nó atual da fila
        fila_hash.remove(noh_atual) # Remove o nó atual da fila

        if noh_atual == fim: # Se o nó atual for o nó final, encontramos o caminho
            while noh_atual in veio_de: # Enquanto o nó atual estiver no dicionário de veio_de
                reconstruir_caminho(veio_de, noh_atual, desenhar) # Reconstrói o caminho
                fim.definir_fim()
                inicio.definir_inicio()
                return True
            
        for vizinho in noh_atual.vizinhos: # Para cada vizinho do nó atual
            custo_g_temp = custo_g[noh_atual] + 1 # Custo g do vizinho é o custo g do nó atual + 1 (custo de mover para o vizinho)

            if custo_g_temp < custo_g[vizinho]: # Se o custo g do vizinho for menor que o custo g atual (achamos um caminho melhor!)
                veio_de[vizinho] = noh_atual # Atualiza o dicionário de veio_de

                # Atualiza o custo g do vizinho
                custo_g[vizinho] = custo_g_temp
                custo_f[vizinho] = custo_g_temp + heuristica(vizinho.consultar_posicao(), fim.consultar_posicao())
                vizinho.custo_f = custo_f[vizinho]

                if vizinho not in fila_hash: # Se o vizinho não estiver na fila
                    contador += 1 # Incrementa o contador
                    fila.put((custo_f[vizinho], contador, vizinho)) # Adiciona o vizinho na fila
                    fila_hash.add(vizinho) # Adiciona o vizinho no conjunto de nós na fila
                    vizinho.definir_esta_na_fronteira() # Define o vizinho como na fronteira

        desenhar()

        if noh_atual != inicio: # Se o nó atual não for o nó inicial
            noh_atual.definir_como_ja_visitado() # Define o nó atual como já visitado

    return False # Se não encontramos o caminho, retorna False

def reconstruir_caminho(veio_de, atual, desenhar):
    while atual in veio_de: # Enquanto o nó atual estiver no dicionário de veio_de
        atual = veio_de[atual] # Atualiza o nó atual
        atual.definir_como_caminho() # Define o nó atual como parte do caminho
        desenhar() # Desenha o caminho
    return True

def criar_grid(largura_altura, linhas):
    grid = []
    espaco = largura_altura // linhas
    for i in range(linhas):
        grid.append([])
        for j in range(linhas):
            noh = Noh(i, j, espaco, linhas)
            grid[i].append(noh)
    return grid

def desenhar_grid(janela, linhas, largura_altura):
    espaco = largura_altura // linhas
    for i in range(linhas):
        pygame.draw.line(janela, CINZA, (0, i * espaco), (largura_altura, i * espaco)) # Linha horizontal
    for j in range(linhas):
        pygame.draw.line(janela, CINZA, (j * espaco, 0), (j * espaco, largura_altura)) # Linha vertical

def desenhar(janela, grid, linhas, largura_altura, fonte):  # Modificado
    janela.fill(BRANCO)
    for linha in grid:
        for noh in linha:
            noh.desenhar(janela, fonte)  # Passa a fonte
    desenhar_grid(janela, linhas, largura_altura)
    pygame.display.update()

def pegar_pos_clicada(pos, linhas, largura_altura): # Identificando em qual quadrado clicamos
    y, x = pos
    espaco = largura_altura // linhas

    linha = y // espaco
    coluna = x // espaco

    return linha, coluna

def main(janela, largura_altura):
    LINHAS = 50
    grid = criar_grid(largura_altura, LINHAS)
    fonte = pygame.font.Font(None, 12)  # Fonte para o texto

    inicio = None
    fim = None

    rodando = True
    comecou_a_busca = False

    while rodando:
        desenhar(janela, grid, LINHAS, largura_altura, fonte)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if pygame.mouse.get_pressed()[0]: # Clique esquerdo no mouse: define inicio/fim ou obstáculo
                pos = pygame.mouse.get_pos() # Posição do mouse

                linha, coluna = pegar_pos_clicada(pos, LINHAS, largura_altura)
                noh = grid[linha][coluna]

                if not inicio and noh != fim: # Definindo o início
                    inicio = noh
                    inicio.definir_inicio()

                elif not fim and noh != inicio: # Definindo o fim
                    fim = noh
                    fim.definir_fim()

                elif noh != fim and noh != inicio: # Definindo obstáculos
                    noh.definir_obstaculo()

            if pygame.mouse.get_pressed()[1] and inicio and fim: # Clique do meio no mouse: reseta o grid
                inicio = None
                fim = None
                grid = criar_grid(largura_altura, LINHAS)

            elif pygame.mouse.get_pressed()[2]: # Clique direito no mouse: remove inicio/fim já marcado ou obstáculo
                pos = pygame.mouse.get_pos()

                linha, coluna = pegar_pos_clicada(pos, LINHAS, largura_altura)
                noh = grid[linha][coluna]
                noh.redefinir()

                if noh == inicio:
                    inicio = None
                
                elif noh == fim:
                    fim = None

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not comecou_a_busca:
                    for linha in grid:
                        for noh in linha:
                            noh.atualizar_vizinhos(grid)

                    algoritmo(lambda: desenhar(janela, grid, LINHAS, largura_altura, fonte), grid, inicio, fim)


    pygame.quit()

main(JANELA, LARGURA_ALTURA)