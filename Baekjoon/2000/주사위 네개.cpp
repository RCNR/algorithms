// 2484 -> 많은 조건 분기
// if로 계속하면 너무 많을 거 같아 key, value를 활용해 조금이라도 더 줄일 수 있도록 설정

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

vector<int> money;


void func(int a, int b, int c, int d) {
    map<int, int> m;
    m[a]++;
    m[b]++;
    m[c]++;
    m[d]++;

    int max_num = max({ m[a], m[b], m[c], m[d] });
    vector<pair<int,int>> v;

    for (const auto& pair : m) {
        if (pair.Y == max_num) v.pb({ pair.X, pair.Y });
    }

    sort(v.rbegin(), v.rend());

    if (v[0].Y == 4) money.pb( 50000 + v[0].X * 5000);
    else if (v[0].Y == 3) money.pb( 10000 + v[0].X * 1000);
    else if (v.size() == 2 && v[0].Y == 2) {
        money.pb(2000 + v[0].X * 500 + v[1].X * 500);
    }
    else if (v.size() == 1 && v[0].Y == 2) {
        money.pb(1000 + v[0].X * 100);
    }
    else money.pb(v[0].X * 100);


}

int main() {
    FAST_IO;

    int n;

    cin >> n;

    while (n--) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        func(a, b, c, d);
    }
    sort(money.begin(), money.end());
    cout << money[money.size() - 1];
}

