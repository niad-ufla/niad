"""
Módulo principal do jogo de damas.

Este módulo contém a classe JogoDamas que coordena uma partida completa,
incluindo a interação entre jogadores, validação de movimentos e
determinação do vencedor.
"""

from typing import Optional, Tuple, Dict, Any
from .tabuleiro import Tabuleiro, Movimento, CorPeca, MovimentoInvalidoError
from exercicios.algoritmos_busca import EstrategiaJogo


# A importação dos algoritmos agora será feita por quem usar este módulo
# para evitar dependência circular entre os pacotes

class StatusJogo:
    """Classe para representar o status atual do jogo."""
    
    def __init__(self):
        self.em_andamento = True
        self.vencedor: Optional[CorPeca] = None
        self.numero_jogadas = 0
        self.historico_avaliacoes = []
        self.estatisticas_jogadores = {
            CorPeca.BRANCA: [],
            CorPeca.PRETA: []
        }
    
    def finalizar_jogo(self, vencedor: Optional[CorPeca]):
        """
        Finaliza o jogo e define o vencedor.
        
        Args:
            vencedor (Optional[CorPeca]): Cor do vencedor (None para empate)
        """
        self.em_andamento = False
        self.vencedor = vencedor
    
    def registrar_jogada(self, estatisticas: Dict[str, Any], avaliacao: float):
        """
        Registra estatísticas de uma jogada.
        
        Args:
            estatisticas (Dict[str, Any]): Estatísticas da busca realizada
            avaliacao (float): Avaliação da posição após o movimento
        """
        self.numero_jogadas += 1
        self.historico_avaliacoes.append(str(avaliacao))


class JogoDamas:
    """
    Classe principal que coordena uma partida de damas.
    
    Esta classe gerencia o loop principal do jogo, coordenando a interação
    entre os jogadores (humanos ou IA) e mantendo o estado da partida.
    """
    
    def __init__(self, estrategia_brancas: EstrategiaJogo, 
                 estrategia_pretas: EstrategiaJogo,
                 exibir_tabuleiro: bool = True,
                 limite_jogadas: int = 200):
        """
        Inicializa uma nova partida de damas.
        
        Args:
            estrategia_brancas: Estratégia para as peças brancas (deve implementar EstrategiaJogo)
            estrategia_pretas: Estratégia para as peças pretas (deve implementar EstrategiaJogo)
            exibir_tabuleiro (bool): Se deve exibir o tabuleiro a cada jogada
            limite_jogadas (int): Limite de jogadas para evitar jogos infinitos
        """
        self.tabuleiro = Tabuleiro()
        self.estrategias = {
            CorPeca.BRANCA: estrategia_brancas,
            CorPeca.PRETA: estrategia_pretas
        }
        self.exibir_tabuleiro = exibir_tabuleiro
        self.limite_jogadas = limite_jogadas
        self.status = StatusJogo()
        
        # Log de eventos do jogo
        self.log_eventos = []
        
        self._log_evento("Jogo iniciado")
        self._log_evento(f"Estratégia brancas: {type(estrategia_brancas).__name__}")
        self._log_evento(f"Estratégia pretas: {type(estrategia_pretas).__name__}")
    
    def _log_evento(self, evento: str):
        """
        Registra um evento no log do jogo.
        
        Args:
            evento (str): Descrição do evento
        """
        self.log_eventos.append(f"Jogada {self.status.numero_jogadas}: {evento}")
    
    def jogar(self) -> CorPeca:
        """
        Executa uma partida completa de damas.
        
        Returns:
            CorPeca: Cor do vencedor (ou None em caso de empate)
        """
        if self.exibir_tabuleiro:
            print("=== JOGO DE DAMAS ===")
            print(self.tabuleiro.exibir())
        
        while self.status.em_andamento:
            # Verificar se o jogo terminou
            jogo_terminado, vencedor = self.tabuleiro.jogo_terminado()
            if jogo_terminado:
                self.status.finalizar_jogo(vencedor)
                break
            
            # Verificar limite de jogadas
            if self.status.numero_jogadas >= self.limite_jogadas:
                self._log_evento(f"Limite de jogadas ({self.limite_jogadas}) atingido")
                # Determinar vencedor pela avaliação atual
                avaliacao_final = self.tabuleiro.avaliar_posicao()
                if avaliacao_final > 0:
                    vencedor = CorPeca.BRANCA
                elif avaliacao_final < 0:
                    vencedor = CorPeca.PRETA
                else:
                    vencedor = None  # Empate
                self.status.finalizar_jogo(vencedor)
                break
            
            # Realizar jogada
            try:
                self._realizar_jogada()
            except Exception as e:
                self._log_evento(f"Erro durante jogada: {e}")
                # Em caso de erro, considerar derrota do jogador atual
                jogador_atual = self.tabuleiro.turno_atual
                vencedor = CorPeca.PRETA if jogador_atual == CorPeca.BRANCA else CorPeca.BRANCA
                self.status.finalizar_jogo(vencedor)
                break
        
        self._finalizar_partida()
        return self.status.vencedor
    
    def _realizar_jogada(self):
        """Realiza uma jogada completa para o jogador atual."""
        jogador_atual = self.tabuleiro.turno_atual
        estrategia = self.estrategias[jogador_atual]
        
        if self.exibir_tabuleiro:
            print(f"\n--- Turno de {jogador_atual.value} ---")
        
        # Obter movimento da estratégia
        movimento = estrategia.escolher_movimento(self.tabuleiro, jogador_atual)
        
        # Registrar estatísticas
        estatisticas = estrategia.obter_estatisticas()
        self.status.estatisticas_jogadores[jogador_atual].append(estatisticas)
        
        # Executar movimento
        self.tabuleiro.executar_movimento(movimento)
        
        # Registrar evento
        self._log_evento(f"{jogador_atual.value} jogou: {movimento}")
        
        # Registrar avaliação da posição
        avaliacao = self.tabuleiro.avaliar_posicao()
        self.status.registrar_jogada(estatisticas, avaliacao)
        
        if self.exibir_tabuleiro:
            print(f"Movimento: {movimento}")
            if estatisticas['tempo_execucao'] > 0:
                print(f"Tempo: {estatisticas['tempo_execucao']:.3f}s, "
                      f"Nós explorados: {estatisticas['nos_explorados']}")
            print(f"Avaliação: {avaliacao:.2f}")
            print(self.tabuleiro.exibir())
    
    def _finalizar_partida(self):
        """Finaliza a partida e exibe resultados."""
        self._log_evento("Jogo finalizado")
        
        if self.exibir_tabuleiro:
            print("\n=== RESULTADO FINAL ===")
            if self.status.vencedor:
                print(f"Vencedor: {self.status.vencedor.value}")
            else:
                print("Empate!")
            
            print(f"Número de jogadas: {self.status.numero_jogadas}")
            
            # Estatísticas dos jogadores
            for cor in [CorPeca.BRANCA, CorPeca.PRETA]:
                stats = self.status.estatisticas_jogadores[cor]
                if stats:
                    tempo_total = sum(s['tempo_execucao'] for s in stats)
                    nos_total = sum(s['nos_explorados'] for s in stats)
                    print(f"\n{cor.value}:")
                    print(f"  Tempo total: {tempo_total:.3f}s")
                    print(f"  Nós explorados: {nos_total}")
                    print(f"  Tempo médio por jogada: {tempo_total/len(stats):.3f}s")
    
    def obter_resumo_partida(self) -> Dict[str, Any]:
        """
        Retorna um resumo completo da partida.
        
        Returns:
            Dict[str, Any]: Dicionário com informações da partida
        """
        return {
            'vencedor': self.status.vencedor.value if self.status.vencedor else None,
            'numero_jogadas': self.status.numero_jogadas,
            'avaliacao_final': str(self.tabuleiro.avaliar_posicao()) if abs(self.tabuleiro.avaliar_posicao()) == float('inf') or abs(self.tabuleiro.avaliar_posicao()) == float('-inf') else self.tabuleiro.avaliar_posicao(),
            'pecas_restantes': {
                'brancas': self.tabuleiro.contar_pecas(CorPeca.BRANCA),
                'pretas': self.tabuleiro.contar_pecas(CorPeca.PRETA)
            },
            'historico_avaliacoes': self.status.historico_avaliacoes,
            'estatisticas_jogadores': {
                'branca': self.status.estatisticas_jogadores[CorPeca.BRANCA],
                'preta': self.status.estatisticas_jogadores[CorPeca.PRETA]
            },
            'log_eventos': self.log_eventos,
            'historico_movimentos': [str(mov) for mov in self.tabuleiro.historico_movimentos]
        }
    
    def salvar_partida(self, nome_arquivo: str):
        """
        Salva o resumo da partida em um arquivo JSON.
        
        Args:
            nome_arquivo (str): Nome do arquivo para salvar
        """
        import json
        from datetime import datetime
        
        resumo = self.obter_resumo_partida()
        resumo['data_partida'] = datetime.now().isoformat()
        resumo['estrategias'] = {
            'brancas': type(self.estrategias[CorPeca.BRANCA]).__name__,
            'pretas': type(self.estrategias[CorPeca.PRETA]).__name__
        }
        
        # Converter objetos não serializáveis
        def converter_para_json(obj):
            if hasattr(obj, 'value'):  # Enum
                return obj.value
            return str(obj)
        
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(resumo, f, indent=2, ensure_ascii=False, default=converter_para_json)
        
        print(f"Partida salva em: {nome_arquivo}") 