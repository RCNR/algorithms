#include <bits/stdc++.h>
#define rep(i,a,n) for(auto i=a; i<n; i++)
#define REP(i,a,n) for(auto i=a; i<=n; i++)
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL), cout.tie(NULL)

typedef long long ll;

using namespace std;

long long sum[1'000'003];

int main() {

    FAST_IO;

    // 1 2 3 1 2
    // 1 3 6 7 9
    // % 3
    // 1 0 0 1 0
    // (A+B+C)%D = ((A%D)+(B%D)+(C%D)) % D

    int n, m;
    cin >> n >> m;

    REP(i, 1, n) {
        int num; cin >> num;
        sum[i] = num + sum[i-1];
    }

    REP(i, 1, n) {
        sum[i] = sum[i] % m;
    }

    vector<ll> v;
    v.resize(m);

    ll cnt = 0;

    REP(i, 1, n) {
        if(sum[i] == 0) cnt++;
        v[sum[i]]++;
    }

    rep(i, 0, m) {
        if(v[i] >= 2) {
            cnt += (v[i] * (v[i] - 1)) / 2;
        }
    }
    cout << cnt;
}