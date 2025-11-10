/*
  행렬 제곱.cpp 10830
  거듭제곱 연산과 행렬 곱셈을 이용한 문제, 분할하기
*/

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

ll board[5][5];
ll ans[5][5];
ll tmp[5][5];
ll N, B;

void check(ll a[5][5], ll b[5][5]) {

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            tmp[i][j] = 0;

            for (int k = 0; k < N; k++) {
                tmp[i][j] += (a[i][k] * b[k][j]);
            }

            tmp[i][j] %= 1000;
        }
    }

    rep(i, 0, N) {
        rep(j, 0, N) {
            a[i][j] = tmp[i][j];
        }
    }
}

int main() {
    FAST_IO;
    
    cin >> N >> B;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
        ans[i][i] = 1; // 단위행렬로
    }

    while (B > 0) {
        if (B % 2 == 1) check(ans, board); // 홀수면 한번 더 ans에 곱해줘함 a^5 = a^4 * a
        check(board, board); // a^2 * a^2 = a^4
        B = B / 2;
    }

    rep(i, 0, N) {
        rep(j, 0, N) {
            cout << ans[i][j] << ' ';
        }
        cout << endl;
    }
    
    return 0;
}
