// 2467 용액
#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define rep(i, a, n) for(auto i=a; i<n; i++)
#define REP(i, a, n) for(auto i=a; i<=n; i++)
#define endl '\n'
#define ll long long

using namespace std;

int n;
ll board[100'002];
ll INF = 1e12;
int main(void) {
    
    cin >> n;
    rep(i ,0, n) {
        cin >> board[i];
    }
    
    int st = 0;
    int en = n-1;
    ll cur = INF;
    pair<int, int> idx;
    while (st < en) {
        ll res = board[st] + board[en];

        if(abs(res) < abs(cur)){
            idx.first = st;
            idx.second = en;
            if(res < 0) st++;
            else en--;
            cur = res;
        }
        else {
            if(res < 0) st++;
            else en--;
            
        }
    }
    cout << board[idx.first] << ' ' << board[idx.second] << endl;

    
    return 0;
}