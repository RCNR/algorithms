// 1504
// 이 코드는 전체 경로를 다 조사함
// 효율적으로 바꿀 필요가 있음
/*int answer1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,V);
    int answer2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,V);
    
    int answer = min(answer1,answer2); 
    이렇게 하면 다익스트라 경로 조회 횟수를 대폭 줄일 수 있어 시간이 넉넉함
    */

#include <iostream>
#include <vector>
#include <queue>
#define FAST_IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define rep(i, a, n) for(auto i=a; i<n; i++)
#define REP(i, a, n) for(auto i=a; i<=n; i++)
#define X first
#define Y second

using namespace std;

const int INF = 0x3f3f3f3f;
vector<vector<pair<int,int>>> adj(802);
vector<vector<int>> route(802);

int func(int start, int u, int v, int end);

int main() {
    FAST_IO;
    int n,m;
    int u, v;
    cin >> n >> m;
    rep(i, 0, m) {
        int st, en, cost;
        cin >> st >> en >> cost;
        adj[st].push_back({cost, en});
        adj[en].push_back({cost, st});
    }

    cin >> u >> v;  

    REP(i, 1, n) {
        priority_queue<pair<int,int>, vector<pair<int,int>>,  greater<pair<int,int>>> pq;
        vector<int> dist(802);
        REP(j, 1, n) dist[j] = INF;
        
        dist[i] = 0;

        pq.push({dist[i], i});

        while(!pq.empty()) {
            auto cur = pq.top(); pq.pop();

            if(cur.X != dist[cur.Y]) continue;

            for(auto nxt:adj[cur.Y]) {
                if (dist[nxt.Y] <= dist[cur.Y] + nxt.X) continue;
                
                dist[nxt.Y] = dist[cur.Y] + nxt.X;
                pq.push({dist[nxt.Y], nxt.Y});
            }
        }

        REP(j, 1, n) {
            route[i].push_back(dist[j]);
        }
    }

    long long num1 = func(1, u, v, n);
    long long num2 = func(1, v, u, n);
    cout << min(num1, num2) << '\n';

    // rep(i, 0, 4) {
    //     cout << route[3][i] << endl;
    // }
}

int func(int start, int u, int v, int end) {
    long long sum = 0;
    sum += route[start][u-1];
    sum += route[u][v-1];
    sum += route[v][end-1];
    if(sum >= INF) return -1;
    return sum;
}