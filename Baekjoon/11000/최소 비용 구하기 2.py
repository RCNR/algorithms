from shlex import join
import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = 0x3f3f3f3f

adj = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
prev = [0] * (n+1)

for i in range(m):
    start, end, cost = map(int, input().split())
    adj[start].append((cost, end))

st, en = map(int, input().split())

dist[st] = 0
pq = [(dist[st], st)]

while len(pq)!=0:
    cur_dist, cur_node = heapq.heappop(pq)
    if dist[cur_node] != cur_dist: continue
    
    for nxt_cost, nxt in adj[cur_node]:
        if dist[nxt] <= dist[cur_node] + nxt_cost: continue
        dist[nxt] = dist[cur_node] + nxt_cost
        pq.append((dist[nxt], nxt))
        prev[nxt] = cur_node

print(dist[en])


ans = []
ans.append(en)
cnt=1

while(en!=st):
    en = prev[en]
    cnt+=1
    ans.append(en)

print(cnt)
for i in ans[::-1]:
    print(i, end=' ')
