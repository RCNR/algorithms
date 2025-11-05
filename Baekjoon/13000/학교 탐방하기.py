import sys
input = sys.stdin.readline

def find(u):
    if parent[u] == u: return u
    else:
        parent[u] = find(parent[u])
        return parent[u]

def is_diff(u, v):
    u = find(u)
    v = find(v)
    if u==v: return 0
    if rank[u] > rank[v]: u,v = v,u
    parent[u] = v
    if rank[u] == rank[v]: rank[v] += 1
    return 1

n, m = map(int, input().split())
m += 1

parent = [x for x in range(0, n+1)]
rank = [0 for _ in range(n+1)]
edge = []

for i in range(m):
    a, b, cost = map(int, input().split())
    edge.append([cost, a, b])

edge.sort() # 최소 신장 트리 -> 오르막길 순서 (0이 많음 -> 힘든 길)

cnt = 0
is_zero_max = 0
for i in range(m):
    cost, a, b = edge[i]
    if is_diff(a, b) == 0: continue
    
    if cost == 0:
        is_zero_max += 1
    cnt += 1
    if cnt == n: break

rank = [0 for _ in range(n+1)]
parent = [x for x in range(0, n+1)]
cnt = 0
is_zero_min = 0

edge.sort(key=lambda x:-x[0]) # 최대 신장 트리 -> 내리막길 순서
for i in range(m):
    cost, a, b = edge[i]
    if is_diff(a, b) == 0: continue
    if cost == 0:
        is_zero_min += 1
    cnt += 1
    if cnt == n: break


print((is_zero_max**2) - (is_zero_min**2))
