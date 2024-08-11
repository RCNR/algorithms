// 2448
#include <bits/stdc++.h>

using namespace std;

// const int MAX = 1024 * 3 + 3;

char board[3100][6200];

void star(int x, int y) {
    board[x][y] = '*';
    board[x+1][y+1] = '*';
    board[x+1][y-1] = '*';

    for(int i = y-2; i <= y+2; i++) board[x+2][i] = '*';
}

void func(int n, int x, int y) {
    if(n==3) {
        star(x, y);
        return;
    }

    int k = n/2;
    func(k, x, y); // 중앙
    func(k, x+k, y-k); // 왼쪽
    func(k, x+k, y+k); // 오른쪽
}

int main() {
    cin.tie(0); cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n;
    cin >> n;   

    func(n, 0, n-1);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < 2*n-1; j++) {
            if(board[i][j] == '*') cout << '*';
            else cout << ' ';
        }
        cout << '\n';
    }
    
}