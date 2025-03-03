# 후위 표기식 1918
from collections import deque
Q = deque()

ary = list(input().rstrip())
first = ['*', '/']
second = ['+', '-']
res = []

def func(op):
    while True:
        if len(Q) == 0 or Q[-1] == '(':
            Q.append(op)
            break

        if op in first:
            cur = Q[-1]
            if cur in first: # top의 우선순위 같은 경우 *, /
                res.append(Q.pop())
            else:
                Q.append(op) # top의 우선순위 낮은 경우
                break
        else:
            cur = Q.pop()
            res.append(cur)

for c in ary:
    if c.isalpha():
        res.append(c)
    elif c == '(':
        Q.append(c)
    elif c == ')': # 이 괄호이면 '(' 까지의 모든 연산자를 제거
        i = len(Q)-1
        while(Q[i] != '('):
            res.append(Q[i])
            Q.pop()
            i -= 1
        Q.pop() # 마지막 '('까지 제거
    else:
        func(c)

while len(Q) != 0:
    res.append(Q.pop())
print("".join(res))