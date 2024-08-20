# 1967 - 트리의 지름
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

def dfs(cur, cur_dist):
    for v, cost in adj[cur]:
        if dist[v] != -1: continue
        dist[v] = cur_dist + cost
        dfs(v, dist[v])


adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, cost = map(int, input().split())
    adj[u].append((v, cost))
    adj[v].append((u, cost)) # 처음에 필요 없을 거라고 생각 -> 하지만 마지막에 한번 더 dfs 해야해서 필요함

dist = [-1] * (n+1)
dist[1] = 0
dfs(1, 0) # 일단 무조건적으로 1(루트)에서 가장 멀리 있으면서 dist 값이 큰 노드로 가야함

super_node = dist.index(max(dist)) # 1 기준으로 가장 멀리 떨어져 있는 놈을 선택해야함 -> 예제 기준 9번 노드가 나옴

dist = [-1] * (n+1)
dist[super_node] = 0  
dfs(super_node, 0) # 예제 기준 9번에서 한 번 dfs 해야함

print(max(dist)) # 9번 기준 가장 큰 값이 나오게 됨