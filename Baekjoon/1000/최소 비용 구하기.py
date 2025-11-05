import sys
import heapq

input = sys.stdin.readline


n = int(input())
m = int(input())
board = [[] for _ in range(n+2)]
dist = [0x3f3f3f3f] * (n+2)


for _ in range(m):
    u, v, cost = map(int, input().split()) # 시작, 도착, 비용
    board[u].append((v, cost))

st, en = map(int, input().split()) # 구해야 하는 시작, 도착지점

Q = []
dist[st] = 0
heapq.heappush(Q, (dist[st], st)) # 비용, 노드(시작)

while len(Q) != 0:
    cost, node = heapq.heappop(Q)
    if dist[node] != cost: continue
    else: # 거쳐 가는 게 더 짧은 경우
        for nxt_node, nxt_cost in board[node]:
            if dist[nxt_node] <= dist[node] + nxt_cost: continue
            else:
                dist[nxt_node] = dist[node] + nxt_cost
                heapq.heappush(Q, (dist[nxt_node], nxt_node))

print(dist[en])


