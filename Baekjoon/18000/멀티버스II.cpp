#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
#define X first
#define Y second
#define pb push_back
#define pii pair<int, int>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL), cout.tie(NULL)
#define endl '\n'


using namespace std;

int n, m;

void func(vector<int> &v1) {

    FAST_IO;

    vector<int> v2;
    rep(i, 0, v1.size()) {
        v2.push_back(v1[i]);
    }

    sort(v2.begin(), v2.end());
    v2.erase(unique(v2.begin(), v2.end()), v2.end());

    rep(i, 0, m) {
        v1[i] = lower_bound(v2.begin(), v2.end(), v1[i]) - v2.begin();  // 좌표 압축
    }
}

int comp(vector<int> v1, vector<int> v2) {
    
    rep(i, 0, m) {
        if (v1[i] != v2[i]) return 0;
    }
    return 1;
}

int main(void) {

    cin >> n >> m;
    vector<vector<int>> v(n + 2, vector<int>(m + 2));


    rep(i, 0, n) {
        rep(j, 0, m) {
            cin >> v[i][j];
        }
        func(v[i]);
    }

    int cnt = 0;

    for (int i = 0; i < n-1; i++) {
        for (int j = i + 1; j < n; j++) {
            cnt += comp(v[i], v[j]);
        }
    }
    cout << cnt;

	return 0;
}
