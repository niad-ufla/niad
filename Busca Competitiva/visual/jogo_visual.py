"""
Jogo visual de damas integrando interface gráfica com lógica do jogo.

Este módulo combina a InterfaceGrafica com as classes do jogo para
criar uma experiência visual completa e interativa.
"""

import pygame
import time
from typing import Optional, Tuple
from jogo_damas import JogoDamas, Tabuleiro, CorPeca
from exercicios.algoritmos_busca import EstrategiaJogo, JogadorHumano, JogadorAleatorio
from .interface_grafica import InterfaceGrafica


class JogadorHumanoVisual(EstrategiaJogo):
    """
    Adaptação do JogadorHumano para interface gráfica.
    
    Em vez de usar input de console, usa cliques do mouse
    na interface gráfica.
    """
    
    def __init__(self, interface: InterfaceGrafica):
        """
        Inicializa jogador humano visual.
        
        Args:
            interface (InterfaceGrafica): Interface gráfica para interação
        """
        super().__init__()
        self.interface = interface
        self.movimento_selecionado = None
    
    def escolher_movimento(self, tabuleiro: Tabuleiro, cor_jogador: CorPeca):
        """
        Escolhe movimento através de cliques na interface gráfica.
        
        Args:
            tabuleiro (Tabuleiro): Estado atual do tabuleiro
            cor_jogador (CorPeca): Cor do jogador
            
        Returns:
            Movimento: Movimento escolhido pelo usuário
        """
        self.resetar_estatisticas()
        inicio = time.time()
        
        movimentos_possiveis = tabuleiro.obter_movimentos_possiveis(cor_jogador)
        if not movimentos_possiveis:
            raise ValueError("Não há movimentos possíveis para o jogador atual")
        
        self.movimento_selecionado = None
        origem_selecionada = None
        
        # Loop de seleção de movimento
        while self.movimento_selecionado is None:
            eventos = self.interface.processar_eventos()
            
            for evento in eventos:
                if evento == "quit":
                    raise SystemExit("Jogo fechado pelo usuário")
                
                elif evento.startswith("click:"):
                    # Parsear posição do clique
                    _, linha_str, coluna_str = evento.split(":")
                    posicao_clicada = (int(linha_str), int(coluna_str))
                    
                    if origem_selecionada is None:
                        # Primeira seleção: origem
                        peca = tabuleiro.get_peca(posicao_clicada)
                        if peca and peca.cor == cor_jogador:
                            origem_selecionada = posicao_clicada
                            self.interface.selecionar_posicao(posicao_clicada, tabuleiro)
                    else:
                        # Segunda seleção: destino
                        if posicao_clicada == origem_selecionada:
                            # Clicou na mesma posição, desselecionar
                            origem_selecionada = None
                            self.interface.desselecionar()
                        else:
                            # Tentar fazer movimento
                            movimento = self.interface.encontrar_movimento(
                                origem_selecionada, posicao_clicada, tabuleiro
                            )
                            if movimento:
                                self.movimento_selecionado = movimento
                            else:
                                # Movimento inválido, tentar nova seleção
                                peca = tabuleiro.get_peca(posicao_clicada)
                                if peca and peca.cor == cor_jogador:
                                    origem_selecionada = posicao_clicada
                                    self.interface.selecionar_posicao(posicao_clicada, tabuleiro)
                                else:
                                    origem_selecionada = None
                                    self.interface.desselecionar()
            
            # Renderizar interface
            info = f"Jogador {cor_jogador.value} - Clique para selecionar peça"
            if origem_selecionada:
                info = f"Peça selecionada - Clique no destino"
            
            self.interface.renderizar(tabuleiro, info)
        
        # Limpar seleção
        self.interface.desselecionar()
        
        self.nos_explorados = 1
        self.melhor_movimento_encontrado = self.movimento_selecionado
        self.tempo_execucao = time.time() - inicio
        
        return self.movimento_selecionado


class JogoVisual:
    """
    Classe principal para jogos de damas com interface gráfica.
    
    Integra a lógica do jogo com a interface visual, permitindo
    partidas interativas e visualização de algoritmos.
    """
    
    def __init__(self, largura: int = 800, altura: int = 950):
        """
        Inicializa o jogo visual.
        
        Args:
            largura (int): Largura da janela
            altura (int): Altura da janela (aumentada para mais espaço)
        """
        self.interface = InterfaceGrafica(largura, altura)
        self.jogo: Optional[JogoDamas] = None
        self.pausado = False
        self.velocidade_ia = 1.0  # Segundos entre jogadas da IA
    
    def criar_jogo(self, estrategia_brancas: EstrategiaJogo, 
                   estrategia_pretas: EstrategiaJogo) -> JogoDamas:
        """
        Cria um novo jogo com as estratégias especificadas.
        
        Args:
            estrategia_brancas (EstrategiaJogo): Estratégia para peças brancas
            estrategia_pretas (EstrategiaJogo): Estratégia para peças pretas
            
        Returns:
            JogoDamas: Nova instância do jogo
        """
        # Adaptar jogadores humanos para interface gráfica
        if isinstance(estrategia_brancas, JogadorHumano):
            estrategia_brancas = JogadorHumanoVisual(self.interface)
        if isinstance(estrategia_pretas, JogadorHumano):
            estrategia_pretas = JogadorHumanoVisual(self.interface)
        
        self.jogo = JogoDamas(
            estrategia_brancas=estrategia_brancas,
            estrategia_pretas=estrategia_pretas,
            exibir_tabuleiro=False,  # Não usar output de console
            limite_jogadas=300
        )
        
        return self.jogo
    
    def executar_partida(self, estrategia_brancas: EstrategiaJogo, 
                        estrategia_pretas: EstrategiaJogo) -> Optional[CorPeca]:
        """
        Executa uma partida completa com interface gráfica.
        
        Args:
            estrategia_brancas (EstrategiaJogo): Estratégia para peças brancas
            estrategia_pretas (EstrategiaJogo): Estratégia para peças pretas
            
        Returns:
            Optional[CorPeca]: Vencedor da partida ou None se o jogo foi fechado
        """
        jogo = self.criar_jogo(estrategia_brancas, estrategia_pretas)
        
        # Renderizar estado inicial
        self.interface.renderizar(jogo.tabuleiro, "Jogo iniciado!")
        pygame.time.wait(1000)
        
        try:
            # Loop principal do jogo
            while jogo.status.em_andamento:
                # Processar eventos da interface
                eventos = self.interface.processar_eventos()
                
                for evento in eventos:
                    if evento == "quit":
                        return None
                    elif evento == "reset":
                        return self.executar_partida(estrategia_brancas, estrategia_pretas)
                    elif evento == "help":
                        self.mostrar_ajuda()
                
                # Verificar se o jogo terminou
                jogo_terminado, vencedor = jogo.tabuleiro.jogo_terminado()
                if jogo_terminado:
                    jogo.status.finalizar_jogo(vencedor)
                    break
                
                # Verificar limite de jogadas
                if jogo.status.numero_jogadas >= jogo.limite_jogadas:
                    avaliacao_final = jogo.tabuleiro.avaliar_posicao()
                    if avaliacao_final > 0:
                        vencedor = CorPeca.BRANCA
                    elif avaliacao_final < 0:
                        vencedor = CorPeca.PRETA
                    else:
                        vencedor = None
                    jogo.status.finalizar_jogo(vencedor)
                    break
                
                # Realizar jogada
                try:
                    self._realizar_jogada_visual(jogo)
                except SystemExit:
                    return None
                except Exception as e:
                    self.interface.mostrar_mensagem(f"Erro: {e}")
                    # Considerar derrota do jogador atual
                    jogador_atual = jogo.tabuleiro.turno_atual
                    vencedor = CorPeca.PRETA if jogador_atual == CorPeca.BRANCA else CorPeca.BRANCA
                    jogo.status.finalizar_jogo(vencedor)
                    break
            
            # Mostrar resultado final
            self._mostrar_resultado_final(jogo)
            return jogo.status.vencedor
            
        except Exception as e:
            self.interface.mostrar_mensagem(f"Erro inesperado: {e}")
            return None
    
    def _realizar_jogada_visual(self, jogo: JogoDamas):
        """
        Realiza uma jogada com visualização.
        
        Args:
            jogo (JogoDamas): Instância do jogo atual
        """
        jogador_atual = jogo.tabuleiro.turno_atual
        estrategia = jogo.estrategias[jogador_atual]
        
        # Informação sobre o turno
        nome_estrategia = type(estrategia).__name__
        info = f"Turno: {jogador_atual.value} ({nome_estrategia})"
        
        # Se for IA, adicionar delay para visualização
        if not isinstance(estrategia, JogadorHumanoVisual):
            info += " - Pensando..."
            self.interface.renderizar(jogo.tabuleiro, info)
            pygame.time.wait(int(self.velocidade_ia * 1000))
        
        # Obter movimento da estratégia
        movimento = estrategia.escolher_movimento(jogo.tabuleiro, jogador_atual)
        
        # Registrar estatísticas
        estatisticas = estrategia.obter_estatisticas()
        jogo.status.estatisticas_jogadores[jogador_atual].append(estatisticas)
        
        # Executar movimento
        jogo.tabuleiro.executar_movimento(movimento)
        
        # Registrar avaliação da posição
        avaliacao = jogo.tabuleiro.avaliar_posicao()
        jogo.status.registrar_jogada(estatisticas, avaliacao)
        
        # Mostrar informações do movimento
        info_movimento = f"{jogador_atual.value}: {movimento}"
        if estatisticas['tempo_execucao'] > 0:
            info_movimento += f" | Tempo: {estatisticas['tempo_execucao']:.3f}s"
            info_movimento += f" | Nós: {estatisticas['nos_explorados']}"
        
        self.interface.renderizar(jogo.tabuleiro, info_movimento)
        
        # Pausa para visualizar o movimento
        if not isinstance(estrategia, JogadorHumanoVisual):
            pygame.time.wait(500)
    
    def _mostrar_resultado_final(self, jogo: JogoDamas):
        """
        Mostra o resultado final da partida.
        
        Args:
            jogo (JogoDamas): Instância do jogo finalizado
        """
        if jogo.status.vencedor:
            mensagem = f"Vencedor: {jogo.status.vencedor.value.title()}!"
        else:
            mensagem = "Empate!"
        
        mensagem += f"\nJogadas: {jogo.status.numero_jogadas}"
        
        # Mostrar mensagem e aguardar
        self.interface.mostrar_mensagem(mensagem)
        
        # Aguardar input do usuário para continuar
        aguardando = True
        while aguardando:
            eventos = self.interface.processar_eventos()
            for evento in eventos:
                if evento == "quit" or evento.startswith("click:"):
                    aguardando = False
                    break
            
            self.interface.renderizar(jogo.tabuleiro, "Clique para continuar...")
    
    def mostrar_ajuda(self):
        """Mostra tela de ajuda."""
        ajuda_texto = [
            "JOGO DE DAMAS - AJUDA",
            "",
            "CONTROLES:",
            "• Clique nas peças para selecioná-las",
            "• Clique no destino para mover",
            "• R - Reiniciar jogo",
            "• H - Mostrar esta ajuda",
            "• ESC - Sair do jogo",
            "",
            "REGRAS:",
            "• Peças movem diagonalmente",
            "• Capturas são obrigatórias",
            "• Peças viram damas na última fileira",
            "",
            "Pressione qualquer tecla para continuar..."
        ]
        
        # Limpar tela
        self.interface.tela.fill(self.interface.COR_FUNDO)
        
        # Desenhar texto da ajuda
        y_offset = 100
        for linha in ajuda_texto:
            if linha == ajuda_texto[0]:  # Título
                texto_surface = self.interface.fonte.render(linha, True, self.interface.COR_TEXTO)
            else:
                texto_surface = self.interface.fonte_pequena.render(linha, True, self.interface.COR_TEXTO)
            
            x = (self.interface.largura - texto_surface.get_width()) // 2
            self.interface.tela.blit(texto_surface, (x, y_offset))
            y_offset += 30
        
        pygame.display.flip()
        
        # Aguardar input
        aguardando = True
        while aguardando:
            eventos = self.interface.processar_eventos()
            for evento in eventos:
                if evento == "quit" or len(eventos) > 0:
                    aguardando = False
                    break
    
    def definir_velocidade_ia(self, velocidade: float):
        """
        Define a velocidade de jogada da IA.
        
        Args:
            velocidade (float): Tempo em segundos entre jogadas da IA
        """
        self.velocidade_ia = max(0.1, min(5.0, velocidade))
    
    def fechar(self):
        """Fecha o jogo visual."""
        self.interface.fechar()


def main():
    """Função principal para demonstrar o jogo visual."""
    try:
        print("Iniciando jogo visual de damas...")
        print("Certifique-se de ter pygame instalado: pip install pygame")
        
        jogo_visual = JogoVisual()
        
        # Configurar partida: Humano vs IA
        from exercicios.algoritmos_busca import JogadorHumano, JogadorAleatorio
        
        vencedor = jogo_visual.executar_partida(
            estrategia_brancas=JogadorHumano(),  # Será convertido para JogadorHumanoVisual
            estrategia_pretas=JogadorAleatorio()
        )
        
        if vencedor:
            print(f"Partida finalizada! Vencedor: {vencedor.value}")
        else:
            print("Jogo fechado pelo usuário.")
        
        jogo_visual.fechar()
        
    except ImportError:
        print("Erro: Pygame não está instalado!")
        print("Instale com: pip install pygame")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main() 