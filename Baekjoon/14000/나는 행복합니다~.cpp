// 14652 - 2차원 배열에 대해 생각해볼만한 문제
// 단순 사칙연산이지만 2차원 좌표를 정수 하나로 압축시킬 수 있다는 것
// 이는 오로지 열로만 가능하다는 것
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
    
    int n, m, k;
    cin >> n >> m >> k;
    cout << k/m << ' ' << k%m;

    return 0;
}
