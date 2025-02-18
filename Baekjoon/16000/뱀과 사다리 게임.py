import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = {a:b for a, b in (map(int, input().split()) for _ in range(n))}
snake = {a:b for a, b in (map(int, input().split()) for _ in range(m))}
Q = deque()

Q.append(1)

dx = [1,2,3,4,5,6]

dist_cnt = [10000] * 103
dist_cnt[1] = 0

while len(Q) >= 1:
    cur = Q.popleft()
    if cur == 100: break

    if cur in ladder:
        dist_cnt[ladder[cur]] = min(dist_cnt[ladder[cur]], dist_cnt[cur])
        cur = ladder[cur]
    
    if cur in snake:
        dist_cnt[snake[cur]]  = min(dist_cnt[snake[cur]], dist_cnt[cur])
        cur = snake[cur]

    for i in range(6):
        nx = cur + dx[i]
        if nx > 100: continue
        if dist_cnt[cur] + 1 < dist_cnt[nx]:
            Q.append(nx)
            dist_cnt[nx] = dist_cnt[cur] + 1

print(dist_cnt[100])


