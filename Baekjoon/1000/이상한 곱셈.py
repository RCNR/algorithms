# 1225
n, m = map(str, input().split())

sum = 0
for i in n:
    for j in m:
        sum += int(i) * int(j)
print(sum)

# O(n)으로 풀 수도 있다고 함
# 힌트:y(a+b)+z(a+b)=(y+z)(a+b)