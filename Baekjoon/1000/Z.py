from sys import setrecursionlimit
setrecursionlimit(10**6)

def func(n, r, c):
    if n==0: return 0
    half = (1<<(n-1))
    if (r<half and c<half): return func(n-1, r, c) # 1사
    elif (r<half and c>=half) : return 1*half*half + func(n-1, r, c-half) # 2사
    elif (r>=half and c<half) : return 2*half*half + func(n-1, r-half, c) # 3사
    else: return 3*half*half + func(n-1, r-half, c-half) # 4사

n, a, b = map(int, input().split())

print(func(n, a, b))