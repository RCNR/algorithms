# 2018
# n이 천만 O(n^2)이면 시간초과 -> O(n)으로 풀어야함 -> 투 포인터 활용

n = int(input())
cnt = 0

s = 1
e = 1
sum = 0
while(s <= e):
    if e == n:
        cnt+=1
        break
    
    if sum == n:
        cnt+=1
        e+=1
        sum+=e
    elif sum < n:
        e+=1
        sum+=e
    else:
        sum-=s
        s+=1
print(cnt)
