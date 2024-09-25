# 32357
# 살짝 멍청하게 푼 방식 -> 굳이 포인터 두 개로 풀 이유가 없더라
import sys
input = sys.stdin.readline

n = int(input())

board = [input().rstrip() for _ in range(n)]

cnt = 0

for ary in board:
    s, e = 0, len(ary)-1
    flag = 1
    while(s<=e):
        if ary[s] != ary[e]:
            flag = 0
            break
        s += 1
        e -= 1
    if flag==0:
        continue
    else:
        cnt += 1

print(cnt * (cnt-1))
