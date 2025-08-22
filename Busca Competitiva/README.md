# Jogo de Damas - Busca Competitiva

## 📋 Descrição

Este projeto implementa um jogo de damas completo em Python com foco em algoritmos de busca competitiva. Foi desenvolvido para o núcleo de Inteligência Artificial como uma prática educativa para aprender e comparar diferentes algoritmos de busca em jogos.

**🎮 NOVO: Interface Visual Disponível!** Use a interface gráfica para uma experiência mais intuitiva.

## 🎯 Objetivos

- **Educativo**: Compreender algoritmos de busca competitiva na prática
- **Comparativo**: Avaliar desempenho entre MiniMax, Poda Alfa-Beta e Expect MiniMax
- **Prático**: Implementar um jogo funcional com interface e análises
- **Visual**: Experiência intuitiva através de interface gráfica com Pygame

## ⚡ Início Rápido

### 1. **Interface Visual (Recomendado)**

```bash
# Instalar pygame
pip install pygame
# ou
pip install -r requirements.txt

# Executar demonstração visual
python visual_demo.py

# Ou usar o menu principal
python main.py
# Escolher opção 7
```

### 2. **Interface de Console**

```bash
# Executar menu principal
python main.py

# Ou demonstração simples
python demo.py
```

## 🏗️ Estrutura do Projeto

```
busca-competitiva/
├── README.md                       # Esta documentação
├── main.py                        # Interface principal completa
├── demo.py                        # Demonstração simples
├── visual_demo.py                 # 🎮 Demonstração visual
├── requirements.txt               # Dependências (pygame)
│
├── jogo_damas/                    # 📦 Lógica Completa - NÃO MODIFICAR
│   ├── __init__.py               # Exportações do pacote
│   ├── peca.py                   # Classes: Peca, CorPeca, TipoPeca
│   ├── tabuleiro.py              # Classe Tabuleiro (regras completas)
│   └── jogo_damas.py             # Classe JogoDamas (coordenação)
│
├── exercicios/                    # 📝 EXERCÍCIOS - IMPLEMENTAR AQUI
│   ├── __init__.py               # Exportações do pacote
│   └── algoritmos_busca.py       # 🔧 TODO: MiniMax, Alfa-Beta, etc.
│
├── visual/                        # 🎮 INTERFACE GRÁFICA
│   ├── __init__.py               # Exportações do pacote visual
│   ├── interface_grafica.py      # Renderização com Pygame
│   └── jogo_visual.py            # Integração jogo + interface
│
└── utils/                         # 🛠️ UTILITÁRIOS
    ├── __init__.py               # Exportações de utilitários
    └── configuracao_experimento.json  # Configurações de teste
```

## 🎮 Interface Visual

### **Características**

- **Tabuleiro gráfico** com peças visuais bonitas
- **Interação por cliques** - selecione e mova peças facilmente
- **Indicadores visuais** para movimentos possíveis
- **Informações em tempo real** (turno, estatísticas, etc.)
- **Suporte a todas as estratégias** (Humano, IA, algoritmos TODO)

### **Controles**

- 🖱️ **Clique** nas peças para selecioná-las
- 🖱️ **Clique** no destino para mover
- ⌨️ **R** = Reiniciar jogo
- ⌨️ **H** = Mostrar ajuda
- ⌨️ **ESC** = Sair do jogo

### **Modos de Jogo Visual**

1. **Humano vs Humano** - Dois jogadores no mesmo computador
2. **Humano vs IA** - Jogue contra algoritmos implementados
3. **IA vs IA** - Observe algoritmos jogando automaticamente

## 📝 Exercícios TODO

### **Localização**: `exercicios/algoritmos_busca.py`

Implemente os seguintes algoritmos (estruturas já fornecidas):

1. **MiniMax** - Algoritmo básico de busca competitiva
2. **Poda Alfa-Beta** - MiniMax otimizado com poda
3. **Expect MiniMax** - Para jogos com elementos estocásticos

### **Exemplo de TODO**:

```python
def minimax_recursivo(self, tabuleiro, profundidade, maximizando):
    # TODO: Implementar algoritmo MiniMax
    # 1. Verificar condições de parada
    # 2. Se maximizando: escolher melhor movimento
    # 3. Se minimizando: escolher pior movimento para o oponente
    # 4. Chamar recursivamente para próxima profundidade
    pass
```

## 🚀 Como Usar

### **1. Menu Principal** (7 opções)

```bash
python main.py
```

- Partidas simples e torneios
- Análise de desempenho
- **Interface visual interativa**
- Testes e configurações

### **2. Demonstração Visual**

```bash
python visual_demo.py
```

- Teste rápido da interface gráfica
- Escolha Humano vs IA ou IA vs IA

### **3. Implementar Algoritmos**

1. Abra `exercicios/algoritmos_busca.py`
2. Encontre as classes com TODO
3. Implemente os métodos seguindo as instruções
4. Teste usando menu principal ou interface visual

## 🔧 Instalação e Dependências

### **Requisitos Mínimos**

- Python 3.7+
- Pygame 2.5+ (apenas para interface visual)

### **Instalação**

```bash
# Clonar/baixar projeto
cd busca-competitiva

# Instalar pygame (opcional, apenas para interface visual)
pip install pygame

# Ou usar requirements.txt
pip install -r requirements.txt

# Testar instalação
python demo.py              # Console
python visual_demo.py       # Visual (se pygame instalado)
```

## 📊 Funcionalidades

### **✅ Implementadas**

- ✅ Jogo de damas completo (todas as regras)
- ✅ Sistema de avaliação de posições
- ✅ Jogador Aleatório e Jogador Humano
- ✅ **Interface gráfica com Pygame**
- ✅ **Controles visuais intuitivos**
- ✅ Sistema de torneios e análises
- ✅ Coleta de estatísticas detalhadas
- ✅ Salvamento de partidas em JSON

### **🔧 TODO (Exercícios)**

- 🔧 MiniMax (estrutura pronta)
- 🔧 Poda Alfa-Beta (estrutura pronta)
- 🔧 Expect MiniMax (estrutura pronta)

## 🎯 Experimentos Sugeridos

### **Após Implementar os Algoritmos**

1. **Comparação Visual**

   - Use interface gráfica para observar diferentes estratégias
   - Compare velocidade e qualidade de decisões

2. **Torneios Automáticos**

   - Execute torneios entre algoritmos
   - Analise estatísticas de performance

3. **Análise de Profundidade**
   - Teste diferentes profundidades de busca
   - Observe trade-off tempo vs qualidade

## 🆘 Solução de Problemas

### **Interface Visual não Funciona**

```bash
# Verificar pygame
python -c "import pygame; print('Pygame OK:', pygame.version.ver)"

# Instalar se necessário
pip install pygame

# Testar demo
python visual_demo.py
```

### **Importações Falhando**

- Verifique se está executando do diretório correto
- Use `python main.py` (não `python3`)

### **Performance Lenta**

- Reduza profundidade dos algoritmos durante testes
- Use interface visual para debuggar

## 📚 Para Saber Mais

- **Arquivo de estrutura**: `ESTRUTURA.md`
- **Demonstrações**: `demo.py` e `visual_demo.py`
- **Configurações**: `utils/configuracao_experimento.json`
- **Código TODO**: `exercicios/algoritmos_busca.py`

---

**🎯 Objetivo**: Implemente os algoritmos TODO e use tanto a interface de console quanto a visual para comparar e aprender sobre busca competitiva!

**🎮 Dica**: Comece com a interface visual - é mais divertido e intuitivo para entender o jogo!

## 🎯 Regras do Jogo de Damas

### Movimento

- Peças movem diagonalmente em casas escuras
- Peças normais: apenas para frente
- Damas: qualquer direção diagonal

### Captura

- Obrigatória quando possível
- Salte sobre peça adversária para casa vazia
- Capturas múltiplas são possíveis

### Promoção

- Peça normal vira dama ao chegar na última fileira
- Damas têm maior mobilidade

### Vitória

- Capture todas as peças adversárias, OU
- Bloqueie todos os movimentos do oponente

## 📊 Avaliação do Tabuleiro

A função `avaliar_posicao()` no tabuleiro usa:

- **Peças normais**: 3 pontos
- **Damas**: 10 pontos
- **Posição**: Bônus por avanço
- **Mobilidade**: Bônus por número de movimentos possíveis

Valores positivos favorecem brancas, negativos favorecem pretas.

## 🚀 Guia de Implementação

### Passo 1: Comece com MiniMax Básico

```python
# Em exercicios/algoritmos_busca.py, classe MiniMax
def escolher_movimento(self, tabuleiro, cor_jogador):
    # 1. Obter movimentos possíveis
    # 2. Para cada movimento, avaliar com minimax_recursivo
    # 3. Escolher melhor movimento
```

### Passo 2: Adicione Poda Alfa-Beta

```python
# Similar ao MiniMax, mas com poda quando alfa >= beta
```

### Passo 3: Implemente Expect MiniMax

```python
# Adicione nós de chance para modelar incerteza
```

### Passo 4: Teste e Compare

```python
# Use main.py para comparar seus algoritmos
python main.py  # Opção 2: Torneio
```

## 🔍 Dicas de Debugging

1. **Teste com profundidade baixa** (1-2) primeiro
2. **Use print()** para acompanhar a recursão
3. **Compare com JogadorAleatorio** como baseline
4. **Verifique se está maximizando/minimizando corretamente**
5. **Conte nós explorados** para validar poda

## 📚 Conceitos Importantes

- **MiniMax**: Assume jogo ótimo de ambos os lados
- **Poda Alfa-Beta**: Elimina ramos que não afetam o resultado
- **Expect MiniMax**: Modela incerteza e oponentes imperfeitos
- **Função de Avaliação**: Estima valor de posições não-terminais
- **Horizon Effect**: Problemas de busca com profundidade limitada

## 🤝 Fluxo de Trabalho Recomendado

1. **Estude** a estrutura em `jogo_damas/`
2. **Implemente** algoritmos em `exercicios/`
3. **Teste** com `demo.py` ou `main.py`
4. **Compare** com soluções em `utils/` (apenas no final!)
5. **Experimente** diferentes configurações

## 📄 Licença

Projeto educativo para núcleo de IA. Use livremente para aprendizado.

---

**💡 Dica**: Comece implementando o MiniMax básico, depois parta para a Poda Alfa-Beta. O Expect MiniMax é mais desafiador e pode ser deixado por último.

**⚠️ Importante**: Não consulte `utils/solucao_exemplo.py` até tentar implementar por conta própria!
