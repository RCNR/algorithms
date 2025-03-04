# 벽 부수고 이동하기 2206
# 시작은 (0,0)이므로 모든 1을 한 번씩 0으로 바꾸어 가면서 bfs를 돌려본다
# 만약 1을 한 번씩 바꾸었음에도 나아갈 수 없다면 복구시키고 다음 벽으로 넘어간다
# 근데 모든 1을 다 보게 되면 비효율적이다 -> 안 봐도 되는 1을 걸러야된다
# 이렇게해도 1의 개수만큼 bfs를 돌게 된다 -> 시간 초과

# 원큐에 벽을 부수지 않은 경우와 하나만 부수는 경우를 구해야함
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]


def bfs():
    
    # dist[0][i][j] - 부수지 X
    # dist[1][i][j] - 부순 O
    dist = [[[-1] * m for _ in range(n)] for _ in range(2)]
    dist[0][0][0] = 1
    dist[1][0][0] = 1
    Q = deque()
    Q.append((0, 0, 0))

    while len(Q) != 0:
        cur = Q.popleft()
        if cur[1] == n-1 and cur[2] == m-1:
            return dist[cur[0]][n-1][m-1]
        
        for dir in range(4):
            nx = cur[1] + dx[dir]
            ny = cur[2] + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0 and dist[cur[0]][nx][ny] == -1:
                dist[cur[0]][nx][ny] = dist[cur[0]][cur[1]][cur[2]] + 1
                Q.append(( cur[0], nx, ny))
            
            # 이전에 부수지 않았고 다음 차례에 부수는 경우
            if cur[0] == 0  and board[nx][ny] == 1 and dist[1][nx][ny] == -1:
                dist[1][nx][ny] = dist[cur[0]][cur[1]][cur[2]] + 1
                Q.append((1, nx, ny)) # 더 이상 부시지 않기에 1로 append
    return -1


print(bfs())


