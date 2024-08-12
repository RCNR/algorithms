// 15989
// 쉬워보임 -> 착각
// 관찰 그리고 생각 -> 1로만, 1~2로만, 1~3로만 관찰, 생각...

#include <bits/stdc++.h>

using namespace std;

int board[10002][4];

int main() {
    int n;
    cin >> n;

    while(n--) {
        memset(board, 0, sizeof(board));
        int num; cin >> num;
        board[1][1] = 1; board[1][2] = 1; board[1][3] = 1;
        board[2][1] = 1; board[2][2] = 2; board[2][3] = 2;
        board[3][1] = 1; board[3][2] = 2; board[3][3] = 3;

        for(int i = 4; i <= num; i++) {
            board[i][1] = board[i-1][1];
            board[i][2] = i/2 + 1;
            board[i][3] = board[i-1][1] + board[i-2][2] + board[i-3][3];
        }

        cout << board[num][3] << '\n';
    }
}
