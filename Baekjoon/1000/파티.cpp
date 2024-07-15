#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
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

const int INF = 0x3f3f3f3f;
vector<pair<int,int>> adj[1002];
vector<vector<int>> student(1002);

int main() {
    FAST_IO;
    
    // N에 구하기
    int n, m, x;
    cin >> n >> m >> x;

    rep(i, 0, m) {
        int st, en, cost;
        cin >> st >> en >> cost;
        adj[st].pb({ cost, en });
    }
    REP(i, 1, n) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> dist(1003);
        rep(kk, 0, 1003) dist[kk] = INF;
        dist[i] = 0;
        

        pq.push({ dist[i], i });

        while (!pq.empty()) {
            auto cur = pq.top(); pq.pop();

            if (cur.X != dist[cur.Y]) continue;
            
            for (auto nxt : adj[cur.Y]) {
                if (dist[nxt.Y] <= dist[cur.Y] + nxt.X) continue;
                dist[nxt.Y] = dist[cur.Y] + nxt.X;
                pq.push({ dist[nxt.Y], nxt.Y });
            }
        }

        REP(j, 1, n) {
            student[i].pb(dist[j]);
        }
    }

    int long_stu = 0;
    REP(i, 1, n) {
        long_stu = max(long_stu, student[i][x-1] + student[x][i-1]); // 마지막 인덱스 -1 해줘야 out of range 발생X, ex) 4->2최단 경로 + 2->4 최단경로 합
    }
    cout << long_stu;
}

