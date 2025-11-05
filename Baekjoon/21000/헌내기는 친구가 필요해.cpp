#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
#define X first
#define Y second
#define pb push_back
#define pii pair<int, int>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL), cout.tie(NULL)

using namespace std;

int dx[4] = { 1, 0, 0, -1 };
int dy[4] = { 0, 1, -1, 0 };
vector<string> v;
queue<pii> Q;
bool isvisited[602][602];


int main() {
    FAST_IO;

    int n, m;
    cin >> n >> m;

    rep(i, 0, n) {
        string str; cin >> str;
        v.pb(str);
    }

    rep(i, 0, n) {
        rep(j, 0, m) {
            if (v[i][j] == 'I') {
                Q.push({ i, j });
                isvisited[i][j] = true;
            }
        }
    }

    int cnt = 0;
    while (!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m || isvisited[nx][ny] == true) continue;
            if (v[nx][ny] == 'X') continue;
            if (v[nx][ny] == 'P') cnt++;

            Q.push({ nx, ny });
            isvisited[nx][ny] = true;
        }
    }

    if (cnt == 0) cout << "TT";
    else cout << cnt;
}