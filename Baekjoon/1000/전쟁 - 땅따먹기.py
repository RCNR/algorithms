# 전쟁 - 땅따먹기.py 1270
# 병사 수가 매우 많다. 해시를 이용하자
from collections import defaultdict

t = int(input())
for _ in range(t):
    board = list(map(int, input().split()))
    check = defaultdict(int)
    for i in range(1, len(board)):
        check[board[i]] += 1
    
    max_value = max(check.values())

    keys = [k for k, v in check.items() if v == max_value]
    if len(keys) != 1:
        print("SYJKGW")
    elif check[keys[0]] <= board[0]//2:
        print("SYJKGW")
    else:
        print(*keys)
    