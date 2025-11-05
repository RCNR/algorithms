# 11722 가장 긴 감소하는 부분 수열
# 5 30 4 3 20 1
# 1 1 2 3 2 
# 5 4 3 1 => 4
import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))
dp = [0] * (n+3)

for i in range(0, n):
    dp[i] = 1
    for j in range(0, i):
        if board[i] < board[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
