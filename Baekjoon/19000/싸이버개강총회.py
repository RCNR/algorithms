# 싸이버개강총회.py 19583
# set 2개 이용해서 하나는 시작시간보다 작거나 같은지의 값 담당, 나머지 하나는 끝난 시간과 완전 끝난 시간 사이의 값 담당

import sys

input = sys.stdin.readline

S, E, Q = input().rstrip().split()
s = int(S[:2] + S[3:])
e = int(E[:2] + E[3:])
q = int(Q[:2] + Q[3:])

a = set()
b = set()


while(True):
    try:
        T, p = input().split()
        time = int(T[:2] + T[3:])

        if time <= s:
            a.add(p)
        elif e <= time <= q:
            b.add(p)
    except:
        break

print(len(a & b))
