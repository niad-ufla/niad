"""
Interface principal para o jogo de damas com algoritmos de busca competitiva.

Este módulo fornece uma interface amigável para executar partidas,
comparar algoritmos e realizar experimentos com diferentes estratégias.
"""

import sys
import time
from typing import List, Dict, Any

# Importar módulos do jogo de damas
from jogo_damas import JogoDamas, CorPeca

# Importar algoritmos de busca
from exercicios.algoritmos_busca import (
    MiniMax, PodaAlfaBeta, ExpectMiniMax, 
    JogadorAleatorio, JogadorHumano
)

# Importar interface visual (opcional)
try:
    from visual import JogoVisual
    VISUAL_DISPONIVEL = True
except ImportError:
    VISUAL_DISPONIVEL = False


def executar_partida_simples():
    """Executa uma partida simples entre dois jogadores aleatórios."""
    print("=== PARTIDA SIMPLES ===")
    print("Executando partida entre dois jogadores aleatórios...")
    
    jogo = JogoDamas(
        estrategia_brancas=JogadorAleatorio(),
        estrategia_pretas=JogadorAleatorio(),
        exibir_tabuleiro=False,
        limite_jogadas=100
    )
    
    vencedor = jogo.jogar()
    resumo = jogo.obter_resumo_partida()
    
    print(f"Vencedor: {vencedor.value if vencedor else 'Empate'}")
    print(f"Número de jogadas: {resumo['numero_jogadas']}")
    print(f"Peças restantes - Brancas: {resumo['pecas_restantes']['brancas']}, "
          f"Pretas: {resumo['pecas_restantes']['pretas']}")


def executar_torneio_algoritmos(numero_partidas: int = 10):
    """
    Executa um torneio entre diferentes algoritmos de busca.
    
    Args:
        numero_partidas (int): Número de partidas para cada confronto
    """
    print(f"=== TORNEIO DE ALGORITMOS ({numero_partidas} partidas cada) ===")
    print()
    
    # TODO: Quando os algoritmos estiverem implementados, descomente as linhas abaixo
    # algoritmos = {
    #     'MiniMax_3': MiniMax(profundidade_maxima=3),
    #     'MiniMax_4': MiniMax(profundidade_maxima=4),
    #     'AlfaBeta_3': PodaAlfaBeta(profundidade_maxima=3),
    #     'AlfaBeta_4': PodaAlfaBeta(profundidade_maxima=4),
    #     'ExpectMiniMax_3': ExpectMiniMax(profundidade_maxima=3, probabilidade_erro=0.1),
    #     'Aleatorio': JogadorAleatorio()
    # }
    
    # Por enquanto, usando apenas jogadores aleatórios para demonstração
    algoritmos = {
        'Aleatorio_A': JogadorAleatorio(),
        'Aleatorio_B': JogadorAleatorio()
    }
    
    resultados = {}
    
    nomes_algoritmos = list(algoritmos.keys())
    for i, nome1 in enumerate(nomes_algoritmos):
        for nome2 in nomes_algoritmos[i+1:]:
            print(f"Confronto: {nome1} vs {nome2}")
            
            vitorias_1 = 0
            vitorias_2 = 0
            empates = 0
            tempo_total_1 = 0
            tempo_total_2 = 0
            nos_total_1 = 0
            nos_total_2 = 0
            
            for partida in range(numero_partidas):
                if partida % 2 == 0:
                    # Partida par: algoritmo 1 com brancas
                    estrategia_brancas = algoritmos[nome1]
                    estrategia_pretas = algoritmos[nome2]
                else:
                    # Partida ímpar: algoritmo 2 com brancas
                    estrategia_brancas = algoritmos[nome2]
                    estrategia_pretas = algoritmos[nome1]
                
                jogo = JogoDamas(
                    estrategia_brancas=estrategia_brancas,
                    estrategia_pretas=estrategia_pretas,
                    exibir_tabuleiro=False,
                    limite_jogadas=200
                )
                
                vencedor = jogo.jogar()
                resumo = jogo.obter_resumo_partida()
                
                # Determinar vencedor do confronto
                if vencedor is None:
                    empates += 1
                elif (partida % 2 == 0 and vencedor == CorPeca.BRANCA) or \
                     (partida % 2 == 1 and vencedor == CorPeca.PRETA):
                    vitorias_1 += 1
                else:
                    vitorias_2 += 1
                
                # Acumular estatísticas
                stats_brancas = resumo['estatisticas_jogadores']['branca']
                stats_pretas = resumo['estatisticas_jogadores']['preta']
                
                if partida % 2 == 0:
                    # Algoritmo 1 com brancas
                    if stats_brancas:
                        tempo_total_1 += sum(s['tempo_execucao'] for s in stats_brancas)
                        nos_total_1 += sum(s['nos_explorados'] for s in stats_brancas)
                    if stats_pretas:
                        tempo_total_2 += sum(s['tempo_execucao'] for s in stats_pretas)
                        nos_total_2 += sum(s['nos_explorados'] for s in stats_pretas)
                else:
                    # Algoritmo 2 com brancas
                    if stats_brancas:
                        tempo_total_2 += sum(s['tempo_execucao'] for s in stats_brancas)
                        nos_total_2 += sum(s['nos_explorados'] for s in stats_brancas)
                    if stats_pretas:
                        tempo_total_1 += sum(s['tempo_execucao'] for s in stats_pretas)
                        nos_total_1 += sum(s['nos_explorados'] for s in stats_pretas)
            
            # Registrar resultados
            confronto = f"{nome1}_vs_{nome2}"
            resultados[confronto] = {
                'vitorias_1': vitorias_1,
                'vitorias_2': vitorias_2,
                'empates': empates,
                'tempo_medio_1': tempo_total_1 / numero_partidas if numero_partidas > 0 else 0,
                'tempo_medio_2': tempo_total_2 / numero_partidas if numero_partidas > 0 else 0,
                'nos_medio_1': nos_total_1 / numero_partidas if numero_partidas > 0 else 0,
                'nos_medio_2': nos_total_2 / numero_partidas if numero_partidas > 0 else 0
            }
            
            print(f"  {nome1}: {vitorias_1} vitórias")
            print(f"  {nome2}: {vitorias_2} vitórias")
            print(f"  Empates: {empates}")
            print(f"  Tempo médio - {nome1}: {tempo_total_1/numero_partidas:.3f}s, "
                  f"{nome2}: {tempo_total_2/numero_partidas:.3f}s")
            print()
    
    return resultados


def executar_analise_profundidade():
    """Analisa o desempenho dos algoritmos em diferentes profundidades."""
    print("=== ANÁLISE DE PROFUNDIDADE ===")
    print("Comparando desempenho dos algoritmos em diferentes profundidades...")
    print()
    
    # TODO: Implementar quando os algoritmos estiverem prontos
    print("Esta funcionalidade será implementada após completar os algoritmos TODO.")
    print("Ela comparará:")
    print("- Tempo de execução vs profundidade")
    print("- Qualidade das jogadas vs profundidade")  
    print("- Número de nós explorados vs profundidade")
    print("- Eficiência da poda alfa-beta")


def jogar_contra_humano():
    """Permite que um humano jogue contra a IA."""
    print("=== JOGO HUMANO vs IA ===")
    print()
    
    print("Escolha a dificuldade da IA:")
    print("1. Fácil (Jogador Aleatório)")
    print("2. Médio (MiniMax profundidade 3) - TODO")
    print("3. Difícil (Poda Alfa-Beta profundidade 4) - TODO")
    print("4. Expert (Poda Alfa-Beta profundidade 6) - TODO")
    
    while True:
        try:
            escolha = int(input("Digite sua escolha (1-4): "))
            if 1 <= escolha <= 4:
                break
            else:
                print("Escolha inválida! Digite um número entre 1 e 4.")
        except ValueError:
            print("Por favor, digite um número válido!")
    
    # Configurar IA baseada na escolha
    if escolha == 1:
        ia = JogadorAleatorio()
        nivel = "Fácil"
    else:
        # TODO: Implementar quando os algoritmos estiverem prontos
        print(f"Dificuldade {escolha} ainda não implementada. Usando nível fácil.")
        ia = JogadorAleatorio()
        nivel = "Fácil"
    
    print(f"\nVocê jogará com as peças brancas contra IA nível {nivel}")
    print("Para fazer um movimento, digite o número correspondente quando solicitado.")
    print()
    
    jogo = JogoDamas(
        estrategia_brancas=JogadorHumano(),
        estrategia_pretas=ia,
        exibir_tabuleiro=True,
        limite_jogadas=300
    )
    
    vencedor = jogo.jogar()
    
    if vencedor == CorPeca.BRANCA:
        print("🎉 Parabéns! Você venceu!")
    elif vencedor == CorPeca.PRETA:
        print("😞 A IA venceu! Tente novamente.")
    else:
        print("🤝 Empate! Bom jogo!")


def executar_teste_desempenho():
    """Executa testes de desempenho dos algoritmos."""
    print("=== TESTE DE DESEMPENHO ===")
    print("Executando testes de desempenho com diferentes configurações...")
    print()
    
    # TODO: Implementar quando os algoritmos estiverem prontos
    configuracoes = [
        # {'algoritmo': MiniMax, 'profundidade': 3, 'nome': 'MiniMax-3'},
        # {'algoritmo': MiniMax, 'profundidade': 4, 'nome': 'MiniMax-4'},
        # {'algoritmo': PodaAlfaBeta, 'profundidade': 3, 'nome': 'AlfaBeta-3'},
        # {'algoritmo': PodaAlfaBeta, 'profundidade': 4, 'nome': 'AlfaBeta-4'},
        {'algoritmo': JogadorAleatorio, 'profundidade': 1, 'nome': 'Aleatório'}
    ]
    
    for config in configuracoes:
        print(f"Testando {config['nome']}...")
        
        if config['algoritmo'] == JogadorAleatorio:
            estrategia = JogadorAleatorio()
        else:
            # TODO: Implementar quando os algoritmos estiverem prontos
            continue
        
        # Executar algumas partidas para medir desempenho
        tempo_total = 0
        nos_total = 0
        partidas_teste = 5
        
        for i in range(partidas_teste):
            jogo = JogoDamas(
                estrategia_brancas=estrategia,
                estrategia_pretas=JogadorAleatorio(),
                exibir_tabuleiro=False,
                limite_jogadas=100
            )
            
            inicio = time.time()
            jogo.jogar()
            tempo_partida = time.time() - inicio
            
            resumo = jogo.obter_resumo_partida()
            stats_brancas = resumo['estatisticas_jogadores']['branca']
            
            tempo_total += tempo_partida
            if stats_brancas:
                nos_total += sum(s['nos_explorados'] for s in stats_brancas)
        
        print(f"  Tempo médio por partida: {tempo_total/partidas_teste:.3f}s")
        print(f"  Nós explorados médios: {nos_total/partidas_teste:.0f}")
        print()


def salvar_configuracao_experimento():
    """Salva uma configuração de experimento para reprodução posterior."""
    print("=== CONFIGURAÇÃO DE EXPERIMENTO ===")
    print("Salvando configuração padrão de experimento...")
    
    import json
    from datetime import datetime
    
    configuracao = {
        'data_criacao': datetime.now().isoformat(),
        'versao': '1.0',
        'algoritmos': {
            'minimax': {
                'implementado': False,
                'profundidades_teste': [3, 4, 5],
                'descricao': 'Algoritmo MiniMax clássico'
            },
            'alfa_beta': {
                'implementado': False,
                'profundidades_teste': [3, 4, 5, 6],
                'descricao': 'MiniMax com poda Alfa-Beta'
            },
            'expect_minimax': {
                'implementado': False,
                'profundidades_teste': [3, 4],
                'probabilidades_erro': [0.1, 0.2],
                'descricao': 'MiniMax esperado para oponentes imperfeitos'
            }
        },
        'configuracoes_teste': {
            'partidas_por_confronto': 20,
            'limite_jogadas': 200,
            'timeout_por_jogada': 30.0,
            'salvar_historicos': True
        },
        'metricas_avaliacao': [
            'taxa_vitoria',
            'tempo_medio_jogada',
            'nos_explorados_medio',
            'profundidade_media_alcancada',
            'qualidade_movimentos'
        ]
    }
    
    with open('configuracao_experimento.json', 'w', encoding='utf-8') as f:
        json.dump(configuracao, f, indent=2, ensure_ascii=False)
    
    print("Configuração salva em: configuracao_experimento.json")
    print("Use esta configuração como base para seus experimentos!")


def exibir_menu():
    """Exibe o menu principal."""
    print("\n" + "="*50)
    print("    JOGO DE DAMAS - BUSCA COMPETITIVA")
    print("="*50)
    print()
    print("1. Executar partida simples (demo)")
    print("2. Torneio entre algoritmos")
    print("3. Análise de profundidade")
    print("4. Jogar contra IA")
    print("5. Teste de desempenho")
    print("6. Salvar configuração de experimento")
    if VISUAL_DISPONIVEL:
        print("7. 🎮 Jogar na interface visual")
    else:
        print("7. 🎮 Interface visual (pygame não instalado)")
    print("0. Sair")
    print()


def jogar_interface_visual():
    """Executa jogo na interface gráfica."""
    if not VISUAL_DISPONIVEL:
        print("❌ Interface visual não disponível!")
        print("   Instale pygame com: pip install pygame")
        return
    
    print("=== INTERFACE VISUAL ===")
    print("Escolha o tipo de partida:")
    print("1. Humano vs Humano")
    print("2. Humano vs IA (Aleatória)")
    print("3. IA vs IA (Demonstração)")
    
    while True:
        try:
            escolha = int(input("Digite sua escolha (1-3): "))
            if 1 <= escolha <= 3:
                break
            else:
                print("Escolha inválida! Digite um número entre 1 e 3.")
        except ValueError:
            print("Por favor, digite um número válido!")
    
    # Configurar estratégias baseado na escolha
    if escolha == 1:
        estrategia_brancas = JogadorHumano()
        estrategia_pretas = JogadorHumano()
        print("Partida: Humano vs Humano")
    elif escolha == 2:
        print("Você jogará com as peças brancas.")
        estrategia_brancas = JogadorHumano()
        estrategia_pretas = JogadorAleatorio()
        print("Partida: Humano vs IA")
    else:
        estrategia_brancas = JogadorAleatorio()
        estrategia_pretas = JogadorAleatorio()
        print("Partida: IA vs IA (demonstração)")
    
    try:
        print("\n🎮 Iniciando interface gráfica...")
        print("   Use o mouse para interagir!")
        print("   Pressione 'H' no jogo para ver ajuda completa.")
        
        jogo_visual = JogoVisual()
        vencedor = jogo_visual.executar_partida(estrategia_brancas, estrategia_pretas)
        
        if vencedor:
            print(f"\n🏆 Partida finalizada! Vencedor: {vencedor.value}")
        else:
            print("\n⏹️  Jogo fechado pelo usuário.")
        
        jogo_visual.fechar()
        
    except Exception as e:
        print(f"❌ Erro na interface visual: {e}")
        print("   Verifique se pygame está instalado corretamente.")


def main():
    """Função principal com menu interativo."""
    print("Bem-vindo ao sistema de Jogo de Damas com Busca Competitiva!")
    print("Desenvolvido para o núcleo de Inteligência Artificial")
    print()
    print("⚠️  ATENÇÃO: Os algoritmos MiniMax, Poda Alfa-Beta e Expect MiniMax")
    print("   ainda precisam ser implementados nos arquivos TODO!")
    
    while True:
        exibir_menu()
        
        try:
            escolha = input("Digite sua escolha: ").strip()
            
            if escolha == '0':
                print("Obrigado por usar o sistema! Até logo!")
                break
            elif escolha == '1':
                executar_partida_simples()
            elif escolha == '2':
                numero_partidas = int(input("Número de partidas por confronto (padrão 10): ") or "10")
                executar_torneio_algoritmos(numero_partidas)
            elif escolha == '3':
                executar_analise_profundidade()
            elif escolha == '4':
                jogar_contra_humano()
            elif escolha == '5':
                executar_teste_desempenho()
            elif escolha == '6':
                salvar_configuracao_experimento()
            elif escolha == '7':
                jogar_interface_visual()
            else:
                print("Opção inválida! Tente novamente.")
            
            input("\nPressione Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            print("Tente novamente ou contacte o desenvolvedor.")


if __name__ == "__main__":
    main() 