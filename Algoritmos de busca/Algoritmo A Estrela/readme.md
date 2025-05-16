# Algoritmo A* com Visualização em Pygame

Este projeto implementa o Algoritmo A*, uma técnica de busca heurística amplamente utilizada para encontrar caminhos de custo mínimo em grafos. A implementação ocorre sobre um grid bidimensional com visualização interativa em tempo real, utilizando a biblioteca Pygame. Desenvolvido com fins educacionais, o projeto tem como objetivo ilustrar de forma clara e visual os principais conceitos do A* e sua lógica de funcionamento.

---

## Tabela de Conteúdos

1. Visão Geral  
2. Pré-requisitos  
3. Instalação e Execução  
4. Arquitetura do Código  
   - Classe Noh  
   - Função heuristica  
   - Função algoritmo  
   - Módulo de Visualização (desenhar)  
   - Funções Auxiliares  
5. Controles de Interação  
6. Fundamentos do Algoritmo A*  
   - Definições de `g`, `h` e `f`  
   - Uso de Fila de Prioridade e Critérios de Desempate  
   - Reconstrução do Caminho Ótimo  
7. Propostas de Extensão  

---

## Visão Geral

O algoritmo A* combina os benefícios da busca em largura e da busca gulosa, utilizando uma função heurística para guiar a exploração do espaço de estados. Cada célula do grid representa um nó (classe Noh), que pode assumir diferentes estados visuais:

- Espaço livre: branco  
- Obstáculo: preto  
- Ponto de início: laranja  
- Ponto de destino: turquesa  
- Fronteira (em avaliação): verde  
- Nó processado: vermelho  
- Caminho final encontrado: azul  

Durante a execução, os nós mostram o valor de `f = g + h` para facilitar o acompanhamento das decisões do algoritmo.

## Pré-requisitos

- Python 3.x  
- Biblioteca Pygame  

Para instalar o Pygame, execute:

```bash
    pip install pygame
```

## Instalação e Execução

1. Clone este repositório.  
2. Instale as dependências necessárias.  
3. Execute o script principal:

```bash
    python a_estrela.py
```

Uma janela gráfica de 800×800 pixels será aberta, contendo o grid interativo.

## Arquitetura do Código

### Classe Noh

Modela as células do grid como objetos com os seguintes atributos principais:

- linha, coluna: coordenadas lógicas.  
- x, y: coordenadas em pixels para renderização.  
- largura_altura: dimensões da célula.  
- cor: representa o estado visual atual.  
- vizinhos: lista de nós adjacentes válidos.  
- custo_f: valor de f associado à célula.  

Inclui métodos para gerenciamento de estado visual, desenho na tela e atualização da lista de vizinhos (ignorando obstáculos).

### Função heuristica

Implementa a distância de Manhattan, definida por:

`
    h = |x1 - x2| + |y1 - y2|
`

Essa heurística é apropriada para grids sem movimentação diagonal, pois calcula o custo mínimo estimado até o destino.

### Função algoritmo

Contém a implementação completa do A*:

1. Inicialização:  
   - Inicializa os dicionários `custo_g` e `custo_f` com valores infinitos.  
   - Define `custo_g[inicio] = 0` e `calcula custo_f[inicio]` usando a heurística.  
   - Insere o nó inicial em uma fila de prioridade com ordenação baseada em `f`.  
   - Utiliza um conjunto auxiliar para otimizar buscas na fila.

2. Execução Iterativa:  
   - Processa o nó com menor valor de `f`.  
   - Se o destino for alcançado, aciona a reconstrução do caminho.  
   - Para cada vizinho do nó atual:  
       - Calcula o custo alternativo `custo_g_temp`.  
       - Se esse custo for menor, atualiza os valores em `custo_g`, `custo_f` e no dicionário `veio_de`.  
       - Adiciona o vizinho à fila, se ainda não estiver presente, e atualiza sua representação gráfica.  
   - Atualiza visualmente o grid a cada iteração.

3. Finalização:  
   - Retorna `False` caso não exista caminho viável até o destino.

### Módulo de Visualização (desenhar)

Responsável por limpar e redesenhar toda a janela, incluindo as células do grid e as linhas que definem a malha. Atualiza dinamicamente a interface conforme o algoritmo é executado.

### Funções Auxiliares

- `criar_grid()`: gera uma matriz de objetos `Noh`.  
- `desenhar_grid()`: traça as linhas da malha.  
- `pegar_pos_clicada()`: traduz a posição do mouse para uma célula do grid.  
- `main()`: função principal de controle de eventos e lógica de interação:  
    - Clique esquerdo: define início, fim ou obstáculos.  
    - Clique direito: remove marcações.  
    - Clique do meio: limpa completamente o grid, removendo início, fim e obstáculos.  
    - Tecla SPACE: inicia a execução do A*.

## Controles de Interação

- Clique esquerdo: define o ponto de início (primeiro), o destino (segundo) e, em seguida, obstáculos.  
- Clique direito: remove qualquer marcação da célula.  
- Clique do meio: limpa completamente o grid, removendo início, fim e obstáculos.  
- Barra de espaço (SPACE): inicia o algoritmo A*.  
- Fechamento da janela: encerra o programa.

## Fundamentos do Algoritmo A*

### Definições de g, h e f

- `g(n)`: custo acumulado desde o início até o nó `n`.  
- `h(n)`: estimativa do custo restante de `n` até o destino.  
- `f(n) = g(n) + h(n)`: custo total estimado passando por`n`. O algoritmo sempre prioriza nós com menor valor de `f`.

### Uso de Fila de Prioridade e Critérios de Desempate

A fila de prioridade é baseada em tuplas (`f`, `contador`), onde `contador` é um valor incremental usado para evitar ambiguidades em empates entre nós com o mesmo f. Essa estratégia assegura comportamento determinístico e estável.

### Reconstrução do Caminho Ótimo

Após atingir o destino, a função reconstruir_caminho percorre o dicionário veio_de de trás para frente, refazendo o trajeto ótimo até o ponto de início. As células do caminho são destacadas em azul para visualização.

---

## Propostas de Extensão

- Exibir os valores de `g` e `h` individualmente em cada célula (ex.: `g|h`).  
- Permitir movimentação diagonal, com ajustes na heurística utilizada.  
- Atribuir diferentes pesos a terrenos variados.  
- Incluir animações para a reconstrução do caminho encontrado.

---

> Nota: Este projeto tem caráter educativo e visa reforçar a compreensão de algoritmos de busca e visualização computacional. Sinta-se livre para modificar, aprimorar a interface e explorar novas funcionalidades!
