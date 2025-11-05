# A ~ B 사이의 소수를 구하고 그 소수의 N제곱한 값이 몇 개 있는지 카운트해야한다.
# sqrt(N)를 해서 제곱근까지의 소수를 구한다
# 그 소수들로 N제곱한 값이 B안에 들어있으면 카운트한다

# 거의 소수.py 1456

import math
n, m = map(int, input().split())

# 10^14 -> 제곱근 -> 10^7
a = [0] * (10000000 + 3)
cnt = 0

for i in range(2, len(a)):
    a[i] = i

for i in range(int(math.sqrt(len(a))) + 1):
    if a[i] == 0: continue

    for j in range(i+i, len(a), i):
        a[j] = 0

for i in range(2, 10000000 + 1):
    if a[i] != 0:
        temp = a[i]

        while a[i] * temp <= m:
            if a[i] * temp >= n:
                cnt += 1
            temp = temp * a[i]

print(cnt)
