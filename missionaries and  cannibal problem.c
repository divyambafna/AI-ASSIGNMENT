#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int m, c, b;
    int parent_idx;
} State;

State queue[200];
bool visited[4][4][2];
int head = 0, tail = 0;

bool is_valid(int m, int c) {
    if (m < 0 || m > 3 || c < 0 || c > 3) return false;
    if (m > 0 && m < c) return false;
    if (3 - m > 0 && (3 - m) < (3 - c)) return false;
    return true;
}

void solve() {
    State start = {3, 3, 1, -1};
    queue[tail++] = start;
    visited[3][3][1] = true;

    int moves[5][2] = {{1,0}, {2,0}, {0,1}, {0,2}, {1,1}};

    while (head < tail) {
        State current = queue[head++];

        if (current.m == 0 && current.c == 0 && current.b == 0) {
            printf("Goal Reached: 0, 0, 0\n");
            return;
        }

        for (int i = 0; i < 5; i++) {
            int nm, nc, nb;
            if (current.b == 1) {
                nm = current.m - moves[i][0];
                nc = current.c - moves[i][1];
                nb = 0;
            } else {
                nm = current.m + moves[i][0];
                nc = current.c + moves[i][1];
                nb = 1;
            }

            if (is_valid(nm, nc) && !visited[nm][nc][nb]) {
                visited[nm][nc][nb] = true;
                State next = {nm, nc, nb, head - 1};
                queue[tail++] = next;
            }
        }
    }
}

int main() {
    solve();
    return 0;
}