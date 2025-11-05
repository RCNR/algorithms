# 25323
# 현재 생각 : abc가 있으면 ab가 제곱수고 ac가 제곱수면 bc도 제곱수임 -> 하나라도 제곱수가 안되면 bc는 성립X
# 배열 수들이 오름차순 배열과 곱해져 제곱수가 되면 정상임

import sys
import math
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
check = board[:]
check.sort()

def func(n):
    if math.isqrt(n)**2 == n:
        return 1
    return 0

for i in range(len(board)):
    num = func(board[i] * check[i])
    if num==0:
        print("NO")
        exit(0)

print("YES")


        