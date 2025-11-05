#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define pb push_back
#define endl "\n"
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define pii pair<int, int>
#define X first
#define Y second
#define PIV (1 << 20)

using namespace std;

int n, m, S;
int reinforce;

vector<vector<pair<int, int>>> board(30);
vector<int> cnt(30);
string ans = "";



void check(pii start, pii dest);

int main() {
    FAST_IO;

    // 25319
    cin >> n >> m >> S;

    rep(i, 0, n) {
        string str;
        cin >> str;
        rep(j, 0, m) {
            board[str[j]-'a'].pb({i, j}); // 예제 입력1 기준으로 board['c']안에 (0,1),(1,0),(0,2),(2,1)이 있을것
        }
    }

    string s;
    cin >> s;
    for(auto e:s) {
        cnt[e -'a']++; // ucpc는 u 1개, c 2개, p 1개 있음
    }

    reinforce = PIV;

    for(auto e : s) {
        reinforce = min(reinforce, (int)board[e-'a'].size() / cnt[e-'a']);
    }

    pii start = {0, 0};

    rep(i, 0, reinforce) {
        rep(j, 0, s.size()) {
            pii dest = board[s[j]-'a'].back();
            board[s[j]-'a'].pop_back();
            check(start, dest);
            start = dest;
            ans.append("P");
        }
    }

    pii end = {n-1, m-1};
    check(start, end);

    cout << reinforce << ' '  << ans.size() << endl;
    rep(i, 0, ans.size()) cout << ans[i];
}


void check(pii start, pii dest) {
    int dx = dest.X - start.X;
    int dy = dest.Y - start.Y;

    string x = dx>0 ? "D" : "U";
    string y = dy>0 ? "R" : "L";

    dx = abs(dx);
    dy = abs(dy);

    rep(i, 0, dx) ans.append(x);
    rep(i, 0, dy) ans.append(y);
}