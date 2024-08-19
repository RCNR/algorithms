# 12891
# 슬라이딩 윈도우
import sys
input = sys.stdin.readline

S, P = map(int, input().split())
board = input().rstrip()
A, C, G, T = map(int, input().split())

def func(idx):
    if board[idx] == 'A': return 0
    if board[idx] == 'C': return 1
    if board[idx] == 'G': return 2
    if board[idx] == 'T': return 3

cnt = 0
st = 0
en = P-1

acgt = [0,0,0,0, 0]

for i in range(P):
    if board[i] == 'A': acgt[0] += 1
    if board[i] == 'C': acgt[1] += 1
    if board[i] == 'G': acgt[2] += 1
    if board[i] == 'T': acgt[3] += 1

while(True):
    if acgt[0] >= A and acgt[1] >= C and acgt[2] >= G and acgt[3] >= T:
        cnt += 1 
    
    en+=1
    if en==S: break
    num = func(en)
    acgt[num] += 1

    num = func(st)
    acgt[num] -= 1
    st+=1
    
print(cnt)