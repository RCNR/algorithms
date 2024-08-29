// 1240
// 맨 처음 제출 때 메모리초과 발생 -> 원인 : 기존에 큐에 들어갔던 값이 또 큐에 들어감
#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(0);  cout.tie(0);
#define rep(i, a, n) for(auto i=a; i<n; i++)
#define REP(i, a, n) for(auto i=a; i<=n; i++)
#define pb push_back
#define X first
#define Y second

using namespace std;

int n, m;
vector<pair<int,int>> adj[1002];
int dist[1002];
int parent[1002];


int main() {

    cin >> n >> m;

    rep(i, 0, n-1) {
        int u, v, cost;
        cin >> u >> v >> cost;
        adj[u].pb({v, cost});
        adj[v].pb({u, cost});
    }

    while(m--) {
        int u, v;
        cin >> u >> v;
        memset(dist, 0, sizeof(dist));
        memset(parent, 0, sizeof(parent));
        queue<int> Q;
        Q.push(u);
        bool flag = false;
        
        while(!Q.empty()) {
            auto cur = Q.front(); Q.pop();
            for(auto nxt : adj[cur]) {
                if(parent[cur] == nxt.X) continue;
                Q.push(nxt.X);
                dist[nxt.X] = dist[cur] + nxt.Y;
                parent[nxt.X] = cur;
                
                if(nxt.X == v) {
                    flag = true;
                    break;
                }
            }
            if(flag) break;
        }
        cout << dist[v] << '\n';
    }
}
