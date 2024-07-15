
edge = [(0, 0, 0) for _ in range(100005)]
cnt = 0
parent = [0] * 100005
rank = [0] * 100005

def find(u):
    if u == parent[u]:
        return u
    else:
        parent[u] = find(parent[u])
        return parent[u]

def is_diff(u, v):
    u = find(u)
    v = find(v)
    if u == v: return False
    if rank[u] > rank[v]:
        u, v = v, u
    parent[u] = v
    if rank[u] == rank[v]:
        rank[v] += 1

    return True

V, E = map(int, input().split())

for i in range(E):
    a, b, cost = list(map(int, input().split()))
    edge[i] = (cost, a, b)
    parent[a] = a
    parent[b] = b
    rank[a] = 1
    rank[b] = 1

edge[0:E] = sorted(edge[0:E]) # 0 ~ E-1까지 부분 정렬

sum = 0

for i in range(E):
    cost, a, b = edge[i]
    if (is_diff(a, b) == False): continue
    #else
    sum += cost
    cnt+=1
    if(cnt == V-1): break

print(sum)


