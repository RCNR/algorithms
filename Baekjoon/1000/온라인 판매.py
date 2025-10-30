# 온라인 판매.py 1246
# 시간이 넉넉하여 정렬하고 하나씩 확인할 수 있지만, lower_bound를 사용해 풀어보았다
# 현재 가격보다 같거나 큰 가격의 개수를 세어 수익을 계산
# 이때 개수가 n보다 작거나 같을 때만 수익 계산

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(int(input()) for _ in range(m))
board.sort()

res = -1
pric = -1
for num in board:
    siz = len(board)
    check = siz - bisect_left(board, num)
    # print(num, check)
    if check <= n:
        if num * check > res:
            res = num * check
            price = num

print(price, res)