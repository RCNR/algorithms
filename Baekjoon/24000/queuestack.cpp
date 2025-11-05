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

deque<ll> Q;
vector<ll> v1;
vector<ll> v2;
int main() {
    FAST_IO;

    // 사실상 스택은 볼 필요가 없고
    // queue에서도 마지막 것만
    int n;
    cin >> n;

    rep(i, 0, n) {
        int num; cin >> num;
        v1.push_back(num);
   }

    rep(i, 0, n) {
        int num; cin >> num;
        v2.push_back(num);
    }
    
    rep(i, 0, n) {
        if (v1[i] == 0) {
            Q.push_back(v2[i]);
        }
    }
    int k; cin >> k;
    if (Q.empty()) {
        rep(i, 0, k) {
            int num; cin >> num;
            cout << num << ' ';
        }
    }

    else {
        rep(i, 0, k) {
            int num; cin >> num;
            cout << Q.back() << ' '; Q.pop_back();
            Q.push_front(num);
        }
    }
    return 0;
}
