# 🗺️ Caminho Mínimo em um Mapa de Cidades — Algoritmo de Dijkstra

Este projeto resolve o problema de encontrar o caminho mais curto entre duas cidades em um mapa, utilizando o **Algoritmo de Dijkstra**. O grafo é representado por cidades (vértices) conectadas por estradas com distâncias (arestas ponderadas).

---

## 📌 Descrição do Problema

Dado um conjunto de cidades e as estradas entre elas com seus respectivos comprimentos, queremos encontrar o caminho de menor custo (distância total mínima) entre uma cidade de origem e uma cidade de destino.

### 🔧 Modelagem
- Cada **cidade** é um **vértice** do grafo.
- Cada **estrada** é uma **aresta com peso**, representando a distância entre duas cidades.
- O grafo é direcionado.

---

## 🧾 Entrada

A entrada consiste em:

1. **Número de cidades** (vértices).
2. **Lista de estradas** no formato `(cidade origem, cidade destino, distância)`.
3. **Cidade de origem**.
4. **Cidade de destino**.

---

## 🧪 Exemplo de Entrada

```text
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
