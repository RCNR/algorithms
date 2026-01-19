# 스타트와 링크.py 14889
# 백트래킹을 이용한 완전 탐색
# 두 팀으로 나누는 모든 경우의 수를 탐색

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0x3f3f3f3f3f3f3f
is_visited = [False] * n

def func(node, count):
    global res
    if count == n // 2:
        start_sum, link_sum = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if is_visited[i] and is_visited[j]: start_sum += board[i][j] + board[j][i]
                elif not is_visited[i] and not is_visited[j]: link_sum += board[i][j] + board[j][i]
        
        res = min(res, abs(start_sum - link_sum))
        return
    
    for i in range(node, n):
        if not is_visited[i]:
            is_visited[i] = True
            func(i + 1, count + 1)
            is_visited[i] = False

func(0, 0) # 0명 뽑음

    
print(res)




