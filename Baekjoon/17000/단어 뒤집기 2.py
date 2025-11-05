# 단어 뒤집기 2
# 처음에는 문자열에서 공백을 기준으로 분리한 후, < or > 기준으로 또 나눠야하나 싶었고 이 방식은 복잡하다고 생각했다
# 핵심은 < or >를 기준으로 어떻게 나누는 것이냐는데, queue를 사용하였다
# 현재 값이 < 이면 앞에 있는 애들을 다 뒤집어서 뺸 후 < 를 넣고
# 현재 값이 > 이면 앞에 있는 애들을 순차적으로 뺸 후(popleft()) > 를 넣는다

from collections import deque
Q = deque()

s = input().rstrip()

res = []
flag = False

for c in s:
    if c == ' ' and flag == False:
        while len(Q) > 0:
            res.append(Q.pop())
        res.append(' ')
    
    elif c == '>':
        while(len(Q) > 0):
            res.append(Q.popleft())
        res.append('>')
        flag = False

    elif c == '<':
        while(len(Q) > 0):
            res.append(Q.pop())
        res.append('<')
        flag = True
    
    else:
        Q.append(c)

while(len(Q) > 0):
    res.append(Q.pop())

print(''.join(res))