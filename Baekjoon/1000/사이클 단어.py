# 사이클 단어.py 1544
# 해시 이용하기, 문자열

n = int(input())
board = list(input().rstrip() for _ in range(n))
res = set()

res.add(board[0])

for i in range(1, len(board)):
    flag = True
    is_exist = False
    new_s = board[i]

    for s in res:
        if len(s) == len(board[i]):
            is_exist = False
            flag = False
            check = board[i] + board[i]
            if s in check:
                # print(s, board[i], check)
                is_exist = True
                break
    if flag:
        res.add(board[i])
    if is_exist == False:
        res.add(new_s)

print(len(res))
# print(res)
            