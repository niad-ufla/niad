"""
Módulo contendo a classe Tabuleiro para o jogo de damas.

Este módulo implementa a lógica completa do jogo de damas, incluindo
movimento de peças, capturas, promoções e validações.
"""

from typing import List, Optional, Tuple, Dict, Set
from copy import deepcopy
from .peca import Peca, CorPeca


class MovimentoInvalidoError(Exception):
    """Exceção para movimentos inválidos."""
    pass


class Movimento:
    """
    Classe que representa um movimento no jogo de damas.
    
    Attributes:
        origem (Tuple[int, int]): Posição de origem do movimento
        destino (Tuple[int, int]): Posição de destino do movimento
        capturas (List[Tuple[int, int]]): Lista de posições das peças capturadas
        e_captura (bool): Indica se o movimento é uma captura
        promocao (bool): Indica se o movimento resulta em promoção
    """
    
    def __init__(self, origem: Tuple[int, int], destino: Tuple[int, int], 
                 capturas: List[Tuple[int, int]] = None, promocao: bool = False):
        self.origem = origem
        self.destino = destino
        self.capturas = capturas or []
        self.e_captura = len(self.capturas) > 0
        self.promocao = promocao
    
    def __str__(self) -> str:
        captura_str = f" (captura: {self.capturas})" if self.e_captura else ""
        promocao_str = " (promoção)" if self.promocao else ""
        return f"{self.origem} -> {self.destino}{captura_str}{promocao_str}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Movimento):
            return False
        return (self.origem == other.origem and 
                self.destino == other.destino and 
                self.capturas == other.capturas and
                self.promocao == other.promocao)


class Tabuleiro:
    """
    Classe que representa o tabuleiro do jogo de damas.
    
    O tabuleiro é 8x8 com peças inicialmente nas três primeiras fileiras
    de cada lado. Implementa todas as regras do jogo de damas.
    """
    
    TAMANHO = 8
    
    def __init__(self):
        """Inicializa o tabuleiro com a configuração inicial do jogo."""
        self.tabuleiro: List[List[Optional[Peca]]] = [[None for _ in range(self.TAMANHO)] 
                                                      for _ in range(self.TAMANHO)]
        self.turno_atual = CorPeca.BRANCA  # Brancas sempre começam
        self.historico_movimentos: List[Movimento] = []
        self.pecas_capturadas: Dict[CorPeca, List[Peca]] = {
            CorPeca.BRANCA: [],
            CorPeca.PRETA: []
        }
        self._inicializar_pecas()
    
    def _inicializar_pecas(self) -> None:
        """Inicializa as peças na posição inicial do jogo."""
        # Peças pretas nas três primeiras fileiras
        for linha in range(3):
            for coluna in range(self.TAMANHO):
                if (linha + coluna) % 2 == 1:  # Apenas casas escuras
                    self.tabuleiro[linha][coluna] = Peca(CorPeca.PRETA, (linha, coluna))
        
        # Peças brancas nas três últimas fileiras
        for linha in range(5, 8):
            for coluna in range(self.TAMANHO):
                if (linha + coluna) % 2 == 1:  # Apenas casas escuras
                    self.tabuleiro[linha][coluna] = Peca(CorPeca.BRANCA, (linha, coluna))
    
    def get_peca(self, posicao: Tuple[int, int]) -> Optional[Peca]:
        """
        Retorna a peça em uma posição específica.
        
        Args:
            posicao (Tuple[int, int]): Posição no tabuleiro (linha, coluna)
            
        Returns:
            Optional[Peca]: Peça na posição ou None se vazia
        """
        linha, coluna = posicao
        if self._posicao_valida(posicao):
            return self.tabuleiro[linha][coluna]
        return None
    
    def _posicao_valida(self, posicao: Tuple[int, int]) -> bool:
        """
        Verifica se uma posição está dentro dos limites do tabuleiro.
        
        Args:
            posicao (Tuple[int, int]): Posição a verificar
            
        Returns:
            bool: True se a posição é válida
        """
        linha, coluna = posicao
        return 0 <= linha < self.TAMANHO and 0 <= coluna < self.TAMANHO
    
    def _casa_escura(self, posicao: Tuple[int, int]) -> bool:
        """
        Verifica se uma posição é uma casa escura (onde as peças podem estar).
        
        Args:
            posicao (Tuple[int, int]): Posição a verificar
            
        Returns:
            bool: True se é uma casa escura
        """
        linha, coluna = posicao
        return (linha + coluna) % 2 == 1
    
    def obter_movimentos_possiveis(self, cor: CorPeca) -> List[Movimento]:
        """
        Obtém todos os movimentos possíveis para uma cor.
        
        Args:
            cor (CorPeca): Cor das peças para obter movimentos
            
        Returns:
            List[Movimento]: Lista de movimentos possíveis
        """
        movimentos = []
        capturas_obrigatorias = []
        
        # Primeiro, verificar se há capturas obrigatórias
        for linha in range(self.TAMANHO):
            for coluna in range(self.TAMANHO):
                peca = self.tabuleiro[linha][coluna]
                if peca and peca.cor == cor:
                    capturas = self._obter_capturas_peca(peca)
                    capturas_obrigatorias.extend(capturas)
        
        # Se há capturas obrigatórias, retornar apenas elas
        if capturas_obrigatorias:
            return capturas_obrigatorias
        
        # Caso contrário, retornar movimentos normais
        for linha in range(self.TAMANHO):
            for coluna in range(self.TAMANHO):
                peca = self.tabuleiro[linha][coluna]
                if peca and peca.cor == cor:
                    movimentos.extend(self._obter_movimentos_peca(peca))
        
        return movimentos
    
    def _obter_movimentos_peca(self, peca: Peca) -> List[Movimento]:
        """
        Obtém movimentos possíveis para uma peça específica (sem capturas).
        
        Args:
            peca (Peca): Peça para obter movimentos
            
        Returns:
            List[Movimento]: Lista de movimentos possíveis
        """
        movimentos = []
        linha, coluna = peca.posicao
        
        if peca.e_dama():
            # Damas podem mover em todas as 4 direções diagonais
            direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for dir_linha, dir_coluna in direcoes:
                nova_linha, nova_coluna = linha + dir_linha, coluna + dir_coluna
                
                while self._posicao_valida((nova_linha, nova_coluna)):
                    if self.tabuleiro[nova_linha][nova_coluna] is None:
                        movimento = Movimento(
                            peca.posicao, 
                            (nova_linha, nova_coluna),
                            promocao=self._verifica_promocao(peca, (nova_linha, nova_coluna))
                        )
                        movimentos.append(movimento)
                        nova_linha += dir_linha
                        nova_coluna += dir_coluna
                    else:
                        break  # Encontrou uma peça, para aqui
        else:
            # Peças normais movem apenas para frente nas diagonais
            direcao = peca.direcao_movimento()
            movimentos_diagonais = [(direcao, -1), (direcao, 1)]
            
            for dir_linha, dir_coluna in movimentos_diagonais:
                nova_linha, nova_coluna = linha + dir_linha, coluna + dir_coluna
                
                if (self._posicao_valida((nova_linha, nova_coluna)) and 
                    self.tabuleiro[nova_linha][nova_coluna] is None):
                    movimento = Movimento(
                        peca.posicao,
                        (nova_linha, nova_coluna),
                        promocao=self._verifica_promocao(peca, (nova_linha, nova_coluna))
                    )
                    movimentos.append(movimento)
        
        return movimentos
    
    def _obter_capturas_peca(self, peca: Peca) -> List[Movimento]:
        """
        Obtém capturas possíveis para uma peça específica.
        
        Args:
            peca (Peca): Peça para obter capturas
            
        Returns:
            List[Movimento]: Lista de capturas possíveis
        """
        capturas = []
        self._buscar_capturas_recursivo(peca, peca.posicao, [], capturas, set())
        return capturas
    
    def _buscar_capturas_recursivo(self, peca: Peca, posicao_atual: Tuple[int, int], 
                                 capturas_atuais: List[Tuple[int, int]], 
                                 todas_capturas: List[Movimento],
                                 pecas_capturadas: Set[Tuple[int, int]]) -> None:
        """
        Busca capturas de forma recursiva para encontrar capturas múltiplas.
        
        Args:
            peca (Peca): Peça que está capturando
            posicao_atual (Tuple[int, int]): Posição atual da peça
            capturas_atuais (List[Tuple[int, int]]): Capturas já realizadas nesta sequência
            todas_capturas (List[Movimento]): Lista para armazenar todas as capturas encontradas
            pecas_capturadas (Set[Tuple[int, int]]): Conjunto de peças já capturadas nesta sequência
        """
        linha, coluna = posicao_atual
        encontrou_captura = False
        
        if peca.e_dama():
            direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        else:
            direcao = peca.direcao_movimento()
            direcoes = [(direcao, -1), (direcao, 1), (-direcao, -1), (-direcao, 1)]
        
        for dir_linha, dir_coluna in direcoes:
            # Para damas, verificar ao longo de toda a diagonal
            passo = 1
            while True:
                pos_adversario = (linha + dir_linha * passo, coluna + dir_coluna * passo)
                pos_destino = (linha + dir_linha * (passo + 1), coluna + dir_coluna * (passo + 1))
                
                if not (self._posicao_valida(pos_adversario) and self._posicao_valida(pos_destino)):
                    break
                
                peca_adversario = self.tabuleiro[pos_adversario[0]][pos_adversario[1]]
                
                # Se encontrou uma peça adversária que ainda não foi capturada
                if (peca_adversario and 
                    peca_adversario.cor != peca.cor and 
                    pos_adversario not in pecas_capturadas and
                    self.tabuleiro[pos_destino[0]][pos_destino[1]] is None):
                    
                    # Realizar a captura temporariamente
                    novas_capturas = capturas_atuais + [pos_adversario]
                    novas_pecas_capturadas = pecas_capturadas | {pos_adversario}
                    
                    # Continuar buscando capturas a partir da nova posição
                    self._buscar_capturas_recursivo(
                        peca, pos_destino, novas_capturas, todas_capturas, novas_pecas_capturadas
                    )
                    encontrou_captura = True
                    
                    if not peca.e_dama():
                        break  # Peças normais só podem capturar uma por vez em cada direção
                
                elif peca_adversario:
                    break  # Encontrou uma peça, não pode prosseguir
                
                if not peca.e_dama():
                    break  # Peças normais só verificam uma casa à frente
                
                passo += 1
        
        # Se não encontrou mais capturas, adicionar o movimento atual
        if not encontrou_captura and capturas_atuais:
            movimento = Movimento(
                peca.posicao,
                posicao_atual,
                capturas_atuais,
                promocao=self._verifica_promocao(peca, posicao_atual)
            )
            todas_capturas.append(movimento)
    
    def _verifica_promocao(self, peca: Peca, destino: Tuple[int, int]) -> bool:
        """
        Verifica se um movimento resulta em promoção a dama.
        
        Args:
            peca (Peca): Peça que está se movendo
            destino (Tuple[int, int]): Destino do movimento
            
        Returns:
            bool: True se resulta em promoção
        """
        if peca.e_dama():
            return False
        
        linha_destino = destino[0]
        
        if peca.cor == CorPeca.BRANCA and linha_destino == 0:
            return True
        elif peca.cor == CorPeca.PRETA and linha_destino == self.TAMANHO - 1:
            return True
        
        return False
    
    def executar_movimento(self, movimento: Movimento) -> bool:
        """
        Executa um movimento no tabuleiro.
        
        Args:
            movimento (Movimento): Movimento a ser executado
            
        Returns:
            bool: True se o movimento foi executado com sucesso
            
        Raises:
            MovimentoInvalidoError: Se o movimento é inválido
        """
        if not self._movimento_valido(movimento):
            raise MovimentoInvalidoError(f"Movimento inválido: {movimento}")
        
        # Obter a peça a ser movida
        peca = self.get_peca(movimento.origem)
        if not peca:
            raise MovimentoInvalidoError("Não há peça na origem do movimento")
        
        # Remover a peça da posição original
        self.tabuleiro[movimento.origem[0]][movimento.origem[1]] = None
        
        # Executar capturas
        for pos_captura in movimento.capturas:
            peca_capturada = self.get_peca(pos_captura)
            if peca_capturada:
                self.pecas_capturadas[peca_capturada.cor].append(peca_capturada)
                self.tabuleiro[pos_captura[0]][pos_captura[1]] = None
        
        # Mover a peça para o destino
        peca.mover_para(movimento.destino)
        self.tabuleiro[movimento.destino[0]][movimento.destino[1]] = peca
        
        # Verificar promoção
        if movimento.promocao:
            peca.promover_a_dama()
        
        # Adicionar ao histórico e alternar turno
        self.historico_movimentos.append(movimento)
        self.turno_atual = CorPeca.PRETA if self.turno_atual == CorPeca.BRANCA else CorPeca.BRANCA
        
        return True
    
    def _movimento_valido(self, movimento: Movimento) -> bool:
        """
        Verifica se um movimento é válido.
        
        Args:
            movimento (Movimento): Movimento a ser validado
            
        Returns:
            bool: True se o movimento é válido
        """
        # Verificar se as posições são válidas
        if not (self._posicao_valida(movimento.origem) and self._posicao_valida(movimento.destino)):
            return False
        
        # Verificar se a origem tem uma peça do jogador atual
        peca = self.get_peca(movimento.origem)
        if not peca or peca.cor != self.turno_atual:
            return False
        
        # Verificar se o destino está vazio
        if self.get_peca(movimento.destino) is not None:
            return False
        
        # Verificar se o destino é uma casa escura
        if not self._casa_escura(movimento.destino):
            return False
        
        # Verificar se o movimento está na lista de movimentos possíveis
        movimentos_possiveis = self.obter_movimentos_possiveis(self.turno_atual)
        return movimento in movimentos_possiveis
    
    def jogo_terminado(self) -> Tuple[bool, Optional[CorPeca]]:
        """
        Verifica se o jogo terminou e quem venceu.
        
        Returns:
            Tuple[bool, Optional[CorPeca]]: (jogo_terminado, vencedor)
        """
        movimentos_brancas = self.obter_movimentos_possiveis(CorPeca.BRANCA)
        movimentos_pretas = self.obter_movimentos_possiveis(CorPeca.PRETA)
        
        # Verificar se algum jogador não tem movimentos
        if not movimentos_brancas:
            return True, CorPeca.PRETA
        elif not movimentos_pretas:
            return True, CorPeca.BRANCA
        
        # Verificar se algum jogador não tem mais peças
        pecas_brancas = self.contar_pecas(CorPeca.BRANCA)
        pecas_pretas = self.contar_pecas(CorPeca.PRETA)
        
        if pecas_brancas == 0:
            return True, CorPeca.PRETA
        elif pecas_pretas == 0:
            return True, CorPeca.BRANCA
        
        return False, None
    
    def contar_pecas(self, cor: CorPeca) -> int:
        """
        Conta o número de peças de uma cor no tabuleiro.
        
        Args:
            cor (CorPeca): Cor das peças a contar
            
        Returns:
            int: Número de peças da cor especificada
        """
        contador = 0
        for linha in range(self.TAMANHO):
            for coluna in range(self.TAMANHO):
                peca = self.tabuleiro[linha][coluna]
                if peca and peca.cor == cor:
                    contador += 1
        return contador
    
    def obter_todas_pecas(self, cor: CorPeca) -> List[Peca]:
        """
        Obtém todas as peças de uma cor no tabuleiro.
        
        Args:
            cor (CorPeca): Cor das peças
            
        Returns:
            List[Peca]: Lista com todas as peças da cor especificada
        """
        pecas = []
        for linha in range(self.TAMANHO):
            for coluna in range(self.TAMANHO):
                peca = self.tabuleiro[linha][coluna]
                if peca and peca.cor == cor:
                    pecas.append(peca)
        return pecas
    
    def copy(self) -> 'Tabuleiro':
        """
        Cria uma cópia profunda do tabuleiro.
        
        Returns:
            Tabuleiro: Nova instância do tabuleiro
        """
        novo_tabuleiro = Tabuleiro()
        novo_tabuleiro.tabuleiro = deepcopy(self.tabuleiro)
        novo_tabuleiro.turno_atual = self.turno_atual
        novo_tabuleiro.historico_movimentos = deepcopy(self.historico_movimentos)
        novo_tabuleiro.pecas_capturadas = deepcopy(self.pecas_capturadas)
        return novo_tabuleiro
    
    def avaliar_posicao(self) -> float:
        """
        Avalia a posição atual do tabuleiro do ponto de vista das peças brancas.
        Valores positivos favorecem as brancas, negativos favorecem as pretas.
        
        Returns:
            float: Avaliação da posição (-∞ a +∞)
        """
        # Verificar se o jogo terminou
        terminado, vencedor = self.jogo_terminado()
        if terminado:
            if vencedor == CorPeca.BRANCA:
                return float('inf')
            elif vencedor == CorPeca.PRETA:
                return float('-inf')
            else:
                return 0.0  # Empate (caso raro em damas)
        
        pontuacao = 0.0
        
        # Contar peças e damas
        for linha in range(self.TAMANHO):
            for coluna in range(self.TAMANHO):
                peca = self.tabuleiro[linha][coluna]
                if peca:
                    valor_peca = 10 if peca.e_dama() else 3
                    if peca.cor == CorPeca.BRANCA:
                        pontuacao += valor_peca
                        # Bônus por posição (peças mais avançadas valem mais)
                        pontuacao += (7 - linha) * 0.1
                    else:
                        pontuacao -= valor_peca
                        # Bônus por posição (peças mais avançadas valem mais)
                        pontuacao -= linha * 0.1
        
        # Bônus por mobilidade (número de movimentos possíveis)
        movimentos_brancas = len(self.obter_movimentos_possiveis(CorPeca.BRANCA))
        movimentos_pretas = len(self.obter_movimentos_possiveis(CorPeca.PRETA))
        pontuacao += (movimentos_brancas - movimentos_pretas) * 0.1
        
        return pontuacao
    
    def exibir(self) -> str:
        """
        Retorna uma representação visual do tabuleiro.
        
        Returns:
            str: Representação em string do tabuleiro
        """
        linhas = []
        linhas.append("  " + " ".join([str(i) for i in range(self.TAMANHO)]))
        linhas.append("  " + "-" * (self.TAMANHO * 2 - 1))
        
        for linha in range(self.TAMANHO):
            linha_str = f"{linha}|"
            for coluna in range(self.TAMANHO):
                peca = self.tabuleiro[linha][coluna]
                if peca:
                    linha_str += str(peca)
                elif self._casa_escura((linha, coluna)):
                    linha_str += "□"
                else:
                    linha_str += "■"
                
                if coluna < self.TAMANHO - 1:
                    linha_str += " "
            
            linhas.append(linha_str)
        
        linhas.append(f"\nTurno atual: {self.turno_atual.value}")
        linhas.append(f"Peças brancas: {self.contar_pecas(CorPeca.BRANCA)}")
        linhas.append(f"Peças pretas: {self.contar_pecas(CorPeca.PRETA)}")
        
        return "\n".join(linhas) 