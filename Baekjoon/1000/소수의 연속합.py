# 소수의 연속합 1644
# 테라토스테네스의 채를 이용한 소수 구하기 + 투 포인터로 경우의 수 구하기

n = int(input())

def is_prime(x):
    
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        
        if prime[i]:
            for j in range(i*i, n + 1, i): # i의 배수 제거 -> n까지
                prime[j] = False

    return [i for i in range(2, n+1) if prime[i]]



st = en = cnt = 0
board = is_prime(n)
board.append(0)
total = board[st]

for st in range(len(board)): # st 끝까지

    while en < len(board) - 1 and total < n:
        en += 1
        total += board[en]
    
    if en == len(board): break

    if total >= n:
        if total == n: cnt += 1
        total -= board[st]

print(cnt)

