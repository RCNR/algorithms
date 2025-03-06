# 1964 오각형, 오각형, 오각형...
n = int(input())
res = 5
for i in range(1, n):
    res += (3*i + 4) % 45678
print(res % 45678) 