# 비숍 1799
# 시간 복잡도 매우 큰 경우 -> 10 * 10 전체를 하나로 본 경우 
import sys
input = sys.stdin.readline


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def func(idx, cnt):
    global max_cnt
    
    if max_cnt >= cnt + limit - idx: # 현재 개수 + 남은 개수 다 넣었을 때
        return
    
    if idx == limit:
        max_cnt = max(max_cnt, cnt)
        return
    

    for i, j in diagonal[idx]:
        if is_visited[i-j] == False:
            is_visited[i-j] = True
            func(idx + 1, cnt + 1) # 비숍 놓는 경우
            is_visited[i-j] = False
    func(idx+1, cnt) # 이번 대각선에 비숍 아예 놓지 않음


# 사선 개수 2n-1개
diagonal = [[] for _ in range(2*n)]
is_visited = [False] * (2*n)

limit = 2*n - 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            diagonal[i+j].append((i, j))

max_cnt = 0
func(0, 0) # diagonal 인덱스, 놓은 개수

print(max_cnt)
