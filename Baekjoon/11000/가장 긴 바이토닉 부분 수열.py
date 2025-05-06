# 가장 긴 바이토닉 부분 수열 11054
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))

dp = [[-1] * (3) for _ in range(n+3)] # dp[a][b] -> 인덱스, 왼쪽/오른쪽 길이

def left_func(num):
    
    if dp[num][0] != -1:
        return dp[num][0]

    dp[num][0] = 1
    
    for i in range(0, num):
        if ary[i] >= ary[num]: continue # 같거나 더 크면 증가하는 부분 수열 X
        dp[num][0] = max(dp[num][0], left_func(i) + 1)
    
    return dp[num][0]

def right_func(num):

    if dp[num][1] != -1:
        return dp[num][1]
    
    dp[num][1] = 1
    
    for i in range(n-1, num-1, -1): # 현재 위치의 오른쪽 값이 더 크면 안된다
        if ary[i] >= ary[num]: continue
        dp[num][1] = max(dp[num][1], right_func(i) + 1)
    
    return dp[num][1]

left = -1
right = -1
for i in range(0, n):
    left = max(left, left_func(i))
    right = max(right, right_func(n-1-i))

# print(dp)
max_result = -1
for i in range(n):
    max_result = max(max_result, dp[i][0] + dp[i][1])

print(max_result - 1) # -1 해주는 이유는 왼쪽에서 구한 길이와 오른쪽에서 구한 길이의 중복 때문에