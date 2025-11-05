# PNUPC에 한 번도 빠지지 않고 출연한 산지니가 새삼 대단하다고 느껴지네 33845 
a = input().rstrip()
b = input().rstrip()

new_a = set(a)
res = [c for c in b if c not in new_a]

print(''.join(res))