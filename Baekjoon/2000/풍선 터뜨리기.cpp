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

    deque<pair<int,int>> q;
    int n; cin >> n;

    rep(i, 0, n) {
        int num;
        cin >> num;
        q.push_back({ num, i });
    }

    rep(i, 0, n) {
        auto cur = q.front(); q.pop_front();
        cout << cur.Y+1 << ' ';
        if (cur.X > 0) {
            while (cur.X != 1) {
                if (q.empty()) break;
                auto pop_num = q.front(); q.pop_front();
                q.push_back(pop_num);
                cur.X--;

            }
        }
        else {
            while (cur.X != 0) {
                if (q.empty()) break;
                auto pop_num = q.back(); q.pop_back();
                q.push_front(pop_num);
                cur.X++;
            }
        }
    }
    return 0;
}
