# 2292

n = int(input())

if n==1:
    print(1)
else:
    check = 2
    cnt = 1
    num = 6
    while check <= n:
        cnt += 1
        check += num
        num += 6
    print(cnt)
    