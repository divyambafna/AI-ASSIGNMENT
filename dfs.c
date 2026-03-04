#include <stdio.h>
#include <stdlib.h>

#define MAX 10

void DFS(int adj[MAX][MAX], int visited[MAX], int start, int n) {
    printf("%d ", start);
    visited[start] = 1;

    for (int i = 0; i < n; i++) {
        if (adj[start][i] == 1 && !visited[i]) {
            DFS(adj, visited, i, n);
        }
    }
}

int main() {
    int n, start_node;
    int adj[MAX][MAX];
    int visited[MAX] = {0};

    printf("Enter the number of nodes (max %d): ", MAX);
    scanf("%d", &n);

    printf("Enter the adjacency matrix (0 or 1):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &adj[i][j]);
        }
    }

    printf("Enter the starting node: ");
    scanf("%d", &start_node);

    if (start_node >= n || start_node < 0) {
        printf("Invalid starting node.\n");
        return 1;
    }

    printf("DFS Traversal: ");
    DFS(adj, visited, start_node, n);
    printf("\n");

    return 0;
}
