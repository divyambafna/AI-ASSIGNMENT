#include <stdio.h>
#include <stdbool.h>

char board[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};

int check_winner() {
    int wins[8][3] = {{0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}};
    for(int i = 0; i < 8; i++) {
        if(board[wins[i][0]] != ' ' && board[wins[i][0]] == board[wins[i][1]] && board[wins[i][0]] == board[wins[i][2]])
            return (board[wins[i][0]] == 'X') ? 10 : -10;
    }
    return 0;
}

int is_full() {
    for(int i = 0; i < 9; i++) if(board[i] == ' ') return 0;
    return 1;
}

int minimax(bool isMax) {
    int score = check_winner();
    if (score == 10 || score == -10) return score;
    if (is_full()) return 0;

    if (isMax) {
        int best = -1000;
        for (int i = 0; i < 9; i++) {
            if (board[i] == ' ') {
                board[i] = 'X';
                int val = minimax(false);
                if (val > best) best = val;
                board[i] = ' ';
            }
        }
        return best;
    } else {
        int best = 1000;
        for (int i = 0; i < 9; i++) {
            if (board[i] == ' ') {
                board[i] = 'O';
                int val = minimax(true);
                if (val < best) best = val;
                board[i] = ' ';
            }
        }
        return best;
    }
}

int main() {
    board[0] = 'X'; board[1] = 'O'; board[2] = 'X';
    board[3] = 'O'; board[4] = 'O';
    
    int result = minimax(true);
    printf("Optimal Value: %d\n", result);
    return 0;
}