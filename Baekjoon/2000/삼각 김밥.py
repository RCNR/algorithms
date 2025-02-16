# 삼각 김밥 2783

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
min_num = float(f"{1000 / m * n:.2f}")
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    res = float(f"{1000 / b * a:.2f}")
    min_num = min(min_num, res)

print(min_num)
