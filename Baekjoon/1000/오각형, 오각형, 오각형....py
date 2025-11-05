# 1964 오각형, 오각형, 오각형...
# 더 빠르게
n = int(input())
inside = n * (n+1) // 2 % 45678
print(((inside * 3) + n + 1)% 45678) 