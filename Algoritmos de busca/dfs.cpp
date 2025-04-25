#include <iostream>
#include <vector>

struct Node {
    int value;
    std::vector<Node*> children;
    Node(int val) : value(val) {}
};

void dfs(Node* node) {
    std::cout << node->value << " ";
    for (Node* child : node->children) {
        dfs(child);
    }
}

int main() {
    Node* root = new Node(1);
    root->children = {new Node(2), new Node(3), new Node(4)};
    root->children[0]->children = {new Node(5), new Node(6)};
    root->children[2]->children = {new Node(7)};

    std::cout << "DFS traversal: ";
    dfs(root);
    std::cout << std::endl;

    return 0;
}