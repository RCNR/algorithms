# 9019 DSLR

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

res = []
for _ in range(n):
    a, b = map(int, input().split())
    Q = deque()
    is_visit=[False] * 10003
    dist = [""] * 10003

    Q.append(a)
    is_visit[a] = True

    while len(Q) != 0:
        cur = Q.popleft()

        if cur == b:
            res = dist[cur]
            break

        D = 2 * cur if 2 * cur <= 9999 else 2 * cur % 10000
        S = cur-1 if cur-1 >= 0 else 9999
        L = cur*10 % 10000 + cur // 1000
        R = cur // 10 + cur % 10 * 1000
        
        for nxt, character in [(D, "D"), (S, "S"), (L, "L"), (R, "R")]:
            if is_visit[nxt] == False:
                Q.append(nxt)
                is_visit[nxt] = True
                dist[nxt] = dist[cur] + character
                # print(dist[nxt])
    print(res) 
