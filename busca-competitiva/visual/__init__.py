"""
Pacote Visual - Interface Gráfica para Jogo de Damas

Este pacote contém a implementação da interface gráfica usando Pygame,
permitindo jogar e visualizar os algoritmos de forma intuitiva.
"""

from .interface_grafica import InterfaceGrafica
from .jogo_visual import JogoVisual
from .configuracao_visual import Cores, Fontes, Animacao, LayoutPresets, obter_preset

__all__ = [
    'InterfaceGrafica', 
    'JogoVisual',
    'Cores',
    'Fontes', 
    'Animacao',
    'LayoutPresets',
    'obter_preset'
] 