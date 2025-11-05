n = int(input())
flag = False
res = 0

for i in range(n):
    sum = i
    k = str(i)
    for j in range(len(k)):
        sum += int(k[j])
    if sum == n:
            flag = True
            res = i
            break    

if flag:
    print(res)
else:
    print(0)
