🗺️ Caminho Mínimo em um Mapa de Cidades — Algoritmo de Dijkstra
Este projeto resolve o problema de encontrar o caminho mais curto entre duas cidades em um mapa, utilizando o Algoritmo de Dijkstra. O grafo é representado por cidades (vértices) conectadas por estradas com distâncias (arestas ponderadas).

📌 Descrição do Problema
Dado um conjunto de cidades e as estradas entre elas com seus respectivos comprimentos, queremos encontrar o caminho de menor custo (distância total mínima) entre uma cidade de origem e uma cidade de destino.

🔧 Modelagem
Cada cidade é um vértice do grafo.

Cada estrada é uma aresta com peso, representando a distância entre duas cidades.

O grafo é direcionado ou não direcionado, dependendo do contexto (neste exemplo, é direcionado).

🧾 Entrada
A entrada consiste em:

Número de cidades (vértices).

Lista de estradas no formato (cidade origem, cidade destino, distância).

Cidade de origem.

Cidade de destino.

🧪 Exemplo de Entrada
text
Copiar
Editar
Cidades: A, B, C, D, E
Representação (índices): A=0, B=1, C=2, D=3, E=4

Estradas:
A -> B (1)
A -> C (4)
B -> C (2)
B -> D (5)
C -> E (3)
D -> E (1)

Origem: A (índice 0)
Destino: E (índice 4)
🎯 Objetivo
Encontrar o caminho mais curto (menor soma das distâncias) entre a cidade A e a cidade E, utilizando o algoritmo de Dijkstra.

💡 Saída Esperada
O programa deve exibir a distância mínima da cidade de origem para todas as outras cidades, como no exemplo abaixo:

text
Copiar
Editar
Distâncias mínimas a partir da cidade 0:
Cidade 0: 0
Cidade 1: 1
Cidade 2: 3
Cidade 3: 6
Cidade 4: 6
No exemplo acima, a menor distância de A até E é 6, passando por A → B → C → E.

⚙️ Tecnologias Utilizadas
Linguagem: C++

Estrutura de Dados: Lista de Adjacência

Algoritmo: Dijkstra com Fila de Prioridade (min-heap)

📚 Conceitos Envolvidos
Grafo ponderado

Lista de adjacência

Fila de prioridade (min-heap)

Algoritmo de Dijkstra

Complexidade: O((V + E) * log V)

🚀 Como Executar
Compile o código:

bash
Copiar
Editar
g++ -o caminho_minimo dijkstra.cpp
Execute:

bash
Copiar
Editar
./caminho_minimo
🧠 Expansões Futuras
Visualização gráfica do grafo.

Leitura de entrada via arquivos.

Interface interativa via terminal.

Suporte a grafos não direcionados.

📎 Referências
Algoritmo de Dijkstra - Wikipédia

Estruturas de Dados e Algoritmos com C++

