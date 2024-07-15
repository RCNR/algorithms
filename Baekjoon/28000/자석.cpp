// 28303

#include <bits/stdc++.h>
#define rep(i, a, n) for(auto i=a; i<n; i++)
#define REP(i, a, n) for(auto i=a; i<=n; i++)
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)

using namespace std;

int n, k;
vector<int> board(500'002);

int main() {
    FAST_IO;

// (a_i - Ki) - (a_j - Kj)  when i > j

    cin >> n >> k;
    REP(i, 1, n)
        cin >> board[i];
    
    vector<int> Reverse_board(500'002);
    REP(i, 1, n) Reverse_board[i] = board[n+1-i];
    
    int max_num = (int)-2e10;

    int min_num1 = (int)2e10;
    int min_num2 = (int)2e10;

    REP(i, 2, n) {
        int j = i - 1;

        min_num1 = min(min_num1, board[j] - k * j);
        min_num2 = min(min_num2, Reverse_board[j] - k * j);

        max_num = max({max_num, board[i]-k*i - min_num1, Reverse_board[i]-k*i - min_num2});
    }

    cout << max_num << '\n';
    
    // REP(i, 2, n) {
    //     int j = i - 1;

    //     min_num2 = min(min_num2, Reverse_board[j] - k * j);
    //     max_num2 = max(max_num2, Reverse_board[i] - k * i);
    // }

    // cout << max(max_num1 - min_num1, max_num2 - min_num2);


}