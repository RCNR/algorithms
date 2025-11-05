// 2775. 부녀회장 -> 2차원 배열, 누적 합 이용

#include<bits/stdc++.h>
#define rep(i, a, n) for(auto i=a; i < n; i++)
#define REP(i, a, n) for(auto i=a; i <= n; i++)
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL), cout.tie(NULL)

using namespace std;

int board[17][17];
int t, k, n;

int main() {
    FAST_IO;

    REP(j, 1, 14) board[0][j] = j;

    REP(i, 1, 14) {
        REP(j, 1, 14) {
            board[i][j] = board[i][j-1] + board[i-1][j]; 
        }
    }

    cin >> t;
    while(t--) {
        cin >> k >> n;
        cout << board[k][n] << '\n';
    }

}