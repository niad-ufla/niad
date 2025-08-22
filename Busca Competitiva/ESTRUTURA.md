# Estrutura Organizacional do Projeto

## 📁 Visão Geral da Reorganização

O projeto foi reorganizado para separar claramente:

- **Lógica Funcional** (não modificar)
- **Exercícios** (implementar)
- **Utilitários** (referência)

## 🏗️ Estrutura Detalhada

```
busca-competitiva/
├── 📄 README.md                    # Documentação principal
├── 📄 ESTRUTURA.md                 # Este arquivo
├── 🚀 main.py                      # Interface completa (menu)
├── 🎮 demo.py                      # Demonstração simples
│
├── 📦 jogo_damas/                  # LÓGICA COMPLETA - NÃO MODIFICAR
│   ├── 📄 __init__.py             # Exportações do pacote
│   ├── 🎯 peca.py                 # Classes: Peca, CorPeca, TipoPeca
│   ├── 🏁 tabuleiro.py            # Classe Tabuleiro (regras completas)
│   └── 🎮 jogo_damas.py           # Classe JogoDamas (coordenação)
│
├── 🔨 exercicios/                  # SEU TRABALHO - IMPLEMENTAR AQUI
│   ├── 📄 __init__.py             # Exportações dos algoritmos
│   └── 🧠 algoritmos_busca.py     # TODO: MiniMax, Alfa-Beta, ExpectMiniMax
│
└── 🔧 utils/                       # UTILITÁRIOS E REFERÊNCIA
    ├── 📄 __init__.py             # Exportações dos utilitários
    ├── 🔒 solucao_exemplo.py      # Soluções completas (não espiar!)
    └── ⚙️ configuracao_experimento.json # Configurações de teste
```

## 📦 Pacote `jogo_damas/` - Lógica Funcional

### Objetivo

Contém toda a implementação funcional do jogo de damas. **Não modifique estes arquivos.**

### Arquivos

#### `peca.py`

- **Classes**: `Peca`, `CorPeca`, `TipoPeca`
- **Funcionalidades**: Representação e manipulação de peças
- **Métodos principais**: `promover_a_dama()`, `mover_para()`, `e_dama()`

#### `tabuleiro.py`

- **Classe**: `Tabuleiro`
- **Funcionalidades**: Regras completas do jogo, movimentos, capturas
- **Métodos principais**:
  - `obter_movimentos_possiveis()`
  - `executar_movimento()`
  - `avaliar_posicao()`
  - `jogo_terminado()`

#### `jogo_damas.py`

- **Classes**: `JogoDamas`, `StatusJogo`
- **Funcionalidades**: Coordenação de partidas, estatísticas, logging
- **Métodos principais**: `jogar()`, `salvar_partida()`

## 🔨 Pacote `exercicios/` - Sua Implementação

### Objetivo

Contém os algoritmos de busca que você deve implementar.

### Arquivo Principal: `algoritmos_busca.py`

#### Classes para Implementar

1. **`MiniMax`**

   ```python
   def escolher_movimento(self, tabuleiro, cor_jogador):
       # TODO: Implementar algoritmo MiniMax

   def minimax_recursivo(self, tabuleiro, profundidade, maximizando, cor_jogador):
       # TODO: Implementar recursão MiniMax
   ```

2. **`PodaAlfaBeta`**

   ```python
   def escolher_movimento(self, tabuleiro, cor_jogador):
       # TODO: Implementar MiniMax com Poda Alfa-Beta

   def alfabeta_recursivo(self, tabuleiro, profundidade, alfa, beta, maximizando, cor_jogador):
       # TODO: Implementar recursão com poda
   ```

3. **`ExpectMiniMax`**

   ```python
   def escolher_movimento(self, tabuleiro, cor_jogador):
       # TODO: Implementar Expect MiniMax

   def expectminimax_recursivo(self, tabuleiro, profundidade, no_chance, cor_jogador):
       # TODO: Implementar recursão com nós de chance
   ```

#### Classes Já Implementadas

1. **`EstrategiaJogo`** - Classe base abstrata
2. **`JogadorAleatorio`** - Para testes e baseline
3. **`JogadorHumano`** - Para jogar manualmente

## 🔧 Pacote `utils/` - Utilitários

### Objetivo

Ferramentas auxiliares e soluções de referência.

### Arquivos

#### `solucao_exemplo.py` 🔒

- **Conteúdo**: Implementações completas dos algoritmos
- **Classes**: `MiniMaxCompleto`, `PodaAlfaBetaCompleta`, `ExpectMiniMaxCompleto`
- **⚠️ AVISO**: Use apenas para comparação após implementar!

#### `configuracao_experimento.json` ⚙️

- **Conteúdo**: Parâmetros para experimentos
- **Uso**: Configurações padronizadas para testes

## 🔄 Fluxo de Importações

### Uso Básico

```python
# Importar jogo completo
from jogo_damas import JogoDamas, Tabuleiro, CorPeca

# Importar seus algoritmos
from exercicios.algoritmos_busca import MiniMax, PodaAlfaBeta, JogadorAleatorio

# Criar partida
jogo = JogoDamas(
    estrategia_brancas=MiniMax(profundidade_maxima=4),
    estrategia_pretas=PodaAlfaBeta(profundidade_maxima=4)
)
```

### Para Comparação (apenas no final!)

```python
# Importar soluções de referência
from utils.solucao_exemplo import MiniMaxCompleto, PodaAlfaBetaCompleta
```

## 🎯 Vantagens desta Organização

### 📚 **Clareza Educativa**

- Separação clara entre código funcional e exercícios
- Estudantes focam apenas no que precisam implementar
- Reduz confusão sobre o que modificar

### 🔒 **Integridade do Código**

- Lógica do jogo protegida contra modificações acidentais
- Testes sempre funcionam com implementação correta
- Facilita debugging de algoritmos

### 📦 **Modularidade**

- Cada pacote tem responsabilidade específica
- Imports claros e organizados
- Fácil extensão e manutenção

### 🧪 **Facilita Experimentos**

- Algoritmos podem ser testados independentemente
- Comparações padronizadas
- Métricas consistentes

## 🚀 Como Começar

### 1. Explore a Estrutura

```bash
# Veja o jogo funcionando
python demo.py

# Explore o menu completo
python main.py
```

### 2. Entenda o Jogo

```python
# Importe e explore
from jogo_damas import Tabuleiro, CorPeca
tabuleiro = Tabuleiro()
print(tabuleiro.exibir())
```

### 3. Implemente Algoritmos

```python
# Edite exercicios/algoritmos_busca.py
# Comece com MiniMax básico
```

### 4. Teste Suas Implementações

```python
# Use demo.py ou main.py para testar
# Compare com JogadorAleatorio
```

### 5. Compare com Soluções (opcional)

```python
# Apenas no final, para verificar
from utils.solucao_exemplo import MiniMaxCompleto
```

## 📋 Checklist de Implementação

- [ ] Implementar `MiniMax.escolher_movimento()`
- [ ] Implementar `MiniMax.minimax_recursivo()`
- [ ] Testar MiniMax vs JogadorAleatorio
- [ ] Implementar `PodaAlfaBeta.escolher_movimento()`
- [ ] Implementar `PodaAlfaBeta.alfabeta_recursivo()`
- [ ] Comparar eficiência: MiniMax vs Alfa-Beta
- [ ] Implementar `ExpectMiniMax.escolher_movimento()`
- [ ] Implementar `ExpectMiniMax.expectminimax_recursivo()`
- [ ] Executar torneio completo entre algoritmos
- [ ] Comparar com soluções de referência

## ❓ Dúvidas Frequentes

### "Posso modificar arquivos em `jogo_damas/`?"

**Não.** Estes arquivos contêm a implementação correta e completa. Modificá-los pode quebrar os testes.

### "Onde estão os TODOs?"

**Em `exercicios/algoritmos_busca.py`.** Todos os TODOs estão claramente marcados com comentários detalhados.

### "Como testar minha implementação?"

**Use `demo.py` ou `main.py`.** Comece testando contra `JogadorAleatorio`.

### "Quando posso ver as soluções?"

**Apenas após implementar.** Use `utils/solucao_exemplo.py` apenas para comparação final.

### "Como comparar eficiência?"

**Use o menu principal.** Opção 2 (Torneio) compara diferentes algoritmos automaticamente.

---

Esta organização foi pensada para maximizar o aprendizado e minimizar a confusão. Foque em implementar os algoritmos em `exercicios/` e use o resto como ferramentas de apoio!
