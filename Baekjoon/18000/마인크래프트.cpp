// 18111 마인크래프트
// 모두 평지로 만들어야함. 높이는 0 ~ 256
// 블록 늘리면 +1, 블록 줄이면 +2
// 인벤토리의 -, +
// 256 x O(N) x O(M) ------ 최대 연산 횟수 257 x (500 x 500)

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

int board[505][505];

int main() {
    FAST_IO;

    int n, m, block;
    cin >> n >> m >> block;
    rep(i, 0, n) {
        rep(j, 0, m) {
            cin >> board[i][j];
        }
    }
    vector<pii> v;

    for (int height = 0; height <= 256; height++) {
        int time = 0;
        int check = height;
        int cnt = block;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int res = board[i][j] - height;
                if (res < 0) { // 블록 늘리기
                    time += abs(res);
                    cnt -= abs(res);
                }
                else if (res > 0) { // 블록 줄이기
                    time += abs(res) * 2;
                    cnt += abs(res);
                }
            }
        }
        if (cnt >= 0) v.pb({ time, height});
    }
    sort(v.begin(), v.end());


    vector<pair<int, int>> vv; // 같은 시간일 때 땅의 높이가 가장 높은 것 땜에 추가
    vv.push_back({ v[0].X, v[0].Y });
    rep(i, 1, v.size()) {
        if (v[0].X == v[i].X) {
            vv.push_back({v[i].X, v[i].Y});
        }
    }
    int siz = vv.size();
    cout << vv[siz - 1].X << ' ' << vv[siz - 1].Y;
    return 0;
}
