from collections import deque

def solution(board):
    
    n = len(board)
    is_visited = [[False] * n for _ in range(n)]
    total_len = n * n
    Q = deque()
    cnt = 0 
    
    dx = [0, 0, -1, -1, -1, 1, 1, 1]
    dy = [-1, 1, -1, 0, 1, 0, 1, -1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                Q.append((i,j))
                is_visited[i][j] = True
                cnt += 1
    
    while(len(Q) > 0) :
        x, y = Q.popleft()
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and is_visited[nx][ny] == False:
                    is_visited[nx][ny] = True
                    cnt += 1
    
    print(total_len - cnt)
    return total_len - cnt

