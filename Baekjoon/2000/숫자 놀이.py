# 2145
while(True):
    n = input().rstrip()
    if n == "0":
        break
    sum = 0
    while(len(n) >= 1):
        sum = 0
        for i in range(len(n)):
            sum += int(n[i])
        n = str(sum)
        k = sum
        if(len(n)==1): break
    print(k)

