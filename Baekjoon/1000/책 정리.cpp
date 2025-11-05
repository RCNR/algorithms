// 1434 책 정리 - 박스마다 루프 돌려서 책 들어갈 수 있는지 확인
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

int box[55];
int book[55];
int n, m;

int main() {
    FAST_IO;
    cin >> n >> m;
    rep(i, 0, n) cin >> box[i];
    rep(i, 0, m) cin >> book[i];
    int idx = 0;
    while (idx != m) {
        int num = book[idx];
        for(int i = 0; i < n; i++) {
            if (box[i] - num >= 0){
                box[i] -= num;
                break;
            }
        }
        idx++;
    }
    ll sum = 0;
    rep(i, 0, n) {
        if (box[i] != 0) {
            sum += box[i];
        }
    }
    cout << sum;

    return 0;
}
