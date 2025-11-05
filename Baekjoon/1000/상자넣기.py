# 상자넣기.py 1965
# 작은 상자는 큰 상자 안에 넣을 수 있다. 가장 많이 넣을 수 있는 상자에서의 개수를 카운트해야한다
# DP 문제 -> LIS 문제
# DP[i] = i번째 상자를 마지막으로 넣었을 때의 최대 개수
n = int(input())
board = list(map(int, input().split()))
dp = [1] * (n+3)

for i in range(n):
    for j in range(0, i):
        if board[j] < board[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))