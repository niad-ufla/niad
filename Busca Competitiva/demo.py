"""
Demonstração básica do jogo de damas.

Este arquivo mostra como usar as classes do jogo de damas
e pode ser usado para testes rápidos.
"""

from jogo_damas import JogoDamas
from exercicios.algoritmos_busca import JogadorAleatorio


def main():
    """
    Função principal para demonstrar o uso do jogo de damas.
    
    Esta função configura uma partida de exemplo e pode ser usada
    para testar as implementações dos algoritmos.
    """
    print("=== DEMONSTRAÇÃO DO JOGO DE DAMAS ===")
    print()
    print("Esta é uma demonstração básica do jogo de damas.")
    print("Para testar os algoritmos de busca, implemente os métodos TODO")
    print("em exercicios/algoritmos_busca.py")
    print()
    
    # Configurar estratégias
    # TODO: Substituir por implementações reais dos algoritmos
    # estrategia_brancas = MiniMax(profundidade_maxima=4)
    # estrategia_pretas = PodaAlfaBeta(profundidade_maxima=4)
    
    estrategia_brancas = JogadorAleatorio()
    estrategia_pretas = JogadorAleatorio()
    
    # Criar e executar o jogo
    jogo = JogoDamas(
        estrategia_brancas=estrategia_brancas,
        estrategia_pretas=estrategia_pretas,
        exibir_tabuleiro=True,
        limite_jogadas=50  # Limite baixo para demonstração
    )
    
    jogo.jogar()
    
    # Salvar resumo da partida
    jogo.salvar_partida("partida_exemplo.json")
    
    print("\n=== FIM DA DEMONSTRAÇÃO ===")
    print("Para implementar os algoritmos de busca, edite o arquivo")
    print("'exercicios/algoritmos_busca.py' e complete os métodos marcados com TODO.")


if __name__ == "__main__":
    main() 