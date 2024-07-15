#30804
import sys

input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
cnt = [0] * 200001

st = 0
en = 0
max_sum = 0
sum = 0
count = 0
check = [0] * 10

while (en < n):
    if count <= 2:
        num = board[en]
        if cnt[num] == 0:
            count += 1
            check[num] = 1
        cnt[num] += 1
        sum += 1
        en += 1
    else:
        num = board[st]
        cnt[num] -= 1
        if(cnt[num] == 0):
            check[num] = 0
            count -= 1
        sum -= 1
        st += 1
    
    if(count <= 2):
        max_sum = max(max_sum, sum)
    
print(max_sum)


