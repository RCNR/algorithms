# 1~9 => 1 => 9개
# 10 ~99 => 2 => 90개
# 100 ~ 999 => 3 => 900개
# 1000 ~ 9999 => 4 => 9000개
# 1. n 보다 작은 10의 제곱 수 개수 먼저 구하기
# 2. n의 10의 제곱 수 ~ n까지의 개수 구하기

n = int(input())
MOD = 1234567

length = len(str(n))
cnt = 0

for i in range(1, length):
  cnt += 9 * (10 ** (i - 1)) * i

cnt += (n - 10 ** (length - 1) + 1) * length

print(cnt%MOD)