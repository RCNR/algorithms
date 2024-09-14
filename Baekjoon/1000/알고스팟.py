# 1261
# bfs와 최단경로 알고리즘 짬뽕
import sys
import heapq
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board = [0]
INF = 0x3f3f3f3f
dist = [[INF] * 103 for _ in range(103)] 
m, n = map(int, input().split())

for _ in range(n):
    ary = input().rstrip()
    board.append(ary)

dist[1][1] = 0
pq = []
heapq.heappush(pq, (0, 1, 1)) # 비용, x좌표, y좌표

while len(pq) != 0:
    cost, cur_x, cur_y = heapq.heappop(pq)

    if dist[cur_x][cur_y] != cost: continue
    
    for dir in range(4):
        nxt_x = dx[dir] + cur_x
        nxt_y = dy[dir] + cur_y
        if nxt_x > n or nxt_x < 1: continue
        if nxt_y > m or nxt_y < 1: continue
        
        nxt_wall = dist[cur_x][cur_y] + int(board[nxt_x][nxt_y-1]) # nxt_y-1을 한 이유: "011","111","110"-> board[i][j] 여기서 i는 1부터, j 0 부터 시작임 
        if nxt_wall < dist[nxt_x][nxt_y]:
            dist[nxt_x][nxt_y] = nxt_wall
            heapq.heappush(pq, (nxt_wall, nxt_x, nxt_y))

print(dist[n][m])
        
