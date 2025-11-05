#2921
n = int(input())

# cnt = 0
# for i in range(n+1):
#     for j in range(i, n+1):
#         cnt += i+j
# print(cnt)

from itertools import combinations_with_replacement # 중복조합

cnt = 0
for i in combinations_with_replacement(range(n+1), 2): 
    cnt += sum(i) # i가 tuple 형태임
print(cnt)