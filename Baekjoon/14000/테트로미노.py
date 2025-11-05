# 테트로미노 14500
import sys
sys.setrecursionlimit(10*69)
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
is_visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

max_sum = 0

def dfs(i, j, sum, cnt):
    global max_sum

    if cnt == 5:
        max_sum = max(sum, max_sum)
        return
    
    for idx in range(4):
        nx = i + dx[idx]
        ny = j + dy[idx]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue 
        if is_visited[nx][ny] == True: continue

        is_visited[nx][ny] = True
        dfs(nx, ny, sum + board[nx][ny], cnt+1) # 다음 이동
        is_visited[nx][ny] = False

def middle_shape(i, j):
    global max_sum
    sum = board[i][j]
    max_three_nums = []

    for idx in range(4): # 한 지점을 중심으로 상, 하, 좌, 우의 값 구하고 최대값 구하기
        nx = i + dx[idx]
        ny = j + dy[idx]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        max_three_nums.append(board[nx][ny])

    max_three_nums.sort(reverse=True) # 상, 하, 좌, 우 중 가장 큰 값 3개
    if len(max_three_nums) <= 2: return
    else:
        for i in range(3):
            sum += max_three_nums[i]
    max_sum = max(max_sum, sum)

for i in range(n):
    for j in range(m):
        is_visited[i][j] = True
        dfs(i, j, 0, 1)
        middle_shape(i, j)
        is_visited[i][j] = False


print(max_sum)
