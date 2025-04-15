# 숨바꼭질 2 12851
# 가장 빠른 시간에 왔는지(얼마만큼의 거리)는 bfs를 돌려서 구성한다.
# 방문했던 곳을 또 올 수 있도록 처리한다.
# 방문했는지 확인하는 배열은 따로 구성하지 않고 거리를 구성하는 dist[] 배열로 해결

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dist = [-1] * 100004  # 이동 횟수, 몇 개 인지
Q = deque()
cnt = 0

dist[n] = 0
Q.append(n)

while Q:
    cur = Q.popleft()
    if cur == k:
        cnt += 1
        continue
    board = [cur - 1, cur + 1, 2 * cur]
    for move in board:
        if move > 100000 or move < 0: continue
        if dist[move] == -1: # 첫 방문
            dist[move] = dist[cur] + 1
            Q.append(move)
        elif dist[move] == dist[cur] + 1: # 첫 방문이 아닌데 가장 빠른 시간과 같은 경우
            Q.append(move)

print(dist[k])
print(cnt)