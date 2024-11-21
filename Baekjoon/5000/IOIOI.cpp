// 5525 IOIOI
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

int n, m;
string str;

int main() {
    FAST_IO;

    cin >> n;
    cin >> m;
    cin >> str;
    
    // 첫 번째 시도 때 만약 IOIOIOIOIOIOI 형태고 p5 형태인 IOIOIOIOI일 때 첫번째 p5 형태를 구했다면 어떻게 다시 IO/IOIOIOIOI 에서
    // 어떻게 2번째 I로 가는지를 해결하지 못함
    // 그런데 IOIOIOIOI 형태에서 뒤의 두개의 형태가 OI 형태이면 첫번째것이 p5를 만족했으니
    // 자연스레 2번째 I에서 시작하는 형태의 p5도 완성하게 됨 -> 즉, 두번째 I를 볼 필요 없음

    int cnt = 0;

    rep(i, 0, m) {
        int check = 0; // check 변수를 통해 Pn의 형태를 파악할 것 p1(IOI) = 1 , p2(IOIOI) = 2, ...

        if (str[i] == 'O') continue; // str[i]가 I일 때만 확인

        while (str[i + 1] == 'O' and str[i + 2] == 'I') { // 무조건 2개씩(O, I인지) 확인할 것임

            check++;
            if (check == n) { // IOIOIOI (P3) 인 경우 확인
                cnt += 1;
                check--; // 확인했으니 다음에 또 OI가 있을 수 있기에 하나 빼준다.
            }
            i += 2;
        }
    }
    cout << cnt;
    
}

