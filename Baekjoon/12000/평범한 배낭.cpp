// 12865 평범한 배낭
// 무게를 인덱스로 설정한다는 게 어렵
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

vector<int> value;
vector<int> weight;
int dp[104][100005];


int main() {
    FAST_IO;
    
    int n, k;
    cin >> n >> k;
    weight.pb(0); value.pb(0);
    rep(i, 0, n) {
        int a, b; cin >> a >> b;
        weight.pb(a);
        value.pb(b);
    }

    REP(i, 1, n) {
        REP(j, 1, k) {
            if (j < weight[i]) dp[i][j] = dp[i - 1][j];
            else {
                dp[i][j] = max(dp[i - 1][j], value[i] + dp[i - 1][j - weight[i]]);
            }
        }
    }

    cout << dp[n][k];
    return 0;
}
