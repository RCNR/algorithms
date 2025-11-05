# 집합의 표현.py 1717
# union-find 기본 문제 -> 경로 압축 기법 사용, N 크기 상 최적화를 하지 않아도 풀린다.

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
p = [i for i in range(0, n+3)]

def find(num):
    if num != p[num]:
        p[num] = find(p[num])

    return p[num]

def func(u, v):
    u_p = find(u)
    v_p = find(v)
    
    if u_p == v_p: return
    p[u_p] = v_p

for _ in range(m):
    check, a, b = map(int, input().split())
    if check == 0: func(a, b)
    else:
        if find(a) == find(b): print('YES')
        else: print('NO')
