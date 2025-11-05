# 2156 포도주 시식.py
import sys
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline

n = int(input())
board = [0] + [int(input()) for _ in range(n)]
dp = [[0] * (n+4) for _ in range(3)]
# dp[1][i] - 하나만
# dp[2][i] - 연속된 경우

dp[1][1] = board[1]
dp[2][1] = board[1]

for i in range(2, n+1):
    for j in range(1, 3):
        dp[1][i] = max(dp[1][i-2], dp[2][i-2], dp[2][i-3]) + board[i]
        # 여기서 핵심은 dp[2][i-3] -> 현재 인덱스 위치를 포함해 연속 3개가 된 경우의 이전(i-3)을 봐야함
        dp[2][i] = dp[1][i-1] + board[i]

print(max(map(max, dp)))