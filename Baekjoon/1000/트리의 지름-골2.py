# 첫번째 생각 -> degree가 1개인 노드들 기준으로 dfs 여러개 -> 시간초과
# 두번쨰 생각 -> 어떤 특정 아무 노드에서 시작 -> 가장 비용이 많이 드는 노드 체크
# -> 그 노드로부터 다시 한번 더 DFS

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

def dfs(node):
    if visited[node] == 1:
        return
    
    visited[node] = 1
    for nxt in adj[node]:
        if visited[nxt[0]] == 1: continue
        dist[nxt[0]] = dist[node] + nxt[1]
        dfs(nxt[0])



n = int(input())
adj = [[] for _ in range(n+1)]



for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)-2, 2):
        adj[arr[0]].append([arr[j], arr[j+1]]) # (node번호, 비용)

dist = [0] * 100002
visited = [0] * 100002
dfs(1)
max_value = max(dist[1:n+1])
max_index = dist.index(max_value) # 가장 멀리 떨어져 있는 노드의 index임


dist = [0] * 100002
visited = [0] * 100002
dfs(max_index)
print(max(dist[1:n+1]))