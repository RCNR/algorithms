# 최소, 최대 2 20053
# 정렬을 시켜 NlogN으로 구하느냐
# min, max 로 O(N)으로 갈 것이냐

import sys
input =  sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    board = list(map(int, input().split()))
    print(f'{min(board)} {max(board)}')
    
