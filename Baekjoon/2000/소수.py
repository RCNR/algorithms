# 2581 소수
n = int(input())
m = int(input())
res = []
for i in range(n, m+1):
    num = i
    if num == 1: continue
    check = True
    for j in range(2, (num//2)+1):
        if num % j == 0:
            check = False
            break
    if check == True:
        res.append(num)

if sum(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(res[0])
