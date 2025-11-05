# 15686 치킨 배달
# 파이썬의 combinations를 이용한 조합 구현

import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1: house.append((i, j))
        elif board[i][j] == 2: chicken.append((i, j))

min_res = 1e9

for comb in combinations(chicken, m):
    total = 0
    for x, y in house:
        dist = min(abs(x - cx) + abs(y - cy) for cx, cy in comb)
        total += dist
    min_res = min(min_res, total)

print(min_res)