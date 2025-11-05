// 32184
// 시작지점 홀수이냐 짝수냐에 따라 달라지니 조심

#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
#define X first
#define Y second
#define pb push_back
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL), cout.tie(NULL)

using namespace std;


int main() {
    FAST_IO;

    int n, m;
    cin >> n >> m;

    int k = (m - n + 1) % 2;
    int a = (m - n + 1) / 2;

    if (n % 2 != 0) { // n홀수
        if (m % 2 == 0) cout << a;
        else cout << a + 1;
    }
    else {
        cout << a + 1;
    }
}