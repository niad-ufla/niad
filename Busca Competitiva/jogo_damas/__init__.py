"""
Pacote do Jogo de Damas - Lógica Completa

Este pacote contém toda a implementação funcional do jogo de damas,
incluindo peças, tabuleiro e coordenação de partidas.
"""

from .peca import Peca, CorPeca, TipoPeca
from .tabuleiro import Tabuleiro, Movimento, MovimentoInvalidoError
from .jogo_damas import JogoDamas, StatusJogo

__all__ = [
    'Peca', 'CorPeca', 'TipoPeca',
    'Tabuleiro', 'Movimento', 'MovimentoInvalidoError', 
    'JogoDamas', 'StatusJogo'
] 