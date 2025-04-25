# Explicação Didática: BFS e DFS em Árvores (C++)

Este repositório contém dois arquivos:

- `bfs.cpp`: Implementação da **Busca em Largura (BFS)** em uma árvore.
- `dfs.cpp`: Implementação da **Busca em Profundidade (DFS)** em uma árvore.

---

## 🌳 Conceito Básico: O que é uma Árvore?

Imagine uma árvore de cabeça para baixo:

- O topo é chamado de **raiz** (root).
- Cada "galho" é um **nó** (node), que pode ter **filhos** (children).
- Um nó pode ter vários filhos, e cada filho também pode ter seus próprios filhos.

---

## 📘 bfs.cpp — Busca em Largura (BFS)

### Objetivo:
Percorrer todos os nós da árvore **nível por nível**, da esquerda para a direita.

### Explicação passo a passo:

```cpp
struct Node {
    int value;
    std::vector<Node*> children;
    Node(int val) : value(val) {}
};
```

- Criamos uma **estrutura Node** para representar cada nó da árvore.
- Cada nó tem um **valor inteiro** e uma **lista de filhos**.

```cpp
void bfs(Node* root) {
    std::queue<Node*> q;
    q.push(root);
```

- Criamos uma **fila (queue)** para organizar os nós que vamos visitar.
- Começamos colocando a raiz na fila.

```cpp
    while (!q.empty()) {
        Node* current = q.front();
        q.pop();
        std::cout << current->value << " ";
```

- Enquanto a fila **não estiver vazia**:
  - Pegamos o nó da frente (com `front()` e `pop()`).
  - Mostramos o valor dele.

```cpp
        for (Node* child : current->children) {
            q.push(child);
        }
    }
```

- Depois colocamos **todos os filhos desse nó na fila**, para visitar eles depois.
- Isso garante que visitamos **nível por nível**, como uma fila de banco.

---

## 📗 dfs.cpp — Busca em Profundidade (DFS)

### Objetivo:
Percorrer todos os nós da árvore **até o fundo** antes de voltar.

### Explicação passo a passo:

```cpp
struct Node {
    int value;
    std::vector<Node*> children;
    Node(int val) : value(val) {}
};
```

- Igual ao BFS, temos uma estrutura de nó com valor e filhos.

```cpp
void dfs(Node* node) {
    std::cout << node->value << " ";
    for (Node* child : node->children) {
        dfs(child);
    }
}
```

- A função `dfs` recebe um nó.
- Primeiro, mostramos o valor do nó.
- Depois, **chamamos a função de novo para cada filho**.
- Isso faz com que a função **vá ao fundo** antes de voltar (como explorar uma caverna até o fim antes de subir).

---

## 🧪 Exemplo de Árvore nos Dois Códigos

Ambos os códigos criam esta árvore:

```
            1
         /  |  \
        2   3   4
       / \      \
      5   6       7
```

- O nó raiz é 1.
- 1 tem filhos: 2, 3, 4
- 2 tem filhos: 5, 6
- 4 tem filho: 7

### Resultado esperado:

- BFS: `1 2 3 4 5 6 7`
- DFS: `1 2 5 6 3 4 7`

---

## 🧠 Dica Final

- Use BFS quando quiser **menor caminho ou percorrer por camadas**.
- Use DFS quando quiser **explorar até o fim primeiro**.

---

Pronto! Agora você entende como andar por uma árvore de duas formas diferentes 🐢🚀