// 11779
#include <bits/stdc++.h>

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
#define X first
#define Y second
#define pii pair<int, int>
using namespace std;

vector<pair<int,int>> adj[1002];
vector<int> dist(1002);
vector<int> previous(1002);
const int INF = 0x3f3f3f3f;

int main() {
    FAST_IO;

    int n, m;
    cin >> n >> m;

    rep(i, 0, m) {
        int start, end, cost;
        cin >> start >> end >> cost;
        adj[start].push_back({cost, end});
    }

    int st, en;
    cin >> st >> en; // 구하고자 하는 출발, 도착 지점

    REP(i, 1, n) dist[i] = INF;


    priority_queue<pii, vector<pii>, greater<pii>> PQ;

    dist[st] = 0;
    previous[st] = 0;
    PQ.push({dist[st], st});

    while(!PQ.empty()) {
        auto cur = PQ.top();
        PQ.pop();

        if(dist[cur.Y] != cur.X) continue;

        for(auto nxt : adj[cur.Y]) {
            if(dist[nxt.Y] <= dist[cur.Y] + nxt.X) continue;
            else {
                dist[nxt.Y] = dist[cur.Y] + nxt.X;
                PQ.push({dist[nxt.Y], nxt.Y});
                previous[nxt.Y] = cur.Y;
            }
        }
    }

    cout << dist[en] << '\n';
    
    vector<int> v;
    v.push_back(en);
    int cnt = 1;

    while(en != st) {
        en = previous[en];
        v.push_back(en);
        cnt++;
    }

    cout << cnt << endl;
    for(int i = v.size()-1; i >= 0; i--) {
        cout << v[i] << ' ';
    }

}
