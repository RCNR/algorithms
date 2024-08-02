// 1389

#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i=a; i<n; i++)
#define REP(i, a, n) for(auto i=a; i<=n; i++)

using namespace std;

vector<pair<int, int>> v; // 총 인원 수, 노드 번호
int dist[102];
bool visited[102];


int main() {

    int n, m;
    cin >> n >> m;

    vector<int> adj[102];
    rep(i, 0, m) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    REP(i, 1, n) {
        
        queue<int> q;
        fill(dist, dist+102, -1);
        memset(visited, false, sizeof(visited));
        dist[i] = 0;
        q.push(i);
        int sum = 0;

        while(!q.empty()) {
            auto cur = q.front(); q.pop();
            for(auto nxt:adj[cur]) {
                if(dist[nxt] != -1) continue;
                q.push(nxt);
                dist[nxt] = dist[cur] + 1;
            }
        }

        REP(i, 1, n) sum += dist[i];
        v.push_back({sum, i});
    }

    sort(v.begin(), v.end());

    cout << v[0].second;
}