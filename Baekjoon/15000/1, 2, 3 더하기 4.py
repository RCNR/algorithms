# 15989 1, 2, 3 더하기 4
import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dp = [[-1] * 5 for _ in range(10005)]

def func(num, idx):
    if num < 0: return 0

    if num == 0: # idx가 1, 2, 3일 때 문제 생김
        dp[0][1] = 1
        dp[0][2] = 0
        dp[0][3] = 0
        return dp[num][idx]

    if dp[num][idx] != -1:
        return dp[num][idx]

    res = 0

    for i in range(1, idx+1):
        res += func(num - idx, i)
    
    dp[num][idx] = res
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    for number in range(1, 4):
        result += func(n, number) # 1 ~ 3까지 합
    print(result)
