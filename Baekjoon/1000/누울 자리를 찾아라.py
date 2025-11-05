#1652
import sys
input = sys.stdin.readline

n = int(input())

board = [list(input().rstrip()) for _ in range(n)]

sum = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if board[i][j] == '.':
            cnt+=1
        else:
            if cnt >= 2:
                sum+=1
            cnt=0
            continue
        
        if j==n-1 and cnt>=2:
            sum+=1

print(sum, end=' ')

sum = 0

for j in range(n):
    cnt=0
    for i in range(n):
        if board[i][j] == '.':
            cnt+=1
            # print(j, i, cnt)
        else:
            if cnt >= 2:
                sum+=1
            cnt=0
            continue
        
        if i==n-1 and cnt>=2:
            sum+=1
        
print(sum)