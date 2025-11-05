# 2294 동전 2
import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

MAX = int(1e6)
n, k = map(int, input().split())
board = list(int(input()) for _ in range(n))
dp = [-1] * 10004

def func(weight):
    if weight < 0: return MAX # 여기까지 온 건 k 초과
    if weight == 0: return 0

    if dp[weight] != -1:
        return dp[weight]
    
    dp[weight] = MAX

    for num in board: 
        dp[weight] = min(dp[weight], func(weight - num) + 1)
    
    return dp[weight]
    
res = func(k)
print(res if res != MAX else -1)