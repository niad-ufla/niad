"""
Módulo para implementação dos algoritmos de busca competitiva no jogo de damas.

Este módulo contém a estrutura base e espaços TODO para implementar:
1. MiniMax
2. Poda Alfa-Beta
3. Expect MiniMax (para variantes com elementos estocásticos)

Todos os algoritmos utilizam a função de avaliação implementada na classe Tabuleiro.
"""

from typing import Tuple, Optional, List
from abc import ABC, abstractmethod
import time
import random
import sys
import os

# Adicionar o diretório pai ao path para importar jogo_damas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jogo_damas import Tabuleiro, Movimento, CorPeca


class EstrategiaJogo(ABC):
    """
    Classe abstrata base para estratégias de jogo.
    
    Todas as implementações de algoritmos de busca devem herdar desta classe
    e implementar o método escolher_movimento.
    """
    
    def __init__(self, profundidade_maxima: int = 6):
        """
        Inicializa a estratégia.
        
        Args:
            profundidade_maxima (int): Profundidade máxima de busca
        """
        self.profundidade_maxima = profundidade_maxima
        self.nos_explorados = 0
        self.tempo_execucao = 0.0
        self.melhor_movimento_encontrado = None
    
    @abstractmethod
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """
        Escolhe o melhor movimento para o jogador atual.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            cor_jogador (CorPeca): Cor do jogador que deve jogar
            
        Returns:
            Movimento: Melhor movimento encontrado
        """
        pass
    
    def resetar_estatisticas(self):
        """Reseta as estatísticas de busca."""
        self.nos_explorados = 0
        self.tempo_execucao = 0.0
        self.melhor_movimento_encontrado = None
    
    def obter_estatisticas(self) -> dict:
        """
        Retorna estatísticas da última busca realizada.
        
        Returns:
            dict: Dicionário com estatísticas da busca
        """
        return {
            'nos_explorados': self.nos_explorados,
            'tempo_execucao': self.tempo_execucao,
            'profundidade_maxima': self.profundidade_maxima,
            'melhor_movimento': str(self.melhor_movimento_encontrado) if self.melhor_movimento_encontrado else None
        }


class MiniMax(EstrategiaJogo):
    """
    Implementação do algoritmo MiniMax para jogo de damas.
    
    O algoritmo MiniMax explora a árvore de jogo de forma completa,
    assumindo que ambos os jogadores jogam de forma ótima.
    """
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """
        Escolhe o melhor movimento usando o algoritmo MiniMax.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            cor_jogador (CorPeca): Cor do jogador que deve jogar
            
        Returns:
            Movimento: Melhor movimento encontrado
        """
        self.resetar_estatisticas()
        inicio = time.time()
        
        # TODO: Implementar o algoritmo MiniMax
        # 
        # Passos para implementação:
        # 1. Inicializar o melhor valor como -infinito (para maximizar) ou +infinito (para minimizar)
        # 2. Para cada movimento possível:
        #    a. Fazer uma cópia do tabuleiro
        #    b. Executar o movimento na cópia
        #    c. Chamar minimax_recursivo para avaliar a posição resultante
        #    d. Manter o movimento que resulta no melhor valor
        # 3. Retornar o melhor movimento encontrado
        #
        # Considere:
        # - cor_jogador determina se estamos maximizando (brancas) ou minimizando (pretas)
        # - Use tabuleiro.obter_movimentos_possiveis(cor_jogador) para obter movimentos
        # - Use tabuleiro.copy() para criar cópias do tabuleiro
        # - Use tabuleiro.executar_movimento() para aplicar movimentos
        # - Incremente self.nos_explorados a cada nó visitado
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        # Implementação temporária - retorna movimento aleatório
        # TODO: Substituir pela implementação real do MiniMax
        melhor_movimento = random.choice(movimentos_possiveis)
        self.melhor_movimento_encontrado = melhor_movimento
        
        self.tempo_execucao = time.time() - inicio
        return melhor_movimento
    
    def minimax_recursivo(self, tabuleiro: Tabuleiro, profundidade: int, 
                         maximizando: bool, cor_jogador: CorPeca) -> float:
        """
        Função recursiva do algoritmo MiniMax.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            profundidade (int): Profundidade atual da busca
            maximizando (bool): True se estamos maximizando, False se minimizando
            cor_jogador (CorPeca): Cor do jogador atual
            
        Returns:
            float: Valor da avaliação da posição
        """
        # TODO: Implementar a função recursiva do MiniMax
        #
        # Casos base:
        # 1. Se profundidade == 0 ou jogo terminou: retornar avaliação da posição
        # 2. Se não há movimentos possíveis: retornar avaliação da posição
        #
        # Caso recursivo:
        # 1. Se maximizando:
        #    - Inicializar melhor_valor = -infinito
        #    - Para cada movimento possível:
        #      a. Fazer cópia do tabuleiro e executar movimento
        #      b. Chamar recursivamente com profundidade-1 e maximizando=False
        #      c. Atualizar melhor_valor se o valor retornado for maior
        #    - Retornar melhor_valor
        # 2. Se minimizando: similar, mas inicializar com +infinito e procurar menor valor
        #
        # Lembre-se de:
        # - Incrementar self.nos_explorados
        # - Alternar a cor do jogador a cada nível
        # - Usar tabuleiro.avaliar_posicao() para avaliar posições terminais
        
        self.nos_explorados += 1
        
        # Implementação temporária - retorna avaliação atual
        # TODO: Substituir pela implementação real da recursão
        return tabuleiro.avaliar_posicao()


class PodaAlfaBeta(EstrategiaJogo):
    """
    Implementação do algoritmo MiniMax com Poda Alfa-Beta.
    
    A poda alfa-beta é uma otimização do MiniMax que permite descartar
    ramos da árvore que não podem influenciar o resultado final.
    """
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """
        Escolhe o melhor movimento usando MiniMax com Poda Alfa-Beta.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            cor_jogador (CorPeca): Cor do jogador que deve jogar
            
        Returns:
            Movimento: Melhor movimento encontrado
        """
        self.resetar_estatisticas()
        inicio = time.time()
        
        # TODO: Implementar o algoritmo MiniMax com Poda Alfa-Beta
        #
        # Similar ao MiniMax, mas com parâmetros alfa e beta:
        # - alfa: melhor valor já garantido para o jogador maximizador
        # - beta: melhor valor já garantido para o jogador minimizador
        # - Inicialmente: alfa = -infinito, beta = +infinito
        #
        # A poda ocorre quando alfa >= beta, indicando que o ramo atual
        # não pode produzir um resultado melhor que os já encontrados.
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        # Implementação temporária - retorna movimento aleatório
        # TODO: Substituir pela implementação real da Poda Alfa-Beta
        melhor_movimento = random.choice(movimentos_possiveis)
        self.melhor_movimento_encontrado = melhor_movimento
        
        self.tempo_execucao = time.time() - inicio
        return melhor_movimento
    
    def alfabeta_recursivo(self, tabuleiro: Tabuleiro, profundidade: int,
                          alfa: float, beta: float, maximizando: bool, 
                          cor_jogador: CorPeca) -> float:
        """
        Função recursiva do algoritmo MiniMax com Poda Alfa-Beta.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            profundidade (int): Profundidade atual da busca
            alfa (float): Melhor valor garantido para o maximizador
            beta (float): Melhor valor garantido para o minimizador
            maximizando (bool): True se estamos maximizando
            cor_jogador (CorPeca): Cor do jogador atual
            
        Returns:
            float: Valor da avaliação da posição
        """
        # TODO: Implementar a função recursiva com Poda Alfa-Beta
        #
        # Estrutura similar ao MiniMax, mas com poda:
        # 
        # Casos base: iguais ao MiniMax
        #
        # Caso recursivo para maximização:
        # 1. melhor_valor = -infinito
        # 2. Para cada movimento:
        #    a. Executar movimento em cópia do tabuleiro
        #    b. valor = alfabeta_recursivo(..., maximizando=False, ...)
        #    c. melhor_valor = max(melhor_valor, valor)
        #    d. alfa = max(alfa, melhor_valor)
        #    e. Se beta <= alfa: break (PODA!)
        # 3. Retornar melhor_valor
        #
        # Caso recursivo para minimização: similar, mas com beta
        #
        # A poda acontece quando beta <= alfa, significando que este ramo
        # não pode produzir um resultado melhor que o já encontrado.
        
        self.nos_explorados += 1
        
        # Implementação temporária - retorna avaliação atual
        # TODO: Substituir pela implementação real da recursão com poda
        return tabuleiro.avaliar_posicao()


class ExpectMiniMax(EstrategiaJogo):
    """
    Implementação do algoritmo Expect MiniMax.
    
    O Expect MiniMax é uma extensão do MiniMax para jogos com elementos
    estocásticos (aleatórios). Em nós de "chance", calcula o valor esperado
    das possíveis ações aleatórias.
    
    Para o jogo de damas (que é determinístico), este algoritmo pode ser
    usado para modelar incerteza na avaliação ou para simular um oponente
    que não joga de forma completamente ótima.
    """
    
    def __init__(self, profundidade_maxima: int = 6, probabilidade_erro: float = 0.1):
        """
        Inicializa o Expect MiniMax.
        
        Args:
            profundidade_maxima (int): Profundidade máxima de busca
            probabilidade_erro (float): Probabilidade do oponente cometer erro
        """
        super().__init__(profundidade_maxima)
        self.probabilidade_erro = probabilidade_erro
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """
        Escolhe o melhor movimento usando Expect MiniMax.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            cor_jogador (CorPeca): Cor do jogador que deve jogar
            
        Returns:
            Movimento: Melhor movimento encontrado
        """
        self.resetar_estatisticas()
        inicio = time.time()
        
        # TODO: Implementar o algoritmo Expect MiniMax
        #
        # O Expect MiniMax adiciona nós de "chance" entre os nós de decisão:
        # 1. Nós de maximização: escolhem o movimento que maximiza o valor
        # 2. Nós de minimização: escolhem o movimento que minimiza o valor  
        # 3. Nós de chance: calculam o valor esperado das ações possíveis
        #
        # Para simular incerteza no oponente, você pode:
        # - Com probabilidade (1 - probabilidade_erro): oponente joga ótimo
        # - Com probabilidade (probabilidade_erro): oponente escolhe movimento aleatório
        #
        # O valor de um nó de chance é: Σ(probabilidade_i * valor_i)
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        # Implementação temporária - retorna movimento aleatório
        # TODO: Substituir pela implementação real do Expect MiniMax
        melhor_movimento = random.choice(movimentos_possiveis)
        self.melhor_movimento_encontrado = melhor_movimento
        
        self.tempo_execucao = time.time() - inicio
        return melhor_movimento
    
    def expectminimax_recursivo(self, tabuleiro: Tabuleiro, profundidade: int,
                               no_chance: bool, cor_jogador: CorPeca) -> float:
        """
        Função recursiva do algoritmo Expect MiniMax.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            profundidade (int): Profundidade atual da busca
            no_chance (bool): True se este é um nó de chance
            cor_jogador (CorPeca): Cor do jogador atual
            
        Returns:
            float: Valor esperado da posição
        """
        # TODO: Implementar a função recursiva do Expect MiniMax
        #
        # Estrutura:
        # 1. Casos base: iguais ao MiniMax
        #
        # 2. Se no_chance == True (nó de chance):
        #    - Obter todos os movimentos possíveis
        #    - Calcular valor esperado:
        #      a. movimento_otimo = melhor movimento (minimax simples)
        #      b. movimentos_aleatorios = outros movimentos
        #      c. valor_esperado = (1-prob_erro) * valor(movimento_otimo) + 
        #                         prob_erro * media(valores(movimentos_aleatorios))
        #    - Retornar valor_esperado
        #
        # 3. Se no_chance == False (nó de decisão normal):
        #    - Proceder como MiniMax normal
        #    - Mas chamar recursão com no_chance=True para o próximo nível
        #
        # A alternância no_chance simula a incerteza do oponente
        
        self.nos_explorados += 1
        
        # Implementação temporária - retorna avaliação atual
        # TODO: Substituir pela implementação real da recursão expect
        return tabuleiro.avaliar_posicao()


class JogadorAleatorio(EstrategiaJogo):
    """
    Estratégia que escolhe movimentos aleatórios.
    Útil para testes e como baseline de comparação.
    """
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """
        Escolhe um movimento aleatório dentre os possíveis.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            cor_jogador (CorPeca): Cor do jogador que deve jogar
            
        Returns:
            Movimento: Movimento escolhido aleatoriamente
        """
        self.resetar_estatisticas()
        inicio = time.time()
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        self.nos_explorados = len(movimentos_possiveis)
        melhor_movimento = random.choice(movimentos_possiveis)
        self.melhor_movimento_encontrado = melhor_movimento
        
        self.tempo_execucao = time.time() - inicio
        return melhor_movimento


class JogadorHumano(EstrategiaJogo):
    """
    Estratégia que permite entrada manual de movimentos.
    Útil para jogos humano vs máquina.
    """
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """
        Solicita ao usuário que escolha um movimento.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            cor_jogador (CorPeca): Cor do jogador que deve jogar
            
        Returns:
            Movimento: Movimento escolhido pelo usuário
        """
        self.resetar_estatisticas()
        inicio = time.time()
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        print(f"\nMovimentos possíveis para {cor_jogador.value}:")
        for i, movimento in enumerate(movimentos_possiveis):
            print(f"{i}: {movimento}")
        
        while True:
            try:
                escolha = int(input("Escolha um movimento (número): "))
                if 0 <= escolha < len(movimentos_possiveis):
                    movimento_escolhido = movimentos_possiveis[escolha]
                    break
                else:
                    print("Número inválido! Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido!")
        
        self.nos_explorados = 1
        self.melhor_movimento_encontrado = movimento_escolhido
        self.tempo_execucao = time.time() - inicio
        
        return movimento_escolhido


# TODO: Implementações adicionais que podem ser úteis
#
# 1. MiniMaxComIterativeDeepening:
#    - Executa MiniMax com profundidades crescentes
#    - Útil para controlar tempo de execução
#    - Permite interrupção antecipada mantendo melhor movimento encontrado
#
# 2. MiniMaxComOrdenacao:
#    - Ordena movimentos antes de explorá-los
#    - Melhora eficiência da poda alfa-beta
#    - Movimentos de captura podem ser priorizados
#
# 3. MiniMaxComTabuada:
#    - Mantém cache de posições já avaliadas
#    - Evita recalcular mesmas posições
#    - Especialmente útil em jogos com transposições
#
# 4. MiniMaxComQuiescence:
#    - Estende busca em posições "instáveis" (com capturas)
#    - Evita horizon effect
#    - Melhora qualidade da avaliação
#
# Para implementar qualquer uma dessas extensões, use como base as
# estruturas já definidas acima e modifique conforme necessário. 