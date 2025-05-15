#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Estrutura para representar uma aresta: destino e peso
struct Aresta {
    int destino;
    int peso;
    
    Aresta(int d, int p) : destino(d), peso(p) {}
};

// Função para encontrar o caminho mínimo usando o Algoritmo de Dijkstra
void dijkstra(int origem, int n, vector<vector<Aresta>>& grafo) {
    // Vetor para armazenar a distância mínima de cada cidade (inicialmente infinita)
    vector<int> dist(n, INT_MAX);
    dist[origem] = 0; // A distância da origem até ela mesma é 0

    // Fila de prioridade (min-heap) para pegar a cidade com a menor distância
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, origem}); // Insere a cidade de origem com distância 0

    while (!pq.empty()) {
        // Pega o vértice com a menor distância
        int u = pq.top().second; 
        int d = pq.top().first;
        pq.pop();

        // Se a distância já foi atualizada, ignoramos
        if (d > dist[u]) continue;

        // Verifica todos os vizinhos (arestas) de u
        for (const Aresta& aresta : grafo[u]) {
            int v = aresta.destino;
            int peso = aresta.peso;

            // Se o caminho até v for mais curto passando por u, atualiza a distância
            if (dist[u] + peso < dist[v]) {
                dist[v] = dist[u] + peso;
                pq.push({dist[v], v}); // Insere v na fila de prioridade
            }
        }
    }

    // Imprime as distâncias mínimas de origem a todas as cidades
    cout << "Distâncias mínimas a partir da cidade " << origem << ":\n";
    for (int i = 0; i < n; i++) {
        cout << "Cidade " << i << ": " << dist[i] << endl;
    }
}

int main() {
    int n = 5; // Número de cidades
    vector<vector<Aresta>> grafo(n); // Grafo representado como uma lista de adjacência

    // Definindo as estradas entre as cidades (Arestas)
    grafo[0].push_back(Aresta(1, 1)); // A -> B (distância 1)
    grafo[0].push_back(Aresta(2, 4)); // A -> C (distância 4)
    grafo[1].push_back(Aresta(2, 2)); // B -> C (distância 2)
    grafo[1].push_back(Aresta(3, 5)); // B -> D (distância 5)
    grafo[2].push_back(Aresta(4, 3)); // C -> E (distância 3)
    grafo[3].push_back(Aresta(4, 1)); // D -> E (distância 1)

    int origem = 0; // Cidade A (índice 0)
    dijkstra(origem, n, grafo); // Chamando a função de Dijkstra

    return 0;
}
