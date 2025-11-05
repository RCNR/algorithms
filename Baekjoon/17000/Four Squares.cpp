// 17626 -> 첫번째 그냥 최소만 생각하고 greedy 접근 => 반례 무조건 생기더라
// dp 접근 -> 이전 값들 사용해서

#include <bits/stdc++.h>

using namespace std;

int dp[50002];

int main() {
    
    int n;
    cin >> n;

    for(int i = 1; i <= n; i++) {
        dp[i] = dp[i-1] + 1;
        for(int j = 1; j*j <= i; j++) {
            dp[i] = min(dp[i], dp[i - j*j] + 1);
        }
    }

    cout << dp[n];
}
        