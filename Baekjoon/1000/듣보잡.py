#1764
import sys
input = sys.stdin.readline

a = dict()
b = []

n, m = map(int, input().split())

for _ in range(n):
    str = input().rstrip()
    a[str] = 1

for _ in range(m):
    str = input().rstrip()
    if str in a:
        b.append(str)
        
b.sort()
print(len(b))
print(*b, sep='\n')

