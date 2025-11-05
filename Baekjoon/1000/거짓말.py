# 거짓말.py 1043
# union-find 적용하기
# 처음에는 dfs로만 해도 될까 싶었지만 진실을 알고 있는지를 구현하는 게 되지 않는다
# 다른 파티여도 특정 파티에 진실을 아는 사람이 있으면 다른 파티도 알 수도 있기 때문에
# 같은 그룹으로 묶어버리는 방식으로 진행

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

truth = []
board = list(map(int, input().split()))

truth = board[1:]
parent = list(range(N+1))

def find(u):
    if u == parent[u]: return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    
    u = find(u)
    v = find(v)
    if u == v: return
    parent[v] = u # v의 부모는 u


parteis = []
for i in range(M):
    party = list(map(int, input().split()))[1:]
    parteis.append(party)
    for i in range(1, len(party)):
        merge(party[0], party[i]) # 대표 하나로 묶기

if not truth:
    print(M)
    exit()

roots = set(find(t) for t in truth)

cnt = 0

for party in parteis:
    if all(find(p) not in roots for p in party): cnt += 1

print(cnt)