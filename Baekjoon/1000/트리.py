# 트리 1068
# 노드 삭제 -> 자식 노드들도 삭제됨
# 이후 남아있는 리프 노드 개수 구하기

# 첫 번째
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

adj = [[] for _ in range(52)]

n = int(input())
board = list(map(int, input().split()))
num = int(input())
is_visited = [False] * 53

def dfs(cur):
    cnt = 0
    check = False

    if cur != num: # 삭제할 노드가 아닌 경우 -> 삭제할 노드쪽은 보지 않겠다
        for nxt in adj[cur]:
            if is_visited[nxt] == False and nxt != num:
                is_visited[nxt] = True
                check = True # cur은 자식 노드가 존재함
                cnt += dfs(nxt) # nxt로 가서 리프 노드 개수 가져옴
    
    return 1 if check==False else cnt
        

idx = 0
for i in board:
    if i == -1:
        root = idx # root를 시작지점으로
    else:
        adj[idx].append(i)
        adj[i].append(idx)
    idx += 1

# print(adj)

is_visited[root] = True
if num == root:
    print(0)
    exit()
print(dfs(root))

##############################################

# 트리 1068
# 노드 삭제 -> 자식 노드들도 삭제됨
# 이후 남아있는 리프 노드 개수 구하기

# 삭제할 노드와 그 밑에 있는 자식 노드들에게 삭제 표시를 남김
# 후에 루프 돌면서 삭제 표시가 없으면서, 부모 노드가 아닌 것에 cnt += 1
# 두 번째

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
num = int(input())

cnt = 0

def dfs(cur):
    board[cur] = -100
    for i in range(n):
        if cur == board[i]:
            dfs(i)

dfs(num)

for i in range(n):
    if board[i] != -100 and i not in board:
        cnt += 1

print(cnt)


