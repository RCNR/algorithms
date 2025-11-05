# 17211
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

gg, gb ,bg, bb = map(float, input().split())

good = [0] * (n+1)
bad = [0] * (n+1)

if m==0:
    good[0] = 1
else:
    bad[0] = 1

for i in range(1, n+1):
    good[i] = good[i-1] * gg + bad[i-1] * bg
    bad[i] = bad[i-1] * bb + good[i-1] * gb

print(int(good[n] * 1000))
print(int(bad[n] * 1000))
