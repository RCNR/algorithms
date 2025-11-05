# 비숍 1799
# 비숍은 대각선으로만 이동 가능 -> 짝수 칸, 홀수 칸 분리 가능
# (0부터 시작 2씩 증가) + (1부터 시작 2씩 증가) -> 제곱 수를 분리해서
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def func(idx, cnt):
    global max_cnt
    
    if max_cnt >= cnt + ((limit + 1) - idx) // 2: # 2개씩 나눠서 가니깐 // 현재 개수 + 남은 개수 다 넣었을 때
        return 
    
    if idx == limit or idx == limit + 1: # 1부터 시작해 +2 하면 범위 나가는 것도 고려
        max_cnt = max(max_cnt, cnt)
        return
    

    for i, j in diagonal[idx]:
        if is_visited[i-j] == False:
            is_visited[i-j] = True
            func(idx + 2, cnt + 1) # 비숍 놓는 경우
            is_visited[i-j] = False
    func(idx+2, cnt) # 이번 대각선에 비숍 아예 놓지 않음


# 사선 개수 2n-1개
diagonal = [[] for _ in range(2*n)]
is_visited = [False] * (2*n)
limit = 2*n - 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            diagonal[i+j].append((i, j))

max_cnt = 0
func(0, 0) # 0부터 시작 
k = max_cnt

max_cnt = 0
func(1, 0) # 1부터 시작

print(k + max_cnt)