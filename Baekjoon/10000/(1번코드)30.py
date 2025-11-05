# 10610
n = int(input())

num = str(n)
num = sorted(num, reverse=True)
new = ''.join(num)

if int(new) % 30 != 0:
    print(-1)
else:
    print(int(new))
