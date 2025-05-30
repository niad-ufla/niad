#!/usr/bin/env python3
"""
Demonstração da Interface Visual do Jogo de Damas

Este arquivo demonstra como usar a interface gráfica do jogo de damas.
Execute este arquivo para testar a interface visual.
"""

def main():
    """Função principal para demonstrar a interface visual."""
    print("=" * 60)
    print("    DEMONSTRAÇÃO - INTERFACE VISUAL JOGO DE DAMAS")
    print("=" * 60)
    print()
    
    # Verificar se pygame está disponível
    try:
        import pygame
        print("✅ Pygame encontrado! Versão:", pygame.version.ver)
    except ImportError:
        print("❌ ERRO: Pygame não está instalado!")
        print()
        print("Para instalar pygame:")
        print("  pip install pygame")
        print("  ou")
        print("  pip install -r requirements.txt")
        print()
        input("Pressione Enter para sair...")
        return
    
    print("🎮 Iniciando demonstração da interface visual...")
    print()
    print("TIPOS DE PARTIDA DISPONÍVEIS:")
    print("1. Humano vs IA (você controla as peças brancas)")
    print("2. IA vs IA (demonstração automática)")
    print()
    
    escolha = input("Escolha o tipo (1 ou 2, Enter para padrão=1): ").strip()
    if not escolha:
        escolha = "1"
    
    try:
        from visual import JogoVisual
        from exercicios.algoritmos_busca import JogadorHumano, JogadorAleatorio
        
        if escolha == "2":
            print("🤖 Demonstração IA vs IA iniciando...")
            print("   Observe os algoritmos jogando automaticamente!")
            estrategia_brancas = JogadorAleatorio()
            estrategia_pretas = JogadorAleatorio()
        else:
            print("👤 Você jogará com as peças brancas contra a IA!")
            print("   Use o mouse para selecionar e mover as peças.")
            estrategia_brancas = JogadorHumano()
            estrategia_pretas = JogadorAleatorio()
        
        print()
        print("CONTROLES DA INTERFACE:")
        print("  🖱️  Clique nas peças para selecioná-las")
        print("  🖱️  Clique no destino para mover")
        print("  ⌨️  R = Reiniciar jogo")
        print("  ⌨️  H = Mostrar ajuda")
        print("  ⌨️  ESC = Sair")
        print()
        print("Preparando interface...")
        
        # Criar e executar jogo visual
        jogo_visual = JogoVisual(largura=800, altura=950)
        vencedor = jogo_visual.executar_partida(estrategia_brancas, estrategia_pretas)
        
        # Mostrar resultado
        print()
        if vencedor:
            print(f"🏆 Resultado: {vencedor.value.title()} venceu!")
            if vencedor.value == "branca" and escolha == "1":
                print("🎉 Parabéns! Você venceu!")
            elif vencedor.value == "preta" and escolha == "1":
                print("😅 A IA venceu! Tente novamente.")
        else:
            print("⏹️  Jogo encerrado pelo usuário.")
        
        jogo_visual.fechar()
        
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        print("   Verifique se todos os módulos estão disponíveis.")
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        print("   Verifique se pygame está funcionando corretamente.")
    
    print()
    input("Pressione Enter para finalizar...")


if __name__ == "__main__":
    main() 