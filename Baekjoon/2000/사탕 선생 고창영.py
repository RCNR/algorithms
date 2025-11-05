import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    input().rstrip()
    num = int(input())
    board = list(int(input()) for _ in range(num))
    res = sum(board)
    print("YES" if res % num == 0 else "NO")