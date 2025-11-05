# 1647
# 마을을 반드시 2개로 분리해야 함, 각 마을엔 최소 하나의 집이 있어야함, 마을과 마을 사이의 다리는 필요없음
# 다리의 cost 비용을 최소화 해야함
# -> 무조건적으로 마을 하나에 집 하나만 남겨두면 되는 거 아닌가?
# -> 이렇게 되면 edge개수가 vertex - 2이면 종료 되어야함

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
edge = [(0,0,0) for _ in range(M+3)]
parent = [0] * (M+3)
rank = [1] * (M+3)

def find(u):
    if u == parent[u]: return u # 루트에 도달
    parent[u] = find(parent[u])
    return parent[u]


def is_diff(u ,v):
    u = find(u) # 각각 부모를 찾아야함
    v = find(v)
    if u==v: return False
    if rank[u] > rank[v]: u,v = v,u
    parent[u] = v
    if rank[u] == rank[v]: rank[v] += 1
    return True

for i in range(M):
    u, v, cost = list(map(int, input().split()))
    edge[i] = (cost, u, v)
    parent[u] = u
    parent[v] = v

edge[0:M] = sorted(edge[0:M]) # cost 기준으로 정렬

cnt = 0
sum = 0
for i in range(M):
    cost, u, v = edge[i]
    if is_diff(u, v) == False: continue
    sum += cost
    cnt += 1
    if (cnt == N-2): break
if N == 2:
    print(0)
else:   
    print(sum)