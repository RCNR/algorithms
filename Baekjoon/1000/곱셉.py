# 귀납적 사고
import sys
sys.setrecursionlimit(10**6)

def func(a, b, c):
    if b==1 : return a % c
    num = func(a, b//2, c)
    
    num = num * num % c # 12^4 = (12^2 * 12^2) % 19

    if b%2==0: return num
    return num * a % c

a, b, c = map(int, input().split())

res = func(a, b, c)

print(res)