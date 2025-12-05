# 타임머신.py 11657
# 특정 노드에서 다른 노드까지의 최단거리를 구하는데 음수가 있는 -> 벨만포드

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 0x3f3f3f3f

edge = [[]]
dist = [INF] * (N+3)

for _ in range(M):
  st, en, w = map(int, input().split())
  edge.append([st, en, w])

dist[1] = 0

for i in range(1, N): # N-1번 엣지 돌기
  for j in range(1, M+1): # 엣지 개수
    st = edge[j][0]
    en = edge[j][1]
    w = edge[j][2]

    # if i ==1:
    #   print(f'i: {i}, st: {st}, en: {en}, w: {w}')


    if dist[st] == INF: continue

    if dist[st] + w < dist[en]:
      dist[en] = dist[st] + w

is_cycle = False
for i in range(1, M+1):
  st = edge[i][0]
  en = edge[i][1]
  w = edge[i][2]

  if dist[st] != INF and dist[en] > dist[st] + w:
    is_cycle = True


if is_cycle:
  print(-1)
else:
  for i in range(2, N+1):
    if dist[i] != INF:
      print(dist[i])
    else:
      print(-1)
    


