"""
Módulo contendo a classe Peca para o jogo de damas.

Este módulo define a estrutura básica de uma peça no jogo de damas,
incluindo sua cor, posição e se é uma dama.
"""

from enum import Enum
from typing import Tuple


class CorPeca(Enum):
    """Enumeração para as cores das peças."""
    BRANCA = "branca"
    PRETA = "preta"


class TipoPeca(Enum):
    """Enumeração para os tipos de peças."""
    NORMAL = "normal"
    DAMA = "dama"


class Peca:
    """
    Classe que representa uma peça no jogo de damas.
    
    Attributes:
        cor (CorPeca): Cor da peça (branca ou preta)
        tipo (TipoPeca): Tipo da peça (normal ou dama)
        posicao (Tuple[int, int]): Posição da peça no tabuleiro (linha, coluna)
    """
    
    def __init__(self, cor: CorPeca, posicao: Tuple[int, int], tipo: TipoPeca = TipoPeca.NORMAL):
        """
        Inicializa uma peça.
        
        Args:
            cor (CorPeca): Cor da peça
            posicao (Tuple[int, int]): Posição inicial da peça (linha, coluna)
            tipo (TipoPeca): Tipo da peça (padrão: normal)
        """
        self.cor = cor
        self.tipo = tipo
        self.posicao = posicao
    
    def promover_a_dama(self) -> None:
        """Promove a peça a dama."""
        self.tipo = TipoPeca.DAMA
    
    def e_dama(self) -> bool:
        """
        Verifica se a peça é uma dama.
        
        Returns:
            bool: True se a peça é uma dama, False caso contrário
        """
        return self.tipo == TipoPeca.DAMA
    
    def mover_para(self, nova_posicao: Tuple[int, int]) -> None:
        """
        Move a peça para uma nova posição.
        
        Args:
            nova_posicao (Tuple[int, int]): Nova posição da peça (linha, coluna)
        """
        self.posicao = nova_posicao
    
    def pode_mover_para_frente(self) -> bool:
        """
        Verifica se a peça pode se mover para frente baseado na sua cor.
        Peças brancas movem para cima (linha menor), pretas para baixo (linha maior).
        
        Returns:
            bool: True se pode mover para frente, False se é uma dama (pode mover em qualquer direção)
        """
        return not self.e_dama()
    
    def direcao_movimento(self) -> int:
        """
        Retorna a direção de movimento da peça.
        
        Returns:
            int: -1 para peças brancas (movem para cima), 1 para peças pretas (movem para baixo)
        """
        if self.e_dama():
            return 0  # Damas podem mover em qualquer direção
        return -1 if self.cor == CorPeca.BRANCA else 1
    
    def copy(self) -> 'Peca':
        """
        Cria uma cópia da peça.
        
        Returns:
            Peca: Nova instância da peça com os mesmos atributos
        """
        return Peca(self.cor, self.posicao, self.tipo)
    
    def __str__(self) -> str:
        """
        Representação em string da peça.
        
        Returns:
            str: Representação da peça (B/P para normal, Br/Pr para dama)
        """
        if self.cor == CorPeca.BRANCA:
            return "Br" if self.e_dama() else "B"
        else:
            return "Pr" if self.e_dama() else "P"
    
    def __repr__(self) -> str:
        """
        Representação formal da peça.
        
        Returns:
            str: Representação detalhada da peça
        """
        return f"Peca({self.cor.value}, {self.posicao}, {self.tipo.value})"
    
    def __eq__(self, other) -> bool:
        """
        Verifica igualdade entre peças.
        
        Args:
            other: Outra peça para comparação
            
        Returns:
            bool: True se as peças são iguais
        """
        if not isinstance(other, Peca):
            return False
        return (self.cor == other.cor and 
                self.tipo == other.tipo and 
                self.posicao == other.posicao) 