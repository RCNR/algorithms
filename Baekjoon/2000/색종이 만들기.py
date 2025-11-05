from sys import setrecursionlimit
setrecursionlimit(10**6)

board = []
#visited = [[0 for _ in range(129)] for _ in range(129)]
cnt_0 =0
cnt_1 = 0

def func(n, x, y):
    global cnt_0, cnt_1

    flag = check(n, x, y)
    if flag==0 :
        cnt_0 += 1
        #print(x, y, "flag : ", flag)
        return
    
    if flag==1:
        cnt_1 += 1
        #print(x, y, "flag : ", flag)
        return
    
    func(n//2, x, y) # 1사
    func(n//2, x, y+n//2) # 2사
    func(n//2, x+n//2, y) # 3사
    func(n//2, x+n//2, y+n//2) # 4사
    
def check(n, x, y):
    global board

    for i in range(n):
        for j in range(n):
            if board[x+i][y+j] != board[x][y]:
                return -1
    
    return board[x][y] # 0 or 1

n = int(input())

for _ in range(n):
    board.append(list(map(int, input().split())))

func(n, 0, 0)

print(cnt_0, cnt_1)

