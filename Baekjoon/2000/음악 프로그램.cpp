// 2623

#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define rep(i, a, n) for(auto i=a; i<n; i++)
#define REP(i, a, n) for(auto i=a; i<=n; i++)

using namespace std;

int n, m;
vector<int> adj[1002];
int indegree[1002];
queue<int> Q;
vector<int> res;

int main() {

    FAST_IO;

    cin >> n >> m;

    while(m--) {
        int num; cin >> num;
        vector<int> board(1002);
        REP(i, 1, num) {
            cin >> board[i];            
        }
        REP(i, 2, num) {
            int u = board[i-1]; int v = board[i];
            adj[u].push_back(v);
            indegree[v]++;
        }
    }

    REP(i, 1, n) {
        if(indegree[i] == 0) {
            Q.push(i);
        }
    }

    while(!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        res.push_back(cur);

        for(auto nxt: adj[cur]) {
            indegree[nxt]--;
            if(indegree[nxt] == 0) Q.push(nxt);
        }
    }

    if (res.size() != n) cout << 0;
    else {
        for(auto c:res) cout << c << '\n';
    }

}