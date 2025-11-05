# 4619 루트
import sys
input = sys.stdin.readline

while True:
    B, N = map(int, input().split())
    if B== 0 and N == 0: break
    a = 1
    while True:
        res = pow(a, N)
        if B - res == 0:
            print(a)
            break
        
        if B - res < 0:
            if res - B < B - pow(a-1,N):
                print(a)
            else:
                print(a-1)
            break
            
        a += 1
        
