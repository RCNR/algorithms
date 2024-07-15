#17219
import sys
input = sys.stdin.readline

board = dict()

n,m = map(int, input().split())

for _ in range(n):
    url, password = map(str, input().split())
    board[url] = password

for _ in range(m):
    url = input().rstrip()
    print(board[url])