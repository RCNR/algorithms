// 1392 노래 악보
#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
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

vector<int> v(100'03);

int main() {
    FAST_IO;

    int n, m;
    int j = 0;
    int st = 0; int idx = 0;
    cin >> n >> m;
    rep(i, 0, n) {
        int num;
        st++;
        cin >> num;
        rep(j, 0, num) {
            v[idx++] = st;
        }
    }

    rep(i, 0, m) {
        int num; cin >> num;
        cout << v[num] << endl;
    }
}

