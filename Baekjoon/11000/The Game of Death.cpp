// 11558 
// DFS로 해결 - 인당 한명씩 지목 가능 -> 끝은 무조건 n이어야한다. n에 도달하지 못하는 경우만 잘 체크하면 해결

#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define REP(i, a, n) for(auto i = a; i <= n; i++)
#define X first
#define Y second
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL), cout.tie(NULL)

using namespace std;

bool visited[10003];
int t, n;
vector<int> board(10003);

int dfs(int i_will_kill, int cnt) {
    if (i_will_kill == n) {
        return cnt;
    }
    if (cnt == n) {
        if (i_will_kill != n)
            return 0;
    }

    cnt += 1;
    return dfs(board[i_will_kill], cnt);
}


int main() {
    FAST_IO;

    cin >> t;
    while (t--) {
        memset(visited, 0, sizeof(visited));
        fill(board.begin(), board.end(), 0);

        cin >> n;
        REP(i, 1, n) {
            int num; cin >> num;
            board[i] = num;
        }

        visited[1] = true;
        int res = dfs(1, 0);
        cout << res << '\n';
    }

}