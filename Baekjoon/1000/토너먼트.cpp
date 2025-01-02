// 1057 토너먼트
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

    int n, a, b; // 인원, 김지민, 임한수
    cin >> n >> a >> b;
    int cnt = 0;
    while (a != b) {
        //n = (n + 1) / 2; // 다음 토너먼트 하는 횟수
        a = (a + 1) / 2;
        b = (b + 1) / 2;
        cnt++;
    }
    cout << cnt;    
    return 0;
}
