// 14215 세 막대
#include <bits/stdc++.h>
#define rep(i, a, n) for (auto i = a; i < n; i++)
#define REP(i, a, n) for (auto i = a; i <= n; i++)
#define pb push_back
#define endl "\n"
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long
#define ull unsigned long long
#define pii pair<int, int>
#define X first
#define Y second
#define all(v) (v).begin(), (v).end()
#define PIV (1 << 20)

using namespace std;

int main() {
    FAST_IO;

    // 두 변의 길이의 합이 나머지 변의 길이보다 커야함
    int board[3];
    rep(i, 0, 3) {
        cin >> board[i];
    }

    sort(board, board + 3);
    
    if (board[0] + board[1] <= board[2]) {
        int check = board[2] - (board[0] + board[1]) + 1;
        board[2] = board[2] - check;
    }
    cout << board[0] + board[1] + board[2];

    return 0;
}
