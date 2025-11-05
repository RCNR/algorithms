#include <bits/stdc++.h>
#define X first
#define Y second
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define endl "\n"

using namespace std;

int V, E;
long long sum;
int cnt;
vector<pair<int, int>> adj[10'003];
bool check[10'003]; // 같은 신장 트리에 속해 있는지

int main() {

    cin >> V >> E;

    rep(i, 0, E) {
        int a, b, cost;
        cin >> a >> b >> cost;
        adj[a].push_back({cost, b});
        adj[b].push_back({cost, a});
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> PQ;

    // 1번 부터 시작
    check[1] = 1;
    for(auto nxt : adj[1]) {
        PQ.push({nxt.X, nxt.Y}); // PQ에 {가중치, 이어진 노드} 할당
    }

    while(cnt < V - 1) { // cnt == V-1 이면 종료
        pair<int, int> p = PQ.top();
        PQ.pop();


        if(check[p.Y]) continue; // 이미 같은 신장 트리에 속해 있으면 pass

        //else
        sum += p.X;
        //cout << p.X << endl;
        check[p.Y] = 1;
        cnt++;
        for(auto nxt : adj[p.Y]) {
            if(!check[nxt.Y])
                PQ.push({nxt.X, nxt.Y});
        }
    }
    cout << sum << endl;

}