import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = input().rstrip()
    b = input().rstrip()
    cnt = sum(x != y for x, y in zip(a,b))
    print(f"Hamming distance is {cnt}.")
    
