"""
ARQUIVO DE SOLUÇÃO - IMPLEMENTAÇÕES COMPLETAS DOS ALGORITMOS

Este arquivo contém as implementações completas dos algoritmos de busca
competitiva para o jogo de damas. Use este arquivo apenas para comparação
após tentar implementar os algoritmos por conta própria.

⚠️ IMPORTANTE: Este arquivo é apenas para referência e comparação.
   Tente implementar os algoritmos nos espaços TODO primeiro!

Algoritmos implementados:
1. MiniMax
2. Poda Alfa-Beta  
3. Expect MiniMax
4. Extensões avançadas
"""

from typing import Tuple, Optional, List
import time
import random
from jogo_damas import Tabuleiro, Movimento, CorPeca
from exercicios import EstrategiaJogo, JogadorAleatorio


class MiniMaxCompleto(EstrategiaJogo):
    """
    Implementação completa do algoritmo MiniMax.
    
    Esta é a solução de referência para comparação.
    Tente implementar primeiro nos espaços TODO!
    """
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """Implementação completa do MiniMax."""
        self.resetar_estatisticas()
        inicio = time.time()
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        melhor_movimento = None
        maximizando = (cor_jogador == CorPeca.BRANCA)
        
        if maximizando:
            melhor_valor = float('-inf')
            for movimento in movimentos_possiveis:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.minimax_recursivo(
                    tabuleiro_copia, 
                    self.profundidade_maxima - 1, 
                    False, 
                    CorPeca.PRETA
                )
                
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = movimento
        else:
            melhor_valor = float('inf')
            for movimento in movimentos_possiveis:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.minimax_recursivo(
                    tabuleiro_copia, 
                    self.profundidade_maxima - 1, 
                    True, 
                    CorPeca.BRANCA
                )
                
                if valor < melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = movimento
        
        self.melhor_movimento_encontrado = melhor_movimento
        self.tempo_execucao = time.time() - inicio
        return melhor_movimento
    
    def minimax_recursivo(self, tabuleiro: Tabuleiro, profundidade: int, 
                         maximizando: bool, cor_jogador: CorPeca) -> float:
        """Implementação completa da recursão MiniMax."""
        self.nos_explorados += 1
        
        # Casos base
        terminado, vencedor = tabuleiro.jogo_terminado()
        if terminado or profundidade == 0:
            return tabuleiro.avaliar_posicao()
        
        movimentos = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        if not movimentos:
            return tabuleiro.avaliar_posicao()
        
        # Recursão
        if maximizando:
            melhor_valor = float('-inf')
            for movimento in movimentos:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.minimax_recursivo(
                    tabuleiro_copia, 
                    profundidade - 1, 
                    False, 
                    CorPeca.PRETA
                )
                melhor_valor = max(melhor_valor, valor)
            
            return melhor_valor
        else:
            melhor_valor = float('inf')
            for movimento in movimentos:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.minimax_recursivo(
                    tabuleiro_copia, 
                    profundidade - 1, 
                    True, 
                    CorPeca.BRANCA
                )
                melhor_valor = min(melhor_valor, valor)
            
            return melhor_valor


class PodaAlfaBetaCompleta(EstrategiaJogo):
    """
    Implementação completa do algoritmo MiniMax com Poda Alfa-Beta.
    
    Esta é a solução de referência para comparação.
    Tente implementar primeiro nos espaços TODO!
    """
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """Implementação completa da Poda Alfa-Beta."""
        self.resetar_estatisticas()
        inicio = time.time()
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        melhor_movimento = None
        maximizando = (cor_jogador == CorPeca.BRANCA)
        alfa = float('-inf')
        beta = float('inf')
        
        if maximizando:
            melhor_valor = float('-inf')
            for movimento in movimentos_possiveis:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.alfabeta_recursivo(
                    tabuleiro_copia, 
                    self.profundidade_maxima - 1, 
                    alfa, beta, False, 
                    CorPeca.PRETA
                )
                
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = movimento
                
                alfa = max(alfa, melhor_valor)
                if beta <= alfa:
                    break  # Poda
        else:
            melhor_valor = float('inf')
            for movimento in movimentos_possiveis:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.alfabeta_recursivo(
                    tabuleiro_copia, 
                    self.profundidade_maxima - 1, 
                    alfa, beta, True, 
                    CorPeca.BRANCA
                )
                
                if valor < melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = movimento
                
                beta = min(beta, melhor_valor)
                if beta <= alfa:
                    break  # Poda
        
        self.melhor_movimento_encontrado = melhor_movimento
        self.tempo_execucao = time.time() - inicio
        return melhor_movimento
    
    def alfabeta_recursivo(self, tabuleiro: Tabuleiro, profundidade: int,
                          alfa: float, beta: float, maximizando: bool, 
                          cor_jogador: CorPeca) -> float:
        """Implementação completa da recursão com Poda Alfa-Beta."""
        self.nos_explorados += 1
        
        # Casos base
        terminado, vencedor = tabuleiro.jogo_terminado()
        if terminado or profundidade == 0:
            return tabuleiro.avaliar_posicao()
        
        movimentos = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        if not movimentos:
            return tabuleiro.avaliar_posicao()
        
        # Recursão com poda
        if maximizando:
            melhor_valor = float('-inf')
            for movimento in movimentos:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.alfabeta_recursivo(
                    tabuleiro_copia, 
                    profundidade - 1, 
                    alfa, beta, False, 
                    CorPeca.PRETA
                )
                
                melhor_valor = max(melhor_valor, valor)
                alfa = max(alfa, melhor_valor)
                
                if beta <= alfa:
                    break  # Poda alfa-beta
            
            return melhor_valor
        else:
            melhor_valor = float('inf')
            for movimento in movimentos:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.alfabeta_recursivo(
                    tabuleiro_copia, 
                    profundidade - 1, 
                    alfa, beta, True, 
                    CorPeca.BRANCA
                )
                
                melhor_valor = min(melhor_valor, valor)
                beta = min(beta, melhor_valor)
                
                if beta <= alfa:
                    break  # Poda alfa-beta
            
            return melhor_valor


class ExpectMiniMaxCompleto(EstrategiaJogo):
    """
    Implementação completa do algoritmo Expect MiniMax.
    
    Esta é a solução de referência para comparação.
    Tente implementar primeiro nos espaços TODO!
    """
    
    def __init__(self, profundidade_maxima: int = 6, probabilidade_erro: float = 0.1):
        super().__init__(profundidade_maxima)
        self.probabilidade_erro = probabilidade_erro
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """Implementação completa do Expect MiniMax."""
        self.resetar_estatisticas()
        inicio = time.time()
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        melhor_movimento = None
        maximizando = (cor_jogador == CorPeca.BRANCA)
        
        if maximizando:
            melhor_valor = float('-inf')
            for movimento in movimentos_possiveis:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.expectminimax_recursivo(
                    tabuleiro_copia, 
                    self.profundidade_maxima - 1, 
                    True,  # Próximo nível é nó de chance
                    CorPeca.PRETA
                )
                
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = movimento
        else:
            melhor_valor = float('inf')
            for movimento in movimentos_possiveis:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.expectminimax_recursivo(
                    tabuleiro_copia, 
                    self.profundidade_maxima - 1, 
                    True,  # Próximo nível é nó de chance
                    CorPeca.BRANCA
                )
                
                if valor < melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = movimento
        
        self.melhor_movimento_encontrado = melhor_movimento
        self.tempo_execucao = time.time() - inicio
        return melhor_movimento
    
    def expectminimax_recursivo(self, tabuleiro: Tabuleiro, profundidade: int,
                               no_chance: bool, cor_jogador: CorPeca) -> float:
        """Implementação completa da recursão Expect MiniMax."""
        self.nos_explorados += 1
        
        # Casos base
        terminado, vencedor = tabuleiro.jogo_terminado()
        if terminado or profundidade == 0:
            return tabuleiro.avaliar_posicao()
        
        movimentos = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        if not movimentos:
            return tabuleiro.avaliar_posicao()
        
        if no_chance:
            # Nó de chance - calcular valor esperado
            if len(movimentos) == 1:
                # Só um movimento, sem incerteza
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimentos[0])
                return self.expectminimax_recursivo(
                    tabuleiro_copia, profundidade - 1, False,
                    CorPeca.PRETA if cor_jogador == CorPeca.BRANCA else CorPeca.BRANCA
                )
            
            # Múltiplos movimentos - simular incerteza
            valores_movimentos = []
            for movimento in movimentos:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self.expectminimax_recursivo(
                    tabuleiro_copia, profundidade - 1, False,
                    CorPeca.PRETA if cor_jogador == CorPeca.BRANCA else CorPeca.BRANCA
                )
                valores_movimentos.append(valor)
            
            # Valor esperado: movimento ótimo com prob (1-erro), aleatório com prob erro
            melhor_valor = max(valores_movimentos) if cor_jogador == CorPeca.BRANCA else min(valores_movimentos)
            valor_medio = sum(valores_movimentos) / len(valores_movimentos)
            
            valor_esperado = ((1 - self.probabilidade_erro) * melhor_valor + 
                            self.probabilidade_erro * valor_medio)
            
            return valor_esperado
        
        else:
            # Nó de decisão normal
            maximizando = (cor_jogador == CorPeca.BRANCA)
            
            if maximizando:
                melhor_valor = float('-inf')
                for movimento in movimentos:
                    tabuleiro_copia = tabuleiro.copy()
                    tabuleiro_copia.executar_movimento(movimento)
                    
                    valor = self.expectminimax_recursivo(
                        tabuleiro_copia, profundidade - 1, True,
                        CorPeca.PRETA
                    )
                    melhor_valor = max(melhor_valor, valor)
                
                return melhor_valor
            else:
                melhor_valor = float('inf')
                for movimento in movimentos:
                    tabuleiro_copia = tabuleiro.copy()
                    tabuleiro_copia.executar_movimento(movimento)
                    
                    valor = self.expectminimax_recursivo(
                        tabuleiro_copia, profundidade - 1, True,
                        CorPeca.BRANCA
                    )
                    melhor_valor = min(melhor_valor, valor)
                
                return melhor_valor


class MiniMaxComIterativeDeepening(EstrategiaJogo):
    """
    Implementação do MiniMax com Iterative Deepening.
    
    Executa buscas com profundidades crescentes até atingir
    o limite de tempo ou profundidade máxima.
    """
    
    def __init__(self, profundidade_maxima: int = 8, tempo_limite: float = 5.0):
        super().__init__(profundidade_maxima)
        self.tempo_limite = tempo_limite
        self.profundidade_alcancada = 0
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca) -> Movimento:
        """Implementação com Iterative Deepening."""
        self.resetar_estatisticas()
        inicio = time.time()
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        melhor_movimento = movimentos_possiveis[0]  # Fallback
        
        # Busca com profundidades crescentes
        for profundidade in range(1, self.profundidade_maxima + 1):
            if time.time() - inicio > self.tempo_limite:
                break
            
            try:
                movimento_atual = self._buscar_profundidade(
                    tabuleiro, cor_jogador, profundidade, inicio
                )
                if movimento_atual:
                    melhor_movimento = movimento_atual
                    self.profundidade_alcancada = profundidade
            except TimeoutError:
                break
        
        self.melhor_movimento_encontrado = melhor_movimento
        self.tempo_execucao = time.time() - inicio
        return melhor_movimento
    
    def _buscar_profundidade(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca, 
                           profundidade: int, inicio_tempo: float) -> Optional[Movimento]:
        """Busca com profundidade específica."""
        movimentos = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        melhor_movimento = None
        maximizando = (cor_jogador == CorPeca.BRANCA)
        
        if maximizando:
            melhor_valor = float('-inf')
            for movimento in movimentos:
                if time.time() - inicio_tempo > self.tempo_limite:
                    raise TimeoutError()
                
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self._minimax_com_timeout(
                    tabuleiro_copia, profundidade - 1, False,
                    CorPeca.PRETA, inicio_tempo
                )
                
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = movimento
        else:
            melhor_valor = float('inf')
            for movimento in movimentos:
                if time.time() - inicio_tempo > self.tempo_limite:
                    raise TimeoutError()
                
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self._minimax_com_timeout(
                    tabuleiro_copia, profundidade - 1, True,
                    CorPeca.BRANCA, inicio_tempo
                )
                
                if valor < melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = movimento
        
        return melhor_movimento
    
    def _minimax_com_timeout(self, tabuleiro: Tabuleiro, profundidade: int,
                           maximizando: bool, cor_jogador: CorPeca, 
                           inicio_tempo: float) -> float:
        """MiniMax com verificação de timeout."""
        if time.time() - inicio_tempo > self.tempo_limite:
            raise TimeoutError()
        
        self.nos_explorados += 1
        
        terminado, vencedor = tabuleiro.jogo_terminado()
        if terminado or profundidade == 0:
            return tabuleiro.avaliar_posicao()
        
        movimentos = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        if not movimentos:
            return tabuleiro.avaliar_posicao()
        
        if maximizando:
            melhor_valor = float('-inf')
            for movimento in movimentos:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self._minimax_com_timeout(
                    tabuleiro_copia, profundidade - 1, False,
                    CorPeca.PRETA, inicio_tempo
                )
                melhor_valor = max(melhor_valor, valor)
            
            return melhor_valor
        else:
            melhor_valor = float('inf')
            for movimento in movimentos:
                tabuleiro_copia = tabuleiro.copy()
                tabuleiro_copia.executar_movimento(movimento)
                
                valor = self._minimax_com_timeout(
                    tabuleiro_copia, profundidade - 1, True,
                    CorPeca.BRANCA, inicio_tempo
                )
                melhor_valor = min(melhor_valor, valor)
            
            return melhor_valor
    
    def obter_estatisticas(self) -> dict:
        """Retorna estatísticas incluindo profundidade alcançada."""
        stats = super().obter_estatisticas()
        stats['profundidade_alcancada'] = self.profundidade_alcancada
        return stats


def comparar_algoritmos():
    """
    Função para comparar o desempenho dos diferentes algoritmos.
    
    Esta função executa uma série de testes comparando:
    - MiniMax vs Poda Alfa-Beta
    - Diferentes profundidades
    - Tempo de execução
    - Qualidade das decisões
    """
    print("=== COMPARAÇÃO DE ALGORITMOS - SOLUÇÃO COMPLETA ===")
    print()
    
    from jogo_damas import JogoDamas
    
    algoritmos = {
        'MiniMax-3': MiniMaxCompleto(profundidade_maxima=3),
        'AlfaBeta-3': PodaAlfaBetaCompleta(profundidade_maxima=3),
        'MiniMax-4': MiniMaxCompleto(profundidade_maxima=4),
        'AlfaBeta-4': PodaAlfaBetaCompleta(profundidade_maxima=4),
        'ExpectMiniMax-3': ExpectMiniMaxCompleto(profundidade_maxima=3),
        'IterativeDeepening': MiniMaxComIterativeDeepening(profundidade_maxima=6, tempo_limite=2.0)
    }
    
    print("Executando comparação entre algoritmos...")
    
    for nome, algoritmo in algoritmos.items():
        print(f"\nTestando {nome}:")
        
        # Executar algumas partidas contra jogador aleatório
        vitorias = 0
        tempo_total = 0
        nos_total = 0
        partidas_teste = 3
        
        for i in range(partidas_teste):
            jogo = JogoDamas(
                estrategia_brancas=algoritmo,
                estrategia_pretas=random.choice([
                    JogadorAleatorio() for _ in range(3)  # Diferentes instâncias
                ]),
                exibir_tabuleiro=False,
                limite_jogadas=100
            )
            
            vencedor = jogo.jogar()
            if vencedor == CorPeca.BRANCA:
                vitorias += 1
            
            resumo = jogo.obter_resumo_partida()
            stats_brancas = resumo['estatisticas_jogadores']['branca']
            
            if stats_brancas:
                tempo_total += sum(s['tempo_execucao'] for s in stats_brancas)
                nos_total += sum(s['nos_explorados'] for s in stats_brancas)
        
        taxa_vitoria = vitorias / partidas_teste
        tempo_medio = tempo_total / partidas_teste
        nos_medio = nos_total / partidas_teste
        
        print(f"  Taxa de vitória: {taxa_vitoria:.1%}")
        print(f"  Tempo médio: {tempo_medio:.3f}s")
        print(f"  Nós explorados médios: {nos_medio:.0f}")
        
        # Estatísticas específicas do algoritmo
        stats = algoritmo.obter_estatisticas()
        if 'profundidade_alcancada' in stats:
            print(f"  Profundidade alcançada: {stats['profundidade_alcancada']}")


def demonstrar_poda_alfabeta():
    """
    Demonstra a eficiência da poda alfa-beta comparando
    com MiniMax puro em termos de nós explorados.
    """
    print("=== DEMONSTRAÇÃO DA EFICIÊNCIA DA PODA ALFA-BETA ===")
    print()
    
    from jogo_damas import JogoDamas
    
    tabuleiro = Tabuleiro()
    
    # Comparar número de nós explorados
    profundidades = [3, 4, 5]
    
    for prof in profundidades:
        print(f"Profundidade {prof}:")
        
        # MiniMax puro
        minimax = MiniMaxCompleto(profundidade_maxima=prof)
        inicio = time.time()
        movimento_mm = minimax.escolher_movimento(tabuleiro, CorPeca.BRANCA)
        tempo_mm = time.time() - inicio
        nos_mm = minimax.nos_explorados
        
        # Poda Alfa-Beta
        alfabeta = PodaAlfaBetaCompleta(profundidade_maxima=prof)
        inicio = time.time()
        movimento_ab = alfabeta.escolher_movimento(tabuleiro, CorPeca.BRANCA)
        tempo_ab = time.time() - inicio
        nos_ab = alfabeta.nos_explorados
        
        # Resultados
        reducao_nos = (nos_mm - nos_ab) / nos_mm * 100
        speedup = tempo_mm / tempo_ab if tempo_ab > 0 else float('inf')
        
        print(f"  MiniMax: {nos_mm} nós, {tempo_mm:.3f}s")
        print(f"  Alfa-Beta: {nos_ab} nós, {tempo_ab:.3f}s")
        print(f"  Redução de nós: {reducao_nos:.1f}%")
        print(f"  Speedup: {speedup:.1f}x")
        print()


if __name__ == "__main__":
    print("ARQUIVO DE SOLUÇÃO DOS ALGORITMOS DE BUSCA COMPETITIVA")
    print("=" * 60)
    print()
    print("Este arquivo contém as implementações completas dos algoritmos.")
    print("Use apenas para comparação após implementar nos espaços TODO!")
    print()
    
    print("Executando demonstrações...")
    print()
    
    # Demonstrar eficiência da poda
    demonstrar_poda_alfabeta()
    
    # Comparar algoritmos
    comparar_algoritmos()
    
    print("\n" + "=" * 60)
    print("Demonstrações concluídas!")
    print("Agora implemente os algoritmos nos espaços TODO e compare os resultados!") 