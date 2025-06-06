# 텀 프로젝트 9466

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
  if indegree[idx] == 0:
    num = graph[idx][0]
    indegree[num] -= 1
    if indegree[num] == 0:
      Q.append(num)
    return 0
  
  if is_visited[idx] == 1:
    return 1
  is_visited[idx] = 1
  
  return dfs(graph[idx][0])


t = int(input())
for _ in range(t):
  n = int(input())
  indegree = [0] * (n+3)
  is_visited = [0] * (n+3)
  board = list(map(int, input().split()))
  graph = [[] for _ in range(n+3)]
  Q = deque()
  cnt = 0
  

  for i in range(1, n+1):
    graph[i].append(board[i-1])
    idx = board[i-1]
    indegree[idx] += 1
  
  # print(indegree)
  
  for i in range(1, n+1):
    if indegree[i] == 0:
      # num = graph[i][0]
      # indegree[num] -= 1
      Q.append(i)

  
  while Q:
    cur = Q.popleft()
    res = dfs(cur)
    if res == 0:
      cnt += 1
  
  print(cnt)

