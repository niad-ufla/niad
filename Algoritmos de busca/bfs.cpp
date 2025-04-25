#include <iostream>
#include <queue>
#include <vector>

struct Node {
    int value;
    std::vector<Node*> children;
    Node(int val) : value(val) {}
};

void bfs(Node* root) {
    std::queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        Node* current = q.front();
        q.pop();
        std::cout << current->value << " ";

        for (Node* child : current->children) {
            q.push(child);
        }
    }
}

int main() {
    Node* root = new Node(1);
    root->children = {new Node(2), new Node(3), new Node(4)};
    root->children[0]->children = {new Node(5), new Node(6)};
    root->children[2]->children = {new Node(7)};

    std::cout << "BFS traversal: ";
    bfs(root);
    std::cout << std::endl;

    return 0;
}