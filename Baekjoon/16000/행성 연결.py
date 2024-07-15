import sys
import time

input = sys.stdin.readline

edge = []
parent = [0] * 1002
rank = [1] * 1002

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def is_diff(u, v):
    u = find(u)
    v = find(v)
    if u==v: return False
    if rank[u] > rank[v]:
        u,v = v,u
    parent[u] = v
    if rank[u] == rank[v]:
        rank[v]+=1
    return True

# start = time.time()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    parent[i] = i
    for j in range(n):
        if i==j: continue
        edge.append([arr[i][j], i, j]) # 비용, 노드1, 노드2

edge.sort()
sum = 0
cnt = 0

for i in range(len(edge)):
    cost, u, v = edge[i]
    if is_diff(u, v) == False: continue
    sum += cost
    cnt += 1
    if cnt==n-1: break

print(sum)


# end = time.time()
# print(end - start)
