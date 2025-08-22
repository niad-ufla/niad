"""
Configurações visuais para o jogo de damas.

Este módulo permite ajustar facilmente o layout e aparência
da interface gráfica sem modificar o código principal.
"""

# ===========================================
# CONFIGURAÇÕES DE LAYOUT
# ===========================================

# Dimensões padrão da janela
LARGURA_PADRAO = 800
ALTURA_PADRAO = 950  # Aumentado para dar mais espaço

# Espaçamentos da interface
ESPACO_INFO_TOPO = 130      # Espaço para informações no topo
ESPACO_BOTOES_BASE = 80     # Espaço para botões na base
MARGEM_LATERAL = 20         # Margem lateral mínima

# ===========================================
# CORES DA INTERFACE
# ===========================================

class Cores:
    """Paleta de cores da interface."""
    
    # Cores do tabuleiro
    CASA_CLARA = (240, 217, 181)      # Bege claro
    CASA_ESCURA = (181, 136, 99)      # Marrom
    
    # Cores das peças
    PECA_BRANCA = (255, 255, 255)     # Branco
    PECA_PRETA = (0, 0, 0)            # Preto
    BORDA_PECA = (100, 100, 100)      # Cinza escuro
    
    # Cores de interação
    DESTAQUE = (255, 255, 0)          # Amarelo (seleção)
    MOVIMENTO_POSSIVEL = (0, 255, 0)  # Verde (movimento normal)
    CAPTURA = (255, 0, 0)             # Vermelho (captura)
    
    # Cores da interface
    FUNDO = (50, 50, 50)              # Cinza escuro
    TEXTO = (255, 255, 255)           # Branco
    TEXTO_DESTAQUE = (255, 255, 100)  # Amarelo suave
    TEXTO_INFO = (200, 200, 255)      # Azul suave
    SEPARADOR = (100, 100, 100)       # Cinza médio
    
    # Cores das mensagens
    FUNDO_MENSAGEM = (40, 40, 40)     # Cinza escuro para caixas
    BORDA_MENSAGEM = (100, 100, 100)  # Cinza médio para bordas

# ===========================================
# CONFIGURAÇÕES DE FONTE
# ===========================================

class Fontes:
    """Tamanhos de fonte da interface."""
    
    TITULO = 30          # Título principal
    GRANDE = 36          # Textos importantes (turno)
    MEDIA = 28           # Textos normais
    PEQUENA = 24         # Textos auxiliares
    BOTOES = 22          # Texto dos botões

# ===========================================
# CONFIGURAÇÕES DE ANIMAÇÃO
# ===========================================

class Animacao:
    """Configurações de animação e temporização."""
    
    FPS = 60                    # Frames por segundo
    TEMPO_MENSAGEM = 2000       # Duração das mensagens (ms)
    DELAY_IA_PADRAO = 1.0      # Delay entre jogadas da IA (segundos)
    DELAY_MOVIMENTO = 500       # Pausa após movimento (ms)
    DELAY_INICIO = 1000        # Pausa no início do jogo (ms)

# ===========================================
# FUNÇÕES DE AJUSTE DINÂMICO
# ===========================================

def calcular_layout(largura: int, altura: int) -> dict:
    """
    Calcula o layout ideal baseado no tamanho da janela.
    
    Args:
        largura (int): Largura da janela
        altura (int): Altura da janela
        
    Returns:
        dict: Configurações de layout calculadas
    """
    # Espaço disponível para o tabuleiro
    espaco_vertical = altura - ESPACO_INFO_TOPO - ESPACO_BOTOES_BASE
    espaco_horizontal = largura - (MARGEM_LATERAL * 2)
    
    # Tamanho do tabuleiro (o menor dos dois espaços)
    tamanho_tabuleiro = min(espaco_vertical, espaco_horizontal)
    tamanho_casa = tamanho_tabuleiro // 8
    
    # Centralização
    offset_x = (largura - tamanho_casa * 8) // 2
    offset_y = ESPACO_INFO_TOPO
    
    return {
        'tamanho_casa': tamanho_casa,
        'offset_x': offset_x,
        'offset_y': offset_y,
        'espaco_info_topo': ESPACO_INFO_TOPO,
        'espaco_botoes_base': ESPACO_BOTOES_BASE
    }

def obter_dimensoes_recomendadas(tamanho_casa_desejado: int = 80) -> tuple:
    """
    Calcula dimensões recomendadas da janela baseado no tamanho desejado das casas.
    
    Args:
        tamanho_casa_desejado (int): Tamanho desejado para cada casa do tabuleiro
        
    Returns:
        tuple: (largura, altura) recomendadas
    """
    tamanho_tabuleiro = tamanho_casa_desejado * 8
    largura = tamanho_tabuleiro + (MARGEM_LATERAL * 2)
    altura = tamanho_tabuleiro + ESPACO_INFO_TOPO + ESPACO_BOTOES_BASE
    
    return largura, altura

# ===========================================
# CONFIGURAÇÕES PRÉ-DEFINIDAS
# ===========================================

class LayoutPresets:
    """Configurações pré-definidas para diferentes resoluções."""
    
    COMPACTO = {
        'largura': 700,
        'altura': 850,
        'tamanho_casa': 70
    }
    
    PADRAO = {
        'largura': 800,
        'altura': 950,
        'tamanho_casa': 80
    }
    
    GRANDE = {
        'largura': 1000,
        'altura': 1150,
        'tamanho_casa': 100
    }
    
    FULLHD = {
        'largura': 1200,
        'altura': 1400,
        'tamanho_casa': 120
    }

def obter_preset(nome: str) -> dict:
    """
    Obtém configuração pré-definida por nome.
    
    Args:
        nome (str): Nome do preset ('compacto', 'padrao', 'grande', 'fullhd')
        
    Returns:
        dict: Configurações do preset
    """
    presets = {
        'compacto': LayoutPresets.COMPACTO,
        'padrao': LayoutPresets.PADRAO,
        'grande': LayoutPresets.GRANDE,
        'fullhd': LayoutPresets.FULLHD
    }
    
    return presets.get(nome.lower(), LayoutPresets.PADRAO) 