// 2252 줄 세우기 (위상정렬 입문 문제)

#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
#define X first
#define Y second
#define pb push_back
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL), cout.tie(NULL)

using namespace std;

int n, m;
vector<int> adj[32002];
int indegree[32002];
queue<int> Q;
vector<int> res;

int main() {
    FAST_IO;

    cin >> n >> m;
    REP(i, 1, m) {
        int u, v; // u가 더 작음 u -> v 형태
        cin >> u >> v;
        adj[u].pb(v);
        indegree[v]++;
    }


    REP(i, 1, n) {
        if (indegree[i] == 0)
            Q.push(i);
    }

    while (!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        res.pb(cur);

        for (auto nxt : adj[cur]) {
            indegree[nxt]--;
            if (indegree[nxt] == 0) {
                Q.push(nxt);
            }
        }
    }

    for (auto i : res)
        cout << i << ' ';
}