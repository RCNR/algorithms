```cpp
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

int cache[1002];
int n;

int main(void) {
    FAST_IO;

    // 1 -> 상근
    // 2 -> 창영
    cin >> n;

    cache[1] = 1;
    cache[2] = 2;
    cache[3] = 1;

    REP(i, 4, n) {
        cache[i] = min(cache[i - 1] + 1, cache[i - 3] + 1);
    }
    cout << ((cache[n] & 1) ? "SK" : "CY");
}
```
