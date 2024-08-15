# 1차원 배열로도 풀 수 있음

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    board = [0]+ [i for i in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n+1):
            board[i] += board[i-1]
    print(board[n])
