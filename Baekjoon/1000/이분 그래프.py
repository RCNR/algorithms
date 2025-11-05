# 이분 그래프 1707
# 분할하기 위해서는 다음 노드가 현재 노드에 속해 있는 집합과는 달라야 한다.

import sys
from collections import deque
input = sys.stdin.readline



k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    board = [[] for _ in range(v+4)]
    is_color = [-1] * (v+4)
    for _ in range(e):
        n, m = map(int, input().split())
        board[n].append(m)
        board[m].append(n)
    
    check = True
    Q = deque()
    
    for i in range(1, v+1):
        Q.append(i)
        while len(Q) != 0:
            cur = Q.popleft()
            if is_color[cur] == -1: is_color[cur] = 0

            for nxt in board[cur]:
                if is_color[nxt] == is_color[cur]:
                    check = False
                    break
                if is_color[nxt] >= 0: continue
                else:
                    if is_color[cur] == 0: is_color[nxt] = 1
                    elif is_color[cur] == 1: is_color[nxt] = 0
                    Q.append(nxt)
            
        if check == False:
            print('NO')
            break
    if check:
        print('YES')