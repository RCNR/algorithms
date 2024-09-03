import sys
input = sys.stdin.readline

edge = [(0, 0, 0) for _ in range(500001)]
parent = [0] * 1002
rank = [0] * 1002

is_zero_cnt = 0
cnt=0

n, m = map(int, input().split())

def find(u):
    if parent[u] == u: return u
    else:
        parent[u] = find(parent[u])
        return parent[u]

def is_diff(u, v):
    u = find(u)
    v = find(v)


for i in range(m+1):
    u, v, is_zero = map(int, input().split())
    if(is_zero == 0): is_zero_cnt += 1
    edge[i] = (is_zero, u, v)
    parent[i] = i
    rank[i] = 1

edge.sort()

for i in range(len(edge)):
    cost, a, b = edge[i]
    if(is_diff(a, b) == 0): continue # 다른 그룹이 아니면 -> 같은 그룹이면 볼 필요 없음
    




