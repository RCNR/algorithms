# 지름길.py 1446
# DP 문제
# 0부터 D까지 쭉 가면서 지름길 시작점 위치와 현재 위치에서 지름길을 타는 경우와 안타는 경우를 비교


import sys
input = sys.stdin.readline

N, D = map(int, input().split())

check = []
board = [i for i in range(D+1)]

for _ in range(N):
    u, v, cost = map(int, input().split())

    if u <= D and v <= D:
        check.append((u, v, cost))

for i in range(D+1):
    
    if i > 0:
        board[i] = min(board[i], board[i-1] + 1)
    
    for u, v, cost in check:
        if i == u:
            board[v] = min(board[v], board[u] + cost)

print(board[D])

